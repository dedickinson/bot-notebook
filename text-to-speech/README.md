# eSpeak NG

There are two aspects to getting your system to speak:

1. Output audio: 
    - On Mac: [CoreAudio](https://developer.apple.com/library/content/documentation/MusicAudio/Conceptual/CoreAudioOverview/WhatisCoreAudio/WhatisCoreAudio.html#//apple_ref/doc/uid/TP40003577-CH3-SW1)
    - On Linux: [PulseAudio](https://www.freedesktop.org/wiki/Software/PulseAudio/)
1. Convert text to speech
    - I'll use [eSpeak-NG](https://github.com/espeak-ng/espeak-ng)

## On a Mac

First we build and install [pcaudiolib](https://github.com/espeak-ng/pcaudiolib)
to provide cross-platform audio abstraction. Then, build and compile
[eSpeak-NG](https://github.com/espeak-ng/espeak-ng).

````
sudo port install autoconf automake libtool pkgconfig

git clone https://github.com/espeak-ng/pcaudiolib.git
cd pcaudiolib
./autogen.sh
./configure
make
sudo make install

cd ..

git clone https://github.com/espeak-ng/espeak-ng.git
cd espeak-ng
./autogen.sh
./configure
make
sudo make install
````

Then run `espeak-ng "hello, world"` or `espeak-ng -v en-gb-scotland "hello, world"`

# Python

````
pip install py-espeak-ng num2words
````