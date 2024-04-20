import datetime
import os
import alsaaudio
import pygame.mixer
import datetime

# Database connection information
pill_database = "/home/pi/capstone/pill-identification/database/pill_info.db"
pill_table = "pill_info_table"
mp3_folder = "/home/pi/capstone/pill-identification/mp3"
pill_info_wav_folder = "/home/pi/capstone/pill-identification/wav/pill_info"
rtc_wav_folder = "/home/pi/capstone/pill-identification/wav/rtc"
am_pm = ''

# Initialize buttons values
volume_factor = 50  # Starting volume (range: 0-100)

# # Initialize ALSA mixer
mixer = alsaaudio.Mixer()

def speak_pill_info(classification, channel):
    # Plays audio containing pill info based on classification
    wav_classification = classification.replace(' ', '_').replace('(', '').replace(')', '').lower()
    wav_path = os.path.join(pill_info_wav_folder, f"{wav_classification}.wav")
    print('wav_path', wav_path)
    audio_path = pygame.mixer.Sound(wav_path)
    channel.play(audio_path)
    return audio_path.get_length()

def speak_rtc(channel):
    # Plays current time audio
    current_time_path = os.path.join(rtc_wav_folder, "classif_time.wav")
    current_time = pygame.mixer.Sound(current_time_path)
    channel.play(current_time)
    return current_time.get_length()

def speak_hour(channel):
    # Plays hour audio based on datetime module
    global am_pm
    hour = datetime.datetime.now().time().strftime("%H")
    print('h:', hour)
    if int(hour) == 12:
        am_pm = 'PM'
    elif int(hour) > 12:
        hour = int(hour) - 12
        am_pm = 'AM'
    rtc_hour_path = os.path.join(rtc_wav_folder, f"{hour}.wav")
    hour_audio = pygame.mixer.Sound(rtc_hour_path)
    channel.play(hour_audio)
    return hour_audio.get_length()

def speak_min(channel):
    # Plays min audio based on datetime module
    minute = datetime.datetime.now().time().strftime("%M")
    print('m:', minute)
    if int(minute) == 0: 
        rtc_min_path = os.path.join(rtc_wav_folder, f"oclock.wav")
    elif int(minute) < 10:
        rtc_min_path = os.path.join(rtc_wav_folder, f"oh_{minute}.wav")
    else: 
        rtc_min_path = os.path.join(rtc_wav_folder, f"{minute}.wav")
    min_audio = pygame.mixer.Sound(rtc_min_path)
    channel.play(min_audio)
    return min_audio.get_length()

def speak_am_pm(channel):
    # Plays AM/PM audio based on datetime module
    global am_pm
    if am_pm == 'PM':
        am_pm_path = os.path.join(rtc_wav_folder, 'PM.wav')
    else: am_pm_path = os.path.join(rtc_wav_folder, 'AM.wav')
    channel.play(pygame.mixer.Sound(am_pm_path))
    
def speak_error_audio():
    # Plays error classification audio 
    error_path = '/home/pi/capstone/pill-identification/wav/error_audio.mp3'
    os.system("play {} tempo 1.1" .format(error_path))
    
def speak_introductory_audio():
    # Plays introductory audio
    intro_audio_path = '/home/pi/capstone/pill-identification/wav/introductory_audio.mp3'
    os.system("play {} tempo 1.1" .format(intro_audio_path))


def increase_volume():
    # Function to increase volume using ALSA
    global volume_factor
    volume_factor = min(volume_factor + 10, 100)  # Increase volume by 10 (max 100)
    mixer.setvolume(volume_factor)
    print('Volume: ', volume_factor)


def decrease_volume():
    # Function to decrease volume using ALSA
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