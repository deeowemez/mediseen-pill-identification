import sqlite3
import os


# Database connection information
pill_database = "/home/pi/capstone/pill-identification/database/pill_info.db"
# pill_database = "E:\\pill-identification\\database\\pill_info.db"
pill_table = "pill_info_table"


def connect_to_database():
    """
    Establishes a connection to the SQLite database.

    Returns:
        sqlite3.Connection: The database connection object.
    """
    conn = sqlite3.connect(pill_database)
    return conn

def get_pill_info_gui(classification):
    '''
        Retrieves pill information from the database based on the provided classification
    '''
    conn = connect_to_database()
    cursor = conn.cursor()
    info_columns = ['medication_name', 'dosage', 'special_instructions_gui', 'possible_side_effects_gui', 'medication_name_dosage']
    cursor.execute(f"SELECT {','.join(info_columns)} FROM pill_info_table WHERE medication_name_dosage = ?", (classification,))
    pill_info = cursor.fetchone()
    cursor.close()
    conn.close()
    return pill_info

if __name__ == "__main__":
    get_pill_info_gui("Sucranorm Metformin HCl 850mg (Packed)")