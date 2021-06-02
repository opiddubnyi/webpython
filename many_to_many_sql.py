import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS User')
cur.execute('DROP TABLE IF EXISTS Member')
cur.execute('DROP TABLE IF EXISTS Course')

cur.executescript("""
CREATE TABLE User(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT UNIQUE
                );

CREATE TABLE Course(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                title TEXT UNIQUE
                );
                
CREATE TABLE Member(
                user_id INTEGER, 
                course_id INTEGER,
                role       INTEGER,
                PRIMARY KEY (user_id, course_id)
                );

""")

str_data = open('roster_data_sample.json').read()
json_data = json.loads(str_data)

for line in json_data:
    name = line[0]
    title = line[1]
    role = line[2]


    print(name, title, role)

    cur.execute("INSERT OR IGNORE INTO User(name) VALUES (?) ", (name,))
    cur.execute("SELECT id FROM User WHERE name = ?", (name, ))
    user_id = cur.fetchone()[0]

    cur.execute("""INSERT OR IGNORE INTO Course(title) VALUES (?)""",
                (title,))
    cur.execute("""SELECT id FROM Course WHERE title = ?""", (title, ))
    course_id = cur.fetchone()[0]

    cur.execute("""INSERT OR REPLACE INTO Member
                (user_id, course_id, role) VALUES(?, ?, ?)""", (user_id,
                                                                course_id, role))

    conn.commit()

