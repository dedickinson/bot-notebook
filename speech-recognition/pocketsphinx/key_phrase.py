#!/usr/bin/env python3

# https://github.com/bambocher/pocketsphinx-python

import os
from pocketsphinx import LiveSpeech, get_model_path

MODELDIR = "model/en-us"

speech = LiveSpeech(
    keyphrase='forward',
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(MODELDIR, 'en-us'),
    lm=os.path.join(MODELDIR, 'en-us.lm.bin'),
    dic=os.path.join(MODELDIR, 'cmudict-en-us.dict')
)

for phrase in speech:
    print(phrase)
