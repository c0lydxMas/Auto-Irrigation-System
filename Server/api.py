from fastapi import FastAPI
import sqlite3

# Absolute path to sqlite database
DATABASE_URL = '''E:\Dev\EmbeddedSystem\Server\SoilMoisture_db.sqlite'''

# Create new FastAPI instance
app = FastAPI()

# Create connection to sqlite database 
conn = None
try:
    conn = sqlite3.connect(DATABASE_URL, check_same_thread = False)
except sqlite3.Error as e:
    print(e)

# This function return one and only one latest value from database
# No need to take care of empty case
def getLastestData():
    cur = conn.cursor()
    cur.execute("SELECT soil_moisture FROM soilmoisture ORDER BY date DESC LIMIT 1")

    rows = cur.fetchone()[0]
    return {'soil_moisture' : rows}

# Handle GET request from client
@app.get('/')
def home():
    return {"Data": "Home"}

# Main Operation
@app.get('/data')
def getAll():
    return getLastestData()