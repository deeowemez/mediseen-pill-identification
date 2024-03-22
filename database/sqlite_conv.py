# https://www.youtube.com/watch?v=UZIhVmkrAEs

import sqlite3
import pandas as pd

# Load data file
df = pd.read_csv('/home/pi/capstone/pill-identification/database/pill_info.csv')

# Data clean up
df.columns = df.columns.str.strip()

# Create/connect to a SQLite database
conn = sqlite3.connect('/home/pi/capstone/pill-identification/database/pill_info.db')

# Create a cursor object
cursor = conn.cursor()

# Drop the existing table (if it exists)
cursor.execute("DROP TABLE IF EXISTS pill_info_table")

# Define the CREATE TABLE statement with data types and primary key
create_table_query = """
CREATE TABLE pill_info_table (
  medicine_id INTEGER PRIMARY KEY,
  medication_name TEXT,
  dosage INTEGER,
  special_instructions TEXT,
  possible_side_effects TEXT,
)
"""

# Create the table with the primary key constraint
df.to_sql('pill_info_table', conn, if_exists='replace', index=False,
          dtype={'medicine_id': 'INTEGER PRIMARY KEY'})

# Close connection
conn.close()
