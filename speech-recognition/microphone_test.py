#!/usr/bin/env python3

"""
PyAudio Example: Records 5 seconds of audio and plays it back

Based on https://stackoverflow.com/questions/46768459/python-recording-and-playing-microphone-input
"""

import pyaudio

CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

data = []

print("* recording started")
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data.append(stream.read(CHUNK))  #read audio stream

print("* recording done")

print("* playback started")
for el in data:
    stream.write(el)  #play back audio stream
print("* playback done")

stream.stop_stream()
stream.close()

p.terminate()