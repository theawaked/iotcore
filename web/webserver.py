from flask import Flask, render_template, request
app = Flask(__name__)
import sqlite3

# import paho.mqtt.client as paho
# broker="192.168.1.184"
# port=1883

# client1= paho.Client("control1")   #create client object
# client1.on_publish = on_message    #assign function to callback
# client1.connect(broker,port)       #establish connection
# ret= client1.publish("house/bulb1","on") 

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
   app.run(host='0.0.0.0', port=5000, debug=True)

