# Speech-to-Text and Text-to-Speech Assistant using OpenAI's ChatGPT

This Python script demonstrates a simple speech-to-text and text-to-speech assistant integrated with OpenAI's ChatGPT model. The assistant listens to user input, converts it to text, sends it to the ChatGPT model for processing, and then responds with synthesized speech.

## Requirements:
- Python 3.x
- `pyttsx3` for text-to-speech conversion
- `speech_recognition` for speech-to-text conversion
- OpenAI's `openai` Python package for interacting with the ChatGPT model

## Installation:
1. Install required packages:
pip install pyttsx3 speech_recognition openai

2. Set up an OpenAI API key and replace `openai.api_key = ""` with your API key.

## Usage:
1. Run the script.
2. Start speaking after the prompt "I'm listening".
3. The assistant converts your speech to text, sends it to ChatGPT, and responds with synthesized speech.

## Features:
- Records user input via microphone.
- Utilizes Google's speech recognition to convert speech to text.
- Sends text input to ChatGPT for generating responses.
- Synthesizes ChatGPT's responses into speech for the user.

## Note:
- This script assumes continuous speech interaction. It loops indefinitely, waiting for user input and responding accordingly.
- Adjust the `model` parameter in the `send_to_chatGPT` function to use different versions or variants of the ChatGPT model.
- Additional functionalities such as opening applications on the computer can be implemented using `subprocess` module, as commented out in the code.

## References:
- [pyttsx3 Documentation](https://pyttsx3.readthedocs.io/en/latest/)
- [SpeechRecognition Documentation](https://github.com/Uberi/speech_recognition)
- [OpenAI API Documentation](https://beta.openai.com/docs/)
