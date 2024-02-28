import sqlite3
import pyttsx3

# Database connection information (replace with your details)
DB_NAME = "pill_data.db"
TABLE_NAME = "pills"

def connect_to_database():
  """
  Establishes a connection to the SQLite database.

  Returns:
      sqlite3.Connection: The database connection object.
  """
  conn = sqlite3.connect(DB_NAME)
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
  cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE name = ?", (classification,))
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
    message = f"The pill is identified as {pill_info[1]}. {pill_info[2]}"  # Replace with actual data access
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()
  else:
    speak("Pill information not found.")

# Example usage (uncomment if running this script directly)
# classification = "Aspirin"  # Replace with actual classification result
# speak_pill_info(classification)
