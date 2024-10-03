import streamlit as st
import speech_recognition as sr
import google.generativeai as genai
import os
import re
from gtts import gTTS

# Set your Google API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyCBvmXKy8Y_--jD4E4kSvhevlepqa9huZM"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize session state to keep track of the conversation and user data
if 'generated_responses' not in st.session_state:
    st.session_state['generated_responses'] = []

# Function to perform speech to text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        st.write("Listening...")

        audio = recognizer.listen(source)

        try:
            st.write("Recognizing...")
            text = recognizer.recognize_google(audio)
            return text

        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

# Function to clean and sanitize the text
def clean_text(text):
    cleaned = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    cleaned = re.sub(r'\d+', '', cleaned)  # Remove digits
    return cleaned.strip()

# Function to convert text to speech using gTTS and save as an audio file
def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    audio_file = "output.mp3"  # Use a timestamped filename
    tts.save(audio_file)
    return audio_file

# Function to generate response from LLM
def generate_llm_response(text):
    try:
        response = model.generate_content(text)
        return response.text
    except Exception as e:
        return f"Error generating content: {str(e)}"

# Streamlit application layout with sidebar for user selections
st.title("Speech-to-Speech LLM Bot")
st.sidebar.title("Settings")
language = st.sidebar.selectbox('Select Language for TTS', ['en', 'es', 'fr', 'de'])

if st.button("Start Recording"):
    with st.spinner('Listening...'):
        spoken_text = speech_to_text()
        st.write("You said: ", spoken_text)

    if spoken_text and "Sorry" not in spoken_text:
        with st.spinner('Generating response...'):
            generated_text = generate_llm_response(spoken_text)
            st.write("Bot says: ", generated_text)

            # Clean and convert the generated text to speech
            cleaned_text = clean_text(generated_text)
            audio_file = text_to_speech(cleaned_text)

        # Save the response in session state for future reference or logging
        st.session_state['generated_responses'].append({
            'input': spoken_text,
            'output': generated_text,
        })

audio_file = 'output.mp3'
# Enable audio playback
if st.button("Play Generated Audio"):
    audio_file_obj = open(audio_file, 'rb')
    audio_bytes = audio_file_obj.read()
    st.audio(audio_bytes, format='audio/mp3')

# Display the conversation history
if st.sidebar.checkbox('Show Conversation History'):
    st.sidebar.write("Conversation History:")
    for i, conv in enumerate(st.session_state['generated_responses']):
        st.sidebar.write(f"{i+1}. You: {conv['input']}")
        st.sidebar.write(f"   Bot: {conv['output']}")
