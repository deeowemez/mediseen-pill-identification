import sqlite3
import pandas as pd

# Load data file
df = pd.read_csv('pill_info.csv')

# Data clean up
df.columns = df.columns.str.strip()

# Create/connect to a SQLite database
connection = sqlite3.connect('pill_info.db')

# Load datafile to SQLite
# fail;replace;append
df.to_sql('pill_info', connection, if_exists='replace')

# Close connection
connection.close()