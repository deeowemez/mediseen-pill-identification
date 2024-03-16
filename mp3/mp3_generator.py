import sqlite3
from gtts import gTTS
import os
# import sounddevice as sd
# import numpy as np
# import librosa
# import alsaaudio

# Database connection information
# pill_database = "/home/pi/capstone/pill-identification/database/pill_info.db"
# mp3_folder = "/home/pi/capstone/pill-identification/mp3"
pill_database = r"E:\pill-identification\database\pill_info.db"
mp3_folder = r"E:\pill-identification\mp3"

pill_table = "pill_info_table"



def connect_to_database():
    """
    Establishes a connection to the SQLite database.

    Returns:
        sqlite3.Connection: The database connection object.
    """
    conn = sqlite3.connect(pill_database)
    return conn

def get_pill_list():
    """
    Queries the database for information about a specific pill.

    Args:
        classification: The name of the pill (identified by the main script).

    Returns:
        list: A list containing medication names and dosages if found, otherwise an empty list.
    """
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT medication_name_dosage FROM pill_info_table")
    medication_names_dosages = [row[0] for row in cursor.fetchall()]
    # print('medication_names_dosage', medication_names_dosages)
    cursor.close()
    conn.close()
    return medication_names_dosages

def generate_mp3():
    conn = connect_to_database()
    cursor = conn.cursor()
    medication_names_dosages = get_pill_list()
    info_columns = ['medication_name', 'dosage', 'special_instructions', 'possible_side_effects']
    for medicine in medication_names_dosages:
        cursor.execute(f"SELECT {','.join(info_columns)} FROM pill_info_table WHERE medication_name_dosage = ?", (medicine,))
        pill_info = cursor.fetchone()
        if pill_info:
            # Construct speech message from pill information
            message = f"The pill is identified as {pill_info[0]} with a dosage of {pill_info[1]} milligrams. {pill_info[2]}. {pill_info[3]}"  # Replace with actual data access

            # Use gTTS to convert text to speech
            tts = gTTS(text=message, lang='en', tld='us', slow=False)
            
            # Save the speech as an audio file
            mp3_medicine = medicine.replace(' ', '_').replace('(', '').replace(')', '').lower()
            file_path = os.path.join(mp3_folder, f"{mp3_medicine}.mp3")
            tts.save(file_path)
            print("{} mp3 file created.".format(medicine))
    # Close the cursor and the connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    generate_mp3()