# Speech recognition

For this project I'll setup a basic speech recognition app that uses
[CMUSphinx](https://cmusphinx.github.io/) to locally run speech recognition.

I'll use [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) to capture sound 
from the microphone.

## Prepare

### OS X

````
sudo port install portaudio swig-python
````

## Setup

````
virtualenv -p python3.6 venv
. venv/bin/activate

pip install pocketsphinx

pip install --global-option='build_ext' \
            --global-option='-I/opt/local/include' \
            --global-option='-L/opt/local/lib' pyaudio

pip install SpeechRecognition
````

Note: Check `requirements.txt` in case this doco has lagged.

### Hotwords (Snowboy)

_NOTE_: I haven't managed to get Snowboy running under Python 3 yet.

The `pmdl` files under the `hotwords` directory are created using [Snowboy](https://snowboy.kitt.ai).

````
sudo port install swig portaudio sox gettext
pip install pyaudio
git clone git@github.com:Kitt-AI/snowboy.git
cd snowboy/swig/Python3/
make
````

Refer to https://github.com/kitt-ai/snowboy

## References

- https://github.com/Uberi/speech_recognition
- https://github.com/cmusphinx/pocketsphinx-python