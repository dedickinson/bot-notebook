#!/usr/bin/env python3

"""
PyAudio Example: 
  - Records 5 seconds of audio
  - Saves it to a WAV file
  - Plays the file back
"""

import wave
import pyaudio

def captureInput(p, duration = 5, audio_format = pyaudio.paInt16, channels = 2, rate = 44100, frames_per_buffer = 1024):
    p = pyaudio.PyAudio()
    data = []

    stream = p.open(format=audio_format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=frames_per_buffer)

    print("* recording started")
    for i in range(0, int(rate / frames_per_buffer * duration)):
        data.append(stream.read(frames_per_buffer))  #read audio stream

    print("* recording done")

    stream.stop_stream()
    stream.close()
    return data


def saveToWavFile(p, data, filename = "output.wav", audio_format = pyaudio.paInt16, channels = 2, rate = 44100):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(audio_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(data))
    wf.close()

def playWavFile(p, filename = "output.wav", frames_per_buffer = 1024):
    wf = wave.open(filename, 'rb')

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(frames_per_buffer)

    while data:
        stream.write(data)
        data = wf.readframes(frames_per_buffer)

    print('done')
    stream.stop_stream()
    stream.close()
    wf.close()
    return


p = pyaudio.PyAudio()
frames = captureInput(p)
saveToWavFile(p, frames)
playWavFile(p)
p.terminate()
