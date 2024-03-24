import sqlite3
from gtts import gTTS
import os
import sounddevice as sd
import numpy as np
import librosa
import alsaaudio
import pygame.mixer

# def abort_audio_and_run_classify():
#     global audio_process
#     global classification
#     global pid
    
#     mp3_classification = classification.replace(' ', '_').replace('(', '').replace(')', '').lower()
#     print('playing: ', mp3_classification)
#     # Abort currently playing audio
#     # Abort currently playing audio
#     if audio_process:
#         # Attempt to kill the audio process
#         try:
#             os.system("kill {}".format(pid))
#         except Exception as e:
#             print("Error while terminating audio process:", e)
        
#         # Run classify() function
#         classify_thread = threading.Thread(target=classify, args=(root,), daemon=True)
#         classify_thread.start()

# def signal_handler(sig, frame):
#     global audio_process, classify_thread, pid
#     # Handle the SIGTERM signal gracefully
#     print("Received SIGTERM signal. Terminating audio playback gracefully.")
#     if audio_process:
#         # Perform cleanup operations before terminating the audio process
#         os.system("kill {}".format(pid))

#     # Start the classify thread after terminating the audio process
#     classify_thread = threading.Thread(target=classify, args=(root,), daemon=True)
#     classify_thread.start()

#     exit(0)

# # Register the signal handler for SIGTERM
# signal.signal(signal.SIGTERM, signal_handler)

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
    # sound = AudioSegment.from_mp3(mp3_path)
    # play(sound)
    

    # 
    # pid = os.popen("pgrep -f 'play audio.mp3'").read().strip()
    # return pid
    

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

def speak_introductory_audio():
    # Initialize audio processing library
    pygame.mixer.pre_init(frequency=25000, 
                        size=-16, 
                        channels=2, 
                        buffer=512, 
                        devicename=None, 
                        allowedchanges=pygame.AUDIO_ALLOW_FREQUENCY_CHANGE | pygame.AUDIO_ALLOW_CHANNELS_CHANGE)
    pygame.mixer.init()

    intro_audio = pygame.mixer.Sound('/home/pi/capstone/pill-identification/introductory_audio.wav')
    audio_path = pygame.mixer.Sound(intro_audio)
    pygame.mixer.Sound.play(audio_path)

if __name__ == "__main__":
    # speak_pill_info('Glucophage XR Metformin HCl 750mg (Unpacked)')
    speak_introductory_audio()