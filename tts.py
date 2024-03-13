import sqlite3
from gtts import gTTS
import os
import sounddevice as sd
import numpy as np
import librosa
import alsaaudio

# Database connection information
pill_database = "/home/pi/capstone/pill-identification/database/pill_info.db"
pill_table = "pill_info_table"
mp3_folder = "/home/pi/capstone/pill-identification/mp3"

# Set tempo
tempo = 1.1

# Initialize ALSA mixer
mixer = alsaaudio.Mixer()

# Initialize buttons values
volume_factor = 50  # Starting volume (range: 0-100)

def speak_pill_info(classification):
    global tempo
    mp3_classification = classification.replace(' ', '_').replace('(', '').replace(')', '').lower()
    mp3_path = os.path.join(mp3_folder, f"{mp3_classification}.mp3")
    print('mp3_path: ', mp3_path)
    os.system("play %s tempo %s" % (mp3_path, tempo))

# Function to play audio with volume adjustment
# def play_audio_with_volume(audio_data):
#     global volume_factor
#     sd.play(volume_factor / 100 * audio_data, samplerate=44100, blocking=True)

# Function to increase volume using ALSA
def increase_volume():
    global volume_factor
    volume_factor = min(volume_factor + 10, 100)  # Increase volume by 10 (max 100)
    mixer.setvolume(volume_factor)
    print('Volume: ', volume_factor)

# Function to decrease volume using ALSA
def decrease_volume():
    global volume_factor
    volume_factor = max(volume_factor - 10, 0)  # Decrease volume by 10 (min 0)
    mixer.setvolume(volume_factor)
    print('Volume: ', volume_factor)

if __name__ == "__main__":
    speak_pill_info('Glucophage XR Metformin HCl 750mg (Unpacked)')
    # Example usage: adjust volume by 10 dB
    # audio_data, _ = librosa.load("output.mp3", sr=44100)
    # play_audio_with_volume(audio_data)