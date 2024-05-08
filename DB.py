import sqlite3

def create_database():
    conn = sqlite3.connect("min_database.db")
    cursor = conn.cursor()

    # Opprett tabellen for personer
    cursor.execute('''CREATE TABLE IF NOT EXISTS personer (id INTEGER PRIMARY KEY, navn TEXT, alder INTEGER)''')

    # Opprett tabellen for notater
    cursor.execute('''CREATE TABLE IF NOT EXISTS notater (id INTEGER PRIMARY KEY, tittel TEXT, innhold TEXT)''')

    # Opprett koblingstabell for å relatere notater til personer
    cursor.execute('''CREATE TABLE IF NOT EXISTS person_notat (
                        person_id INTEGER,
                        notat_id INTEGER,
                        FOREIGN KEY (person_id) REFERENCES personer(id),
                        FOREIGN KEY (notat_id) REFERENCES notater(id)
                    )''')

    conn.commit()
    conn.close()

def legg_til_person(navn, alder):
    conn = sqlite3.connect("min_database.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO personer (navn, alder) VALUES (?, ?)''', (navn, alder))
    conn.commit()
    conn.close()

def legg_til_notat(tittel, innhold):
    conn = sqlite3.connect("min_database.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO notater (tittel, innhold) VALUES (?, ?)''', (tittel, innhold))
    conn.commit()
    conn.close()

def knytt_notat_til_person(person_id, notat_id):
    conn = sqlite3.connect("min_database.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO person_notat (person_id, notat_id) VALUES (?, ?)''', (person_id, notat_id))
    conn.commit()
    conn.close()

def vis_personer_og_notater():
    conn = sqlite3.connect("min_database.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM personer''')
    personer = cursor.fetchall()
    for person in personer:
        print("Person:", person)
        cursor.execute('''SELECT notater.* FROM notater
                          INNER JOIN person_notat ON notater.id = person_notat.notat_id
                          WHERE person_notat.person_id = ?''', (person[0],))
        notater = cursor.fetchall()
        for notat in notater:
            print("Notat:", notat)
        print()
    conn.close()

# Opprett databasen hvis den ikke allerede eksisterer
create_database()

# Legg til noen testdata
legg_til_person("Ola Nordmann", 35)
legg_til_person("Kari Nordmann", 30)
legg_til_notat("Handleliste", "Melk, brød, egg")
legg_til_notat("Møteplan", "Møte med klient kl. 10")

# Knytt notater til personer
knytt_notat_til_person(1, 1)  # Ola Nordmann har handlelisten
knytt_notat_til_person(2, 2)  # Kari Nordmann har møteplanen

# Vis personer og deres tilknyttede notater
vis_personer_og_notater()
        