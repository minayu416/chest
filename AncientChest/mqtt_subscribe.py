import paho.mqtt.client as mqtt
import time

from AncientChest.conv.bytes import dump_hex


class MQTTSubscriber(object):
    """MQTT Subscriber, open a subscribe connection and listening to receive data.

    Notes:
        please customize on_connect, on_message by ownself, you can find them refered to down (MQTTFunctionSample).

    Examples:
        >>> mqtt_subscriber = MQTTSubscriber("subscriber", None, None, "127.0.0.1", 6638, True)
        >>> mqtt_subscriber.subscribe(on_connect, on_message) # please customize these function by ownself and reference
        >>> # is on the bottom.
        >>> mqtt_subscriber.connect()

    """

    def __init__(self, client_id, user, password, mqtt_server, mqtt_port, clean_session=None):
        self.client_id = client_id
        self.client = None
        self.user = user
        self.password = password
        self.mqtt_server = mqtt_server
        self.mqtt_port = mqtt_port
        # Config File: {0: True, 1: False}
        self.clean_session = clean_session

    def subscribe(self, on_connect, on_message):
        """Setting Mqtt Config and Connecting to MQTT.

        Params:
            Please customize your own mqtt function by yourself. You can refer them from MQTTFunctionSample class at
            the bottom.

            on_connect(function):
            on_message(function):

        """
        client_id = self.client_id  # If broker asks client ID.
        self.client = mqtt.Client(client_id=client_id, clean_session=self.clean_session)
        # If broker asks user/password.
        user = self.user
        password = self.password
        self.client.username_pw_set(user, password)

        self.client.on_connect = on_connect
        self.client.on_message = on_message

        self.connect()

    def connect(self):
        try:
            self.client.connect(self.mqtt_server, self.mqtt_port)
            # Using log to record.
            # logger.info("connect succeed")
            # logger.info("Looping...")
            print("connect succeed")
            print("Looping...")
            self.client.loop_forever()

        except KeyboardInterrupt:
            self.client.disconnect()
            print("MQTT disconnect")
            # logger.info("MQTT disconnect")

        except Exception as e:
            # logger.exception(f"MQTT connection problem: {str(e)}")
            print(f"MQTT connection problem: {str(e)}")
            time.sleep(3)
            self.connect()


class MQTTFunctionSample():
    """This is the Sample mqtt function for reference. Please customize your own mqtt function.

    Description:
        You can customize your mqtt function refer by this class or by yourself.
        Making own function then pass to MQTTSubscriber.

    Functions:
        on_connect(client, userdata, flags, rc)
        on_message(client, userdata, flags)
        on_disconnect(client, userdata, flags, rc)
        ... More. Please refer to package paho-mqtt

    """

    def __init__(self, topic, qos=0):
        self.topic = topic
        self.qos = qos

    def on_connect(self, client, userdata, flags, rc):
        # subscribe when connected.
        qos = self.qos
        topic = self.topic
        client.subscribe(topic, qos=qos)

    def on_message(self, client, userdata, msg):
        msg_topic = msg.topic
        try:
            msg_payload = msg.payload.decode('utf-8')
        except UnicodeDecodeError:
            msg_payload = f'binary:{dump_hex(msg.payload)}'

        # Using log to record.
        # logger.info(f"Received topic: {msg_topic}")
        # logger.info(f"Received Msg: {msg_payload}")
        print(f"Received topic: {msg_topic}")
        print(f"Received Msg: {msg_payload}")
