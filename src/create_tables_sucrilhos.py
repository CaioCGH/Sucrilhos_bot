import sqlite3
def create_tables():
    conn = sqlite3.connect('sucrilhos.db') 
    c = conn.cursor()

    c.execute('''CREATE TABLE commandment(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                text TEXT);''')
    print("CREATE TABLE commandment")
    c.execute('''CREATE TABLE event(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                username TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                description TEXT);''')
    print("CREATE TABLE event")        
    c.execute('''CREATE TABLE bot_suggestion(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username text,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                description TEXT);''')
    print("CREATE TABLE bot_suggestion")
    c.execute('''CREATE TABLE corona(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                text TEXT);''')
    print("CREATE TABLE corona")
                    
    conn.commit()
    conn.close()
