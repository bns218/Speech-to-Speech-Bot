import os
import streamlit as st
import tempfile
import ollama
from gtts import gTTS
import speech_recognition as sr
import io
import sounddevice as sd
import soundfile as sf
from playsound import playsound
import time


# Initialize speech recognizer
recognizer = sr.Recognizer()

# Streamlit UI
st.title("🎙️ Speech-to-Speech with LLM & Text Display")
st.info("Click to record, process with Ollama, and hear the response.")

# Record audio
def record_audio(filename, duration=5, fs=16000):
    st.write("Recording... Speak now!")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    sf.write(filename, recording, fs)
    return filename

# Convert Speech to Text
def speech_to_text(audio_file_path):
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)
        try:
            transcript = recognizer.recognize_google(audio)  # Uses Google's free API
            return transcript
        except sr.UnknownValueError:
            raise Exception("Speech could not be understood")
        except sr.RequestError:
            raise Exception("Could not request results from speech recognition service")


# Process with Ollama
def process_with_llm(prompt):
    if not prompt or len(prompt.strip()) == 0:
        raise ValueError("Empty prompt received")
    
    try:
        # Using a more standard model name
        model = ollama.chat(
            model='llama3.2',  # Using the installed Gemma model
            messages=[
                {'role': 'user', 'content': prompt}
            ]
        )
        
        if not model or 'message' not in model or 'content' not in model['message']:
            raise ValueError("Invalid response format from Ollama")
        
        response = model['message']['content']
        if not response:
            return "I apologize, but I couldn't generate a response. Please try again."
        return response
    except Exception as e:
        print(f"Error in process_with_llm: {str(e)}")
        return "I apologize, but there was an error processing your request. Please ensure Ollama is running and try again."

# Convert Text to Speech
def text_to_speech(text, filename="output.mp3"):
    try:
        # Process the entire text for speech first
        temp_dir = tempfile.gettempdir()
        full_audio = os.path.join(temp_dir, f"full_{filename}")
        tts = gTTS(text, lang='en', slow=False)  # Set slow=False for faster speech
        tts.save(full_audio)
        
        # Display words one by one quickly
        words = text.split()
        display_text = st.empty()
        current_text = ""
        
        # Play the full audio in background
        import threading
        audio_thread = threading.Thread(target=lambda: playsound(full_audio))
        audio_thread.start()
        
        # Display words rapidly
        for word in words:
            current_text += word + " "
            display_text.markdown(f"### {current_text}")
            time.sleep(0.4)  # Quick delay for word display
            
        # Wait for audio to finish
        audio_thread.join()
        
        # Clean up the temporary file
        try:
            os.remove(full_audio)
        except:
            pass
            
    except Exception as e:
        st.error(f"Error playing audio: {str(e)}")
        print(f"Error in text_to_speech: {str(e)}")
            
    except Exception as e:
        st.error(f"Error playing audio: {str(e)}")
        print(f"Error in text_to_speech: {str(e)}")

# Streamlit Button to Trigger Workflow
if st.button("🎤 Record and Process"):
    with st.spinner("Listening..."):
        audio_path = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
        record_audio(audio_path)

    with st.spinner("Transcribing..."):
        try:
            transcribed_text = speech_to_text(audio_path)
            st.success(f"You said: {transcribed_text}")
        except Exception as e:
            st.error("Speech recognition failed.")
            st.stop()    
    with st.spinner("Processing with Ollama..."):
        try:
            response_text = process_with_llm(transcribed_text)
            st.write("💬 Ollama Response:")
        except Exception as e:
            st.error("Ollama failed to generate a response.")
            st.stop()

    with st.spinner("Speaking the response..."):
        text_to_speech(response_text)
        st.success("Done! ✅")

    # Clean up the audio file
    try:
        os.remove(audio_path)
    except:
        pass