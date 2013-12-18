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
print (client.loop());

#To disconnect from the broker, use the disconnect() function. To be sure of disconnecting from the broker cleanly, use the on_disconnect() callback.

client.disconnect()

########################
