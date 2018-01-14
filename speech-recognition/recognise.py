#!/usr/bin/env python3

# Based on: https://raw.githubusercontent.com/Uberi/speech_recognition/master/examples/microphone_recognition.py


import os.path
import speech_recognition as sr

with open(os.path.expanduser('~/.azurekeys/speechapi'), 'r') as api_key_file:
    bing_key = api_key_file.readline().strip('\n')

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Sphinx
try:
    sphinx_output = r.recognize_sphinx(audio)
    print(f"Sphinx thinks you said: {sphinx_output}")
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# Microsoft Bing Voice Recognition
try:
    bing_output = r.recognize_bing(audio, key=bing_key)
    print(f"Microsoft Bing Voice Recognition thinks you said: {bing_output}")
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
