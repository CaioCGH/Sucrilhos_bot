import sqlite3

conn = sqlite3.connect('sucrilhos.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

c.execute('''CREATE TABLE commandment(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT,
             timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
             text TEXT);''')
          
c.execute('''CREATE TABLE event(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT UNIQUE,
             username TEXT,
             timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
             description TEXT);''')
        
c.execute('''CREATE TABLE bot_suggestion(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             username text,
             timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
             description TEXT);''')
                 
conn.commit()
conn.close()

# Note that the syntax to create new tables should only be used once in the code (unless you dropped the table/s at the end of the code). 
# The [generated_id] column is used to set an auto-increment ID for each record
# When creating a new table, you can add both the field names as well as the field formats (e.g., Text)