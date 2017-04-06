__author__ = 'Anders'
import datetime
import time
import paho.mqtt.client as mqtt
import json
import clientfields


def on_connect(client, userdata, flags, rc):
    print(("connected with result code "+str(rc)))
    client.subscribe("/fk/rr/2")
def on_message(client, userdata, msg):
    data=json.loads(str(msg.payload)[2:-1])
    for i in data:
            print(i)
    """if data[-1]['type']=='bookinglist':
        data.pop()
        for i in data:
            #print(i['Name'])
            print(i)
    if data[-1]['type']=='list':
        data.pop()
        for i in data:
            #print(i['Name'])
            print(i)"""


client=mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)
client.loop_start()

while True:
    time.sleep(1)
    print("Skriv inn commando")
    inn=input()
    if inn=='liste':
        #data={'command': 'list'}
        verdi1=int(datetime.datetime(2017, 3, 31, 17, 00).timestamp())#debug
        verdi2=int(datetime.datetime(2017, 3, 31, 18, 00).timestamp())#debug
        data={'command': 'liste', 'building': 'Realfagsbygget', 'from' : verdi1 , 'to' : verdi2, 'clientname' : clientfields.name}#debug
        #data={'command': 'list', 'building': 'Realfagsbygget'}#debug
        print(data)#debug
        client.publish('/fk/rr', json.dumps(data))
        print("sendt")

    if inn=='bookings':
        data={'command': 'bookings', 'user': '1', 'clientname' : clientfields.name}#debug
        print(data)
        client.publish('/fk/rr', json.dumps(data))
        print("sendt")