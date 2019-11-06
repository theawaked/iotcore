from flask import Flask, render_template, request
app = Flask(__name__)
import sqlite3

#import paho.mqtt.client as mqtt

# Retrieve data from database
def getData():
	conn=sqlite3.connect('../sensorData.db')
	curs=conn.cursor()
	for row in curs.execute("SELECT * FROM DHT_data ORDER BY rowid DESC LIMIT 1"):
		time = str(row[0])
		temp = row[1]
		hum = row[2]
	conn.close()
	return time, temp, hum
# main route 
@app.route("/")
def index():	
	time, temp, hum = getData()
	templateData = {
		'time': time,
		'temp': temp,
		'hum': hum
	}
	return render_template('index.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)

#callback voor mqtt
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)