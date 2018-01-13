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

pip3 install pocketsphinx

pip3 install --global-option='build_ext' \
            --global-option='-I/opt/local/include' \
            --global-option='-L/opt/local/lib' pyaudio
````


## References

- https://github.com/cmusphinx/pocketsphinx-python