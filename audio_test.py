import pygame
import tts

# Initialize audio processing library
set_frequency = 25000
pygame.mixer.pre_init(frequency=set_frequency, size=-16, channels=2, buffer=512, devicename=None, allowedchanges=pygame.AUDIO_ALLOW_FREQUENCY_CHANGE | pygame.AUDIO_ALLOW_CHANNELS_CHANGE)
pygame.mixer.init()
channel = pygame.mixer.Channel(0)
tts.speak_introductory_audio()