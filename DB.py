import sqlite3
 
conn = sqlite3.connect("min_database.db")
cursor = conn.cursor()
 
cursor.execute('''CREATE TABLE IF NOT EXISTS personer (id INTEGER PRIMARY KEY, navn TEXT, alder INTEGER)''')
 
cursor.execute('''INSERT INTO personer (navn, alder) VALUES ("Ola Nordmann", 35)''')
 
conn.commit()
 
cursor.execute('''SELECT * FROM personer''')
personer = cursor.fetchall()
for person in personer:
    print(person)
 
conn.close()