from flask import Flask, render_template, request

app = Flask(__name__)
import sqlite3

from flask import Flask
from flask_mqtt import Mqtt

app.config['MQTT_BROKER_URL'] = '192.168.1.178'  #homeip
app.config['MQTT_BROKER_PORT'] = 1883  # default port for non-tls connection
# app.config['MQTT_USERNAME'] = ''  # set the username here if you need authentication for the broker
# app.config['MQTT_PASSWORD'] = ''  # set the password here if the broker demands authentication
# app.config['MQTT_KEEPALIVE'] = 5  # set the time interval for sending a ping to the broker to 5 seconds
app.config['MQTT_TLS_ENABLED'] = False  # set TLS to disabled for testing purposes

mqtt = Mqtt()


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

