import datetime
from gtts import gTTS
import os
import sounddevice as sd
import numpy as np
import pyttsx3
import alsaaudio
import pygame.mixer
import datetime

# Database connection information
pill_database = "/home/pi/capstone/pill-identification/database/pill_info.db"
pill_table = "pill_info_table"
mp3_folder = "/home/pi/capstone/pill-identification/mp3"
pill_info_wav_folder = "/home/pi/capstone/pill-identification/wav/pill_info"
rtc_wav_folder = "/home/pi/capstone/pill-identification/wav/rtc"

# Initialize buttons values
volume_factor = 50  # Starting volume (range: 0-100)

# # Initialize ALSA mixer
mixer = alsaaudio.Mixer()

def speak_pill_info(classification, channel):
    wav_classification = classification.replace(' ', '_').replace('(', '').replace(')', '').lower()
    wav_path = os.path.join(pill_info_wav_folder, f"{wav_classification}.wav")
    print('wav_path', wav_path)
    audio_path = pygame.mixer.Sound(wav_path)
    channel.play(audio_path)
    return False

def speak_rtc(channel):
    hour = datetime.datetime.now().time().strftime("%H")
    minute = datetime.datetime.now().time().strftime("%M")
    print('h:', hour)
    print('m:', minute)
    if int(hour) == 12:
        am_pm_path = os.path.join(rtc_wav_folder, 'PM.mp3')
    elif int(hour) > 12:
        hour = int(hour) - 12
        am_pm_path = os.path.join(rtc_wav_folder, 'PM.mp3')
    else: am_pm_path = os.path.join(rtc_wav_folder, 'AM.mp3')
    rtc_hour_path = os.path.join(rtc_wav_folder, f"{hour}.mp3")
    print('hour:', rtc_hour_path)
    
    if int(minute) == 0: 
        rtc_min_path = os.path.join(rtc_wav_folder, f"oclock.mp3")
    elif int(minute) < 10:
        rtc_min_path = os.path.join(rtc_wav_folder, f"oh_{minute}.mp3")
    else: 
        rtc_min_path = os.path.join(rtc_wav_folder, f"{minute}.mp3")
    print(rtc_min_path)
    
    current_time_path = os.path.join(rtc_wav_folder, "current_time.mp3")
    print(current_time_path)

    os.system("play {} tempo 1.1" .format(current_time_path))
    os.system("play {} tempo 1.1" .format(rtc_hour_path))
    os.system("play {} tempo 1.1" .format(rtc_min_path))
    os.system("play {} tempo 1.1" .format(am_pm_path))

    
def speak_error_audio():
    error_path = '/home/pi/capstone/pill-identification/error_audio.mp3'
    os.system("play {} tempo 1.1" .format(error_path))
    
def speak_introductory_audio():
    intro_audio_path = '/home/pi/capstone/pill-identification/introductory_audio.mp3'
    os.system("play {} tempo 1.1" .format(intro_audio_path))



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
    set_frequency = 25000
    # Initialize audio processing library
    pygame.mixer.pre_init(frequency=set_frequency, size=-16, channels=2, buffer=512, devicename=None, allowedchanges=pygame.AUDIO_ALLOW_FREQUENCY_CHANGE | pygame.AUDIO_ALLOW_CHANNELS_CHANGE)
    pygame.mixer.init()
    channel = pygame.mixer.Channel(0)
    print('channel: ', channel.get_busy())
    # speak_pill_info('Glucophage XR Metformin HCl 750mg (Unpacked)', channel)
    # # speak_introductory_audio(channel)
    # speak_error_audio()
    # os.system(f'Current time: {datetime.datetime.now().time().strftime("%H:%M:%S")}')
    speak_rtc(channel)