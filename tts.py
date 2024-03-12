import sqlite3
from gtts import gTTS
import os
from io import BytesIO
import pygame


# Database connection information
pill_database = "pill_info.db"
pill_table = "pill_info_table"

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
    tts = gTTS(text=message, lang='en', tld='co.in', slow=False)

    # Save the speech as an audio file
    tts.save("output.mp3")

    # Play the audio file 
    os.system("mpg321 output.mp3")  

def speak_pill_info(pill_info, language='en'):
    """
    Retrieves information from the database and speaks it using text-to-speech.

    Args:
        classification: The name of the pill (identified by the main script).
    """
    
    if pill_info:
        # Create mp3 file object
        mp3_fo = BytesIO()
        
        # Construct speech message from pill information
        message = f"The pill is identified as {pill_info[0]} with a dosage of {pill_info[1]} milligrams. {pill_info[2]}. {pill_info[3]}"  # Replace with actual data access

        # Use gTTS to convert text to speech
        tts = gTTS(text=message, lang=language, tld='us', slow=False)

        tts.write_to_fp(mp3_fo)
        
        # # Rewind the MP3 object to the beginning
        # mp3_fo.seek(0)

        # # Initialize Pygame mixer
        # pygame.mixer.init()

        # # Load the MP3 data from the memory object
        # pygame.mixer.music.load(mp3_fo)
        # pygame.mixer.music.play()
        
        # Save the speech as an audio file
        tts.save("output.mp3")

        # Play the audio file (assuming you have a media player installed)
        os.system("mpg321 output.mp3")  # Adjust the command based on your system

    else:
        speak("Pill information not found.")

if __name__ == "__main__":
    pinfo = get_pill_info('Jardiance FC Empagliflozin 10mg (Unpacked Side B)')     
    speak_pill_info(pinfo)