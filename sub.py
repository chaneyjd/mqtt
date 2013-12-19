import mosquitto
import time

########################

def on_connect(mosq, obj, rc):
  if rc == 0:
    print("Connected successfully.")

def on_disconnect(mosq, obj, rc):
  print("Disconnected successfully.")

def on_subscribe(mosq, obj, mid, qos_list):
  print("Subscribe with mid "+str(mid)+" received.")

def on_unsubscribe(mosq, obj, mid):
  print("Unsubscribe with mid "+str(mid)+" received.")

def on_message(mosq, obj, msg):
    print("Message received on topic "+msg.topic+" with QoS "+str(msg.qos)+" and payload "+str(msg.payload))

client = mosquitto.Mosquitto("test-sub")

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscribe
client.on_message = on_message

client.connect("127.0.0.1")
client.subscribe("my/topic", 2)

#while (1):
#  time.sleep(3);
client.loop_forever()

client.unsubscribe("my/topic")
client.disconnect()

exit()
