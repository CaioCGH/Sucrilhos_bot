import sqlite3

conn = sqlite3.connect('sucrilhos.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

c.execute('''DROP TABLE IF EXISTS commandment''')
c.execute('''DROP TABLE IF EXISTS event''')
c.execute('''DROP TABLE IF EXISTS bot_suggestion''')
          
conn.commit()
conn.close()
