import sqlite3
from venv import create

conn = sqlite3.connect('E:\Dev\EmbeddedSystem\Server\SoilMoisture_db.sqlite')
cur = conn.cursor()

# createTable = '''CREATE TABLE soilmoisture (
#                  date TIMESTAMP,
#                  soil_moisture INTEGER)'''
# cur.execute(createTable)

# currentDateTime = datetime.datetime.now()
# x = 1024
# arr = [currentDateTime, x]

insertQuery = """INSERT INTO soilmoisture
                 VALUES (?, ?);"""

def insertData(arr):
    cur.execute(insertQuery, arr)
    conn.commit()

# cur.execute('SELECT * FROM soilmoisture')
# data = cur.fetchall()
# print(data)