import sqlite3 as lite
import sys
con = lite.connect('sensorData.db')
cur = con.cursor() 

    #cur.execute("DROP TABLE IF EXISTS DHT_data")
    #cur.execute("CREATE TABLE DHT_data(timestamp DATETIME, temp NUMERIC, hum NUMERIC)")

#     cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 20.5, 30)")
#     cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 25.8, 40)")
#     cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 30.3, 50)")

def insertdata(temp, hum):
          cur.execute("INSERT INTO DHT_data values(datetime('now'),(?), (?))", (temp, hum))
          con.commit()


def printdb():
          for row in cur.execute("SELECT * FROM DHT_data"):
                    print (row)   

#insertdata(con,1,1)
#printdb()