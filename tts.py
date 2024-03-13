import sqlite3
from gtts import gTTS
import os
# from pydub import AudioSegment
# from pydub.playback import play
import sounddevice as sd
import numpy as np
import librosa
import alsaaudio

# Database connection information
pill_database = "/home/pi/capstone/pill-identification/database/pill_info.db"
pill_table = "pill_info_table"

tempo = 1.1

# Initialize ALSA mixer
mixer = alsaaudio.Mixer()

# Initialize buttons values
volume_factor = 50  # Starting volume (range: 0-100)

def connect_to_database():
    """
    Establishes a connection to the SQLite database.

    Returns:
        sqlite3.Connection: The database connection object.
    """
    conn = sqlite3.connect(pill_database)
    return conn

def get_pill_info(classification):
    """
    Queries the database for information about a specific pill.

    Args:
        classification: The name of the pill (identified by the main script).

    Returns:
        tuple: A tuple containing pill information (name, description, etc.) if found, otherwise None.
    """
    conn = connect_to_database()
    cursor = conn.cursor()
    columns = ['medication_name', 'dosage', 'special_instructions', 'possible_side_effects']
    cursor.execute(f"SELECT {','.join(columns)} FROM pill_info_table WHERE medication_name_dosage = ?", (classification,))
    pill_info = cursor.fetchone()
    conn.close()
    return pill_info

def speak(message):
    global tempo
    tts = gTTS(text=message, lang='en', tld='us', slow=False)

    # Save the speech as an audio file
    tts.save("output.mp3")

    # Play the audio file 
    # os.system("mpg321 output.mp3")  
    os.system("play output.mp3 tempo %s" % (tempo))

def speak_pill_info(pill_info, language='en'):
    """
    Retrieves information from the database and speaks it using text-to-speech.

    Args:
        classification: The name of the pill (identified by the main script).
    """
    
    if pill_info:
        global tempo
        # Construct speech message from pill information
        message = f"The pill is identified as {pill_info[0]} with a dosage of {pill_info[1]} milligrams. {pill_info[2]}. {pill_info[3]}"  # Replace with actual data access

        # Use gTTS to convert text to speech
        tts = gTTS(text=message, lang=language, tld='us', slow=False)
        
        # Save the speech as an audio file
        tts.save("output.mp3")

        # Play the audio file (assuming you have a media player installed)
        # os.system("mpg321 output.mp3")  # Adjust the command based on your system
        
        os.system("play output.mp3 tempo %s" % (tempo))

    else:
        speak("Pill information not found.")

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
    # pinfo = get_pill_info('Glucophage Metformin HCl 1g (Packed)')     
    # speak_pill_info(pinfo)
    # Example usage: adjust volume by 10 dB
    audio_data, _ = librosa.load("output.mp3", sr=44100)
    play_audio_with_volume(audio_data)