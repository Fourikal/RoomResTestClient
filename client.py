__author__ = 'Anders'
import datetime
import time
import paho.mqtt.client as mqtt
import json



def on_connect(client, userdata, flags, rc):
    print(("connected with result code "+str(rc)))
    client.subscribe("/hopp/ned/2")
def on_message(client, userdata, msg):
    data=json.loads(str(msg.payload)[2:-1])
    for i in data:
        #print(i['Name'], i['Id'])
        print(i)


client=mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)
client.loop_start()

while True:
    time.sleep(1)
    print("Skriv inn commando")
    inn=input()
    if inn=='list':
        #data={'command': 'list'}
        #verdi1=int(datetime.datetime(2017, 3, 31, 17, 00).timestamp())#debug
        #verdi2=int(datetime.datetime(2017, 3, 31, 18, 00).timestamp())#debug
        verdi1=1000#debug
        verdi2=1300#debug
        data={'command': 'list', 'building': 'Realfagsbygget', 'from' : verdi1 , 'to' : verdi2}#debug
        #data={'command': 'list', 'building': 'Realfagsbygget'}#debug
        print(data)
        client.publish('/hopp/ned', json.dumps(data))
        print("sendt")