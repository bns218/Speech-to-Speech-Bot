# 🎙️ Speech-to-Speech Bot

A streamlined voice-based AI platform that enables natural conversation with a Large Language Model (LLM) using speech input and output. The system provides a seamless voice interaction experience with real-time visual feedback.

## 🌟 Features

- **Speech-to-Text Conversion**:
  - Google Speech Recognition API for accurate transcription
  - Real-time audio capture
  - Clear error handling

- **Text Generation**: 
  - Integration with Ollama for LLM-based responses
  - Real-time text display with word-by-word animation
  - Robust error handling for LLM interactions

- **Text-to-Speech Synthesis**:
  - Google Text-to-Speech (gTTS) for high-quality voice output
  - Background audio playback with synchronized text display
  - Efficient temporary file management

- **User Interface**:
  - Clean Streamlit-based interface
  - Language selection
  - Recording duration control
  - Knowledge base status display
  - Conversation history tracking

## 🛠️ Architecture

### Components

1. **Frontend Layer (Streamlit)**
   - User interface components
   - Audio recording interface
   - Real-time feedback and status updates
   - Settings management

2. **Speech Processing Layer**
   - Speech recognition (Google API, Whisper)
   - Text-to-Speech synthesis (gTTS)
   - Audio processing (sounddevice, soundfile)

3. **Natural Language Processing Layer**
   - LLM integration (Ollama)
   - Sentence transformers for embeddings
   - NLTK for text processing

4. **Knowledge Base Layer**
   - ChromaDB for vector storage
   - Document processing
   - Semantic search
   - Context retrieval

## 📋 Requirements

```txt
streamlit
SpeechRecognition
gtts
sounddevice
soundfile
ollama
playsound==1.2.2
```

## 🚀 Getting Started

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Ollama**
   - Follow instructions at [Ollama's website](https://ollama.ai)
   - Pull the required model:
     ```bash
     ollama pull llama3.2
     ```

3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## 💡 Implementation Notes

### Speech Processing
- Uses `sounddevice` for real-time audio recording at 16kHz
- Audio saved in WAV format for compatibility
- Google Speech Recognition API for accurate transcription
- Automatic cleanup of temporary audio files

### LLM Integration
- Direct integration with Ollama's local LLM
- Uses llama3.2 model for natural responses
- Robust error handling for model interactions
- Clear feedback on processing status

### User Experience
- Word-by-word display synchronized with audio
- Background audio playback using threading
- Comprehensive error handling with user-friendly messages
- Clean and intuitive single-button interface

### File Structure
- `app.py`: Main application file
- `requirements.txt`: Required dependencies

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -am 'Add: YourFeature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Submit a pull request

### Areas for Enhancement
- Support for longer conversations with context memory
- Additional LLM model options
- Customizable voice selection for text-to-speech
- Adjustable recording duration
- Language selection support

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## 🤝 Contributing

Feel free to contribute to this project by:
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is open source and available under the MIT License.
