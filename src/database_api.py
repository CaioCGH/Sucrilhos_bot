#!/usr/bin/python

import sqlite3
import datetime
from datetime import datetime

def insert_commandment(username, text):
    conn = sqlite3.connect('sucrilhos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM commandment WHERE username = ?", (username,))
    row = cursor.fetchone()
    if row == None:    
        conn.execute("INSERT INTO commandment (username, text) VALUES (?, ?)", (username, text));
        print("new entry")
    else:
        conn.execute("UPDATE commandment set text = ? WHERE id = ?", (text, row[0]));
        print("update")
    conn.commit()
    cursor.close()
    conn.close()
        
def find_all_commandments():
    conn = sqlite3.connect('sucrilhos.db')
    cursor = conn.execute("SELECT * FROM commandment")
    rows = cursor.fetchall()
    conn.close()
    return rows

def find_commandment(id):
    conn = sqlite3.connect('sucrilhos.db')
    cursor = conn.execute("SELECT * FROM commandment WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()
    return row


def create_event(username, event_name, event_description):
    conn = sqlite3.connect('sucrilhos.db')
    conn.execute("INSERT INTO event (username, name, description) VALUES (?, ?, ?)", (username, event_name, event_description));
    conn.commit()
    conn.close()
    
def event_exists(event_name):
    conn = sqlite3.connect('sucrilhos.db')
    cursor = conn.execute("SELECT id FROM event WHERE name = ?", (event_name,))
    row = cursor.fetchone()
    conn.close()
    return row != None

def update_event_description(username, event_name, description):
    conn = sqlite3.connect('sucrilhos.db')
    conn.execute("UPDATE event set description = ? WHERE name = ?", (description, event_name));
    conn.commit()
    conn.close()
    
def delete_event(event_name):
    conn = sqlite3.connect('sucrilhos.db')
    conn.execute("DELETE FROM event WHERE name = ?", (event_name,))
    conn.commit()
    conn.close()
    
def find_all_events(row_count):
    conn = sqlite3.connect('sucrilhos.db')
    cursor = conn.execute("SELECT name FROM event ORDER BY timestamp DESC LIMIT ?", (row_count,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def find_event_by_name(event_name):
    conn = sqlite3.connect('sucrilhos.db')
    cursor = conn.execute("SELECT name, description FROM event WHERE name = ?", (event_name,))
    row = cursor.fetchone()
    conn.close()
    return row

def last_event():
    conn = sqlite3.connect('sucrilhos.db')
    cursor = conn.execute("SELECT name, description FROM event ORDER BY timestamp DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    return row

def create_suggestion(username, suggestion_description):
    conn = sqlite3.connect('sucrilhos.db')
    conn.execute("INSERT INTO bot_suggestion (username, description) VALUES (?, ?)", (username, suggestion_description));
    conn.commit()
    conn.close()
    
def insert_corona(username, text):
    conn = sqlite3.connect('sucrilhos.db')
    cursor = conn.cursor()
    conn.execute("INSERT INTO corona (username, text) VALUES (?, ?)", (username, text))
    print("new entry")
    conn.commit()
    cursor.close()
    conn.close()
        
def find_all_corona():
    conn = sqlite3.connect('sucrilhos.db')
    cursor = conn.execute("SELECT * FROM corona")
    rows = cursor.fetchall()
    conn.close()
    print(str(rows))
    return rows
