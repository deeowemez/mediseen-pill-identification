import sqlite3
import pyttsx3

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

def speak_pill_info(classification):
  """
  Retrieves information from the database and speaks it using text-to-speech.

  Args:
      classification: The name of the pill (identified by the main script).
  """
  pill_info = get_pill_info(classification)
  if pill_info:
    # Construct speech message from pill information
    message = f"The pill is identified as {pill_info[0]} with a dosage of {pill_info[1]} milligrams. {pill_info[2]}. {pill_info[3]}"  # Replace with actual data access
    # Initialize the espeak TTS engine
    engine = pyttsx3.init()
    # Set the voice (espeak may have limited voice options)
    engine.setProperty('voice', 'default')  # Example voice, replace with available options on your system
    # Set the speed (speed is a floating-point number where 1.0 is the default)
    engine.setProperty('rate', 100)  # Adjust the speed as needed
    engine.setProperty('pitch', 50)  # Adjust the pitch
    engine.say(message)
    engine.runAndWait()
  else:
    speak("Pill information not found.")

# classification = "Aspirin"  # Replace with actual classification result
speak_pill_info('Sucranorm Metformin HCl 850mg (Unpacked)')
