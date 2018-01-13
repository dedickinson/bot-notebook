# Farcical recognition

First, install Python 3.6

Then: 

````
sudo port install opencv +python36
python -m venv venv
. venv/bin/activate
pip install opencv-python
./app.py haarcascade_frontalface_default.xml
````
Windows:
````
pip install opencv-python
python -m venv venv # doesn't appear to do anything?
python app.py haarcascade_frontalface_default.xml
````
