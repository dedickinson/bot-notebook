#!/usr/bin/env python3
from espeakng import ESpeakNG
from num2words import num2words

esng = ESpeakNG()

print("Get ready")
esng.say('Hello World!')
esng.say(f"The secret number is {num2words(42)}")
print("Did it work?")