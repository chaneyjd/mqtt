import mosquitto

########################

def on_publish(mosq, obj, mid):
  print("Message "+str(mid)+" published.")

def on_disconnect(mosq, obj, rc):
  print("Disconnected successfully.")

def on_connect(mosq, obj, rc):
  if rc == 0:
    print("Connected successfully.")

client = mosquitto.Mosquitto("test-pub")

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

client.connect("127.0.0.1")

for x in range(0, 30):
#while (1):
  client.loop()
  client.publish("my/topic", "hello world " + str(x), 0)
#  z = getch.getch()
#  if ord(z) == 27:
#    sys.exit()

client.disconnect()

