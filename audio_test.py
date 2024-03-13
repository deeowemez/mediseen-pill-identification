import sounddevice as sd
import numpy as np
import librosa

def play_audio_with_volume(audio_data, volume_factor=1.0):
    # Adjust the volume of the audio data
    adjusted_audio = volume_factor * audio_data

    # Play the audio in real-time
    sd.play(adjusted_audio, samplerate=44100)
    sd.wait()

if __name__ == '__main__':
    audio_data, _ = librosa.load("output.mp3", sr=44100)
    play_audio_with_volume(audio_data, volume_factor=1.0)
