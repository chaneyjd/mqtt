import mosquitto
import time
import msvcrt as m

def wait():
  m.getch()

def on_publish(mosq, obj, mid):
  print("Message "+str(mid)+" published.")

def on_disconnect(mosq, obj, rc):
  print("Disconnected successfully.")

def on_connect(mosq, obj, rc):
  if rc == 0:
    print("Connected successfully.")

x=1
client = mosquitto.Mosquitto("test-pub")

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

client.connect("127.0.0.1")
wait()
#input("1")

for x in range(0, 5):
  client.publish("my/topic", "hello world " + str(x), 2)

client.disconnect()
client.loop(500)

time.sleep(2)
