# speech to text vice versa
import pyttsx3
import speech_recognition as sr
# import subprocess
# from subprocess import Popen      //This will be for later to open applications on computer

import openai
openai.api_key = ""     # insert openai key here

# Initialize text-to-speech engine
engine = pyttsx3.init()


# Text to speech Function
def speak_text(command):

    engine.say(command)
    engine.runAndWait()


r = sr.Recognizer()


def record_text():
    # Loop if errors
    while 1:
        try:
            # Use mic as source input
            with sr.Microphone() as source2:

                # Prepare recognizer to receive input
                r.adjust_for_ambient_noise(source2, duration=0.2)

                print("I'm listening")

                # listens for user's input
                audio2 = r.listen(source2)

                # using google to recognize audio
                myText = r.recognize_google(audio2)

                return myText

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("Unknown error occurred")


def send_to_chatGPT(messages, model="gpt-3.5-turbo"):

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].message.content   # Dissect that response to get message from chatGPT
    messages.append(response.choices[0].message)    # Update messages array, append dictionary format to messages array
    return message


messages = [{"role": "user", "content": "Act like Jarvis from Iron Man."}]  # To make it act like Jarvis before convo
while 1:
    text = record_text()
    messages.append({"role": "user", "content": text})
    response = send_to_chatGPT(messages)
    speak_text(response)

    print(response)