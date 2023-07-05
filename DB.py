import sqlite3

db = sqlite3.connect('mydb.db')
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Posts(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, 
                image TEXT)""")
db.commit()
db.close()

