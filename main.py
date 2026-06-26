from gtts import gTTS
import os
from mutagen.mp3 import MP3
import time

#Text to Speech___________

language = 'es-us'

def speak(text):
    speech = gTTS(text= text, lang= language, slow= False)
    speech.save("texto.mp3")
    os.system("start texto.mp3")
    audio = MP3("texto.mp3")
    time.sleep(audio.info.length + 0.5)
