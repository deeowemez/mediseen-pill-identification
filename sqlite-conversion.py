# https://www.youtube.com/watch?v=UZIhVmkrAEs

import sqlite3
import pandas as pd

# Load data file
df = pd.read_csv('pill_info.csv')

# Data clean up
df.columns = df.columns.str.strip()

# Create/connect to a SQLite database
conn = sqlite3.connect('pill_info.db')

# Create the table with the primary key constraint
df.to_sql('pill_info_table', conn, if_exists='replace', index=False,
          dtype={'medicine id': 'INTEGER PRIMARY KEY'})

# Close connection
conn.close()
