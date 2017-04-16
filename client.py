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

a=False #bypassing the loop
while a==True:
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
        data={'command': 'bookings', 'user': 1, 'clientname' : clientfields.name}#debug
        print(data)
        client.publish('/fk/rr', json.dumps(data))
        print("sendt")
    if inn=='ledig':
        data={'command': 'cardask', 'user': 1, 'roomId': 1, 'clientname' : clientfields.name}#debug
        print(data)
        client.publish('/fk/rr', json.dumps(data))
        print("sendt")
b=2
def allTests():
    time.sleep(b)
    print("Start tests")
    print()
    print()
    verdi1=int(datetime.datetime(2017, 3, 31, 17, 00).timestamp())#debug
    verdi2=int(datetime.datetime(2017, 3, 31, 18, 00).timestamp())#debug
    data={'command': 'liste', 'building': 'Realfagsbygget', 'from' : verdi1 , 'to' : verdi2, 'clientname' : clientfields.name}#debug
    print("sent to server:")
    print(data)#debug
    print("Response:")
    client.publish('/fk/rr', json.dumps(data))
    #print("sendt. Sleeping")
    time.sleep(b)
    print()
    #ny test
    data={'command': 'liste', 'clientname' : clientfields.name}#debug
    print("sent to server:")
    print(data)#debug
    print("Response:")
    client.publish('/fk/rr', json.dumps(data))
    time.sleep(b)
    print()
    data={'command': 'bookings', 'user': 1, 'clientname': clientfields.name}#debug
    print("sent to server:")
    print(data)#debug
    print("Response:")
    client.publish('/fk/rr', json.dumps(data))
    #print("sendt. Sleeping")
    time.sleep(b)
    print()
    data={'command': 'cardCancelRest', 'user': 1, 'bookingId': 1, 'clientname' : clientfields.name}#debug
    print("sent to server:")
    print(data)#debug
    print("Response:")
    client.publish('/fk/rr', json.dumps(data))
    time.sleep(b)
    print()
    data={'command': 'cardask', 'user': 1, 'roomId': 1, 'clientname' : clientfields.name, 'RFID': 'abab'}#debug
    print("sent to server:")
    print(data)#debug
    print("Response:")
    client.publish('/fk/rr', json.dumps(data))
    time.sleep(b)
    print()
    data = {'command': 'makeBooking', 'user': 1, 'roomId': 1, 'clientname': clientfields.name, 'from': 200, 'to': 400}  # debug
    print("sent to server:")
    print(data)  # debug
    print("Response:")
    client.publish('/fk/rr', json.dumps(data))
    time.sleep(b)
    print()
    data = {'command': 'deleteBooking', 'user': 1, 'bookingId': 7, 'clientname': clientfields.name}  # debug
    print("sent to server:")
    print(data)  # debug
    print("Response:")
    client.publish('/fk/rr', json.dumps(data))
    time.sleep(b)
    print()
    data = {'command': 'RFIDisUser', 'clientname': clientfields.name, 'RFID': 'abab'}  # debug
    print("sent to server:")
    print(data)  # debug
    print("Response:")
    client.publish('/fk/rr', json.dumps(data))
    time.sleep(3)
    print("test over")
allTests()