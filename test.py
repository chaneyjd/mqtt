import mosquitto

########################

#You can now create a new mosquitto client instance. You must provide the name of the new client, which will be used to identify the client with the broker. The clean session parameter controls whether the client is persistent or not as described in the MQTT man page. You may also provide a Python object that will be passed to the callbacks described later on.

#client = mosquitto.Mosquitto(client_id, clean_session=True, obj=None)
client = mosquitto.Mosquitto("test-client")

#To connect to a broker, use the connect method which takes three parameters, although only the first is required. They are the hostname of the broker to connect to, the network port number to connect to (default 1883) and the "keepalive" time in seconds (defaults to 60, used as the interval between PING packets). If this method returns 0, it was successful.

#client.connect(hostname, port=1883, keepalive=60)
client.connect("127.0.0.1")

#In order to process incoming and outgoing network data, the loop method must be called frequently. The loop method optionally takes a single parameter, an integer indicating the maximum number of milliseconds to wait for network data before returning. Set to 0 to return immediately, or to -1 to use the default value of 1 second. If loop() returns 0, it was successful. Any other value means a failure and that the network connection has been closed.

#client.loop(timeout=-1)
client.loop()

#To disconnect from the broker, use the disconnect() function. To be sure of disconnecting from the broker cleanly, use the on_disconnect() callback.

client.disconnect()

########################


#To publish a message, use the publish method. The only mandatory argument is the topic, which indicates where the message will be published. Note that it is valid to send a payload of value None; this will send a zero length message which can be useful for simple notification purposes. For more details on the qos and retain arguments, please see the mqtt(7) man page. This function returns 0 on success. Note that success only means that the function call didn’t fail. To be certain that the message was published, use the on_publish() callback.

#client.publish(topic, payload=None, qos=0, retain=false)
client.publish("my/topic", "hello world", 1)


#To receive messages, you must first subscribe to a topic. Subscriptions may contain wildcards to receive messages from more than one topic at once. See the mqtt(7) man page for more details. This function only allows a single subscription per call at the moment. This function returns 0 on success. Note that success only means that the function call didn’t fail. To be certain that the subscription was successful, use the on_subscribe() callback.

#client.subscribe(topic, qos)
client.subscribe("my/topic", 0)

#If you no longer wish to receive messages from a subscription, you must unsubscribe from it. This function returns 0 on success. Note that success only means that the function call didn’t fail. To be certain that the subscription was successful, use the on_unsubscribe() callback.

#client.unsubscribe(topic)
client.unsubscribe("my/topic")

########################

#To receive notification on when commands have been successfully processed, you should define callbacks. This is important - the functions that send commands to a broker will return success/failure only to indicate that the input was valid and the command was added to the queue successfully. It does not mean they were processed successfully at the broker.

#All callbacks have two parameters, mosq and obj. The mosq parameter is the client instance that is calling the callback. The obj parameter is the same object that was passed when the client instance was created.

#This is called after the client has received a CONNACK message from the broker in response to calling connect(). The parameter rc is an integer giving the return code:

#0: Success
#1: Refused - unacceptable protocol version
#2: Refused - identifier rejected
#3: Refused - server unavailable
#4: Refused - bad user name or password (MQTT v3.1 broker only)
#5: Refused - not authorised (MQTT v3.1 broker only)

#Define and assign the callback to a client as follows:

def on_connect(mosq, obj, rc):
  if rc == 0:
    print("Connected successfully.")

client.on_connect = on_connect

#Class member functions may also be used:

#def on_connect(self, mosq, obj, rc):
#  if rc == 0:
#    print("Connected successfully.")
#
#self.client.on_connect = self.on_connect

#This is called when the client disconnects from the broker. The rc parameter indicates the status of the disconnection. When 0 the disconnection was the result of disconnect() being called, when 1 the disconnection was unexpected.

def on_disconnect(mosq, obj, rc):
  print("Disconnected successfully.")

client.on_disconnect = on_disconnect

#This is called when a message from the client has been successfully sent to the broker. The mid parameter gives the message id of the successfully published message.

def on_publish(mosq, obj, mid):
  print("Message "+str(mid)+" published."

client.on_publish = on_publish

#This is called when a message has been received by the client. The msg parameter is a MosquittoMessage object that contains all of the message information:

#msg.mid - the integer message id
#msg.topic - the topic to which the message was published
#msg.payloadlen - the length in bytes of the payload (may be zero)
#msg.payload - the message payload
#msg.qos - the message quality of service level, 0, 1 or 2
#msg.retain - set to true if the message was published as a "last known good" value

def on_message(mosq, obj, msg):
  print("Message received on topic "+msg.topic+" with QoS "+str(msg.qos)+" and payload "+msg.payload)

client.on_message = on_message

#This is called when the broker acknowledges a subscription request. The qos_list parameter is a list of integers detailing the granted QoS levels for the requested subscriptions.

def on_subscribe(mosq, obj, mid, qos_list):
  print("Subscribe with mid "+str(mid)+" received.")

client.on_subscribe = on_subscribe

#This is called when the broker acknowledges an unsubscription request.

def on_unsubscribe(mosq, obj, mid):
  print("Unsubscribe with mid "+str(mid)+" received.")

client.on_unsubscribe = on_unsubscribe
