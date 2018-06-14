'''
APPLICATION SERVER WHICH LISTENS MESSAGES FROM MY ARDUINO DEVICE AND TO SEND SMS TO THE VERIFIED USER
Created -  Code Demo
'''

# Phase 1 - MQTT INITIALISATION

# 1.1 Import mqtt package
import paho.mqtt.client as mqttPackage

import ast

# Phase -2 Import twilio package
from twilio.rest import Client


# 1.2 start mqtt connection

hostname  = '34.226.134.195'
port      = 1883
timealive = 60

SUB_TOPIC = "smart-demo"

sendFlag = False


def on_connect(client, userdata, flags, rc ):
	print ("connected")
	(result,mid) = mqttClient.subscribe(SUB_TOPIC)

def on_message(client, userdata, msg):
	# print msg.keys()
	# message = ast.literal_eval(msg.payload)
	
	twilionumber = "+19042991062" # Your Twilio phone Number you will get it while registration
	receivernumber = "+917658922979" #Your verified phone number
	
	distance = int(msg.payload)

	if distance <=10 and sendFlag == False:
		# send message to scavenger
		messageBody = " bin in ACET seminar hall is filled.please come and collect the trash"
	
		twilioClient.messages.create(body=messageBody,to=receivernumber,from_=twilionumber)

		sendFlag = True

	if distance >= 10:
		sendFlag = False

				




		


	
	
# 2.1 
account_sid = "AC7d8e59f70af33487821f2cb19a0f55b1" # Enter your account sid 
auth_token  = "570a54412bf7ceed3b22a5fa4d05d096"   # Enter your auth token

twilioClient = Client(account_sid, auth_token)

			




# 1.3 Initializing mqtt client
mqttClient = mqttPackage.Client()

mqttClient.connect(hostname,port,timealive)

mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.loop_start()
mqttClient.loop_forever()

 
