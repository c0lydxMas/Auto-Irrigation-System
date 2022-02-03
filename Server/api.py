from fastapi import FastAPI
import sqlite3

DATABASE_URL = '''E:\Dev\EmbeddedSystem\Server\SoilMoisture_db.sqlite'''

app = FastAPI()

conn = None
try:
    conn = sqlite3.connect(DATABASE_URL, check_same_thread=False)
except sqlite3.Error as e:
    print(e)

def getLastestData():
    cur = conn.cursor()
    cur.execute("SELECT soil_moisture FROM soilmoisture ORDER BY date DESC LIMIT 1")

    rows = cur.fetchone()[0]
    return {'soil_moisture' : rows}

@app.get('/')
def home():
    return {"Data": "Test"}

@app.get('/data')
def getAll():
    return getLastestData()