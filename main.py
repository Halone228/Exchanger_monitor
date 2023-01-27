import sqlite3
import bestchange_api as api
import datetime

db = sqlite3.connect("main.db")
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS DATA(date DATETIME PRIMARY KEY, name_from INT, name_to INT, rate DOUBLE, exchangers_id INT)""")
db.commit()
api_ = api.BestChange()
while True:
    data = api_.rates().get()
    for i in data:
        cursor.execute(f"""INSERT INTO DATA(date, name_from, name_to, rate, exchangers_id) VALUES(?,?,?,?,?)""", 
        (datetime.datetime.now(),
        i.get('give_id'),
        i.get('get_id'),
        i.get('rate'),
        i.get('exchangers_id')))
        db.commit()
    api_.load()