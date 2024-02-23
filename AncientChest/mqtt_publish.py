import paho.mqtt.client as mqtt
import json
import datetime
import random
import string


class MQTTCfg:
    def __init__(self, server=None, port=None, alive=10, username=None, password=None, client_id=None, qos=0):
        self.server = server
        self.port = port
        self.alive = alive
        self.username = username
        self.password = password
        self.client_id = client_id
        self.qos = qos


class MQTTPublisher(object):
    """MQTT Publisher object

    Description:
        Init a mqtt publisher that can help handle publish messages/payloads with specific topics by mqtt.

    Examples:
        >>> cfg = MQTTCfg(server="127.0.0.1", port=3369, client_id="publish_tester")
        >>> mqtt_publisher = MQTTPublisher(cfg)
        >>> mqtt_publisher.publish("/topic/test", "hello world!")

    """

    __mqtt_conn = None

    def __init__(self, cfg: MQTTCfg = None):
        if cfg is None:
            raise TypeError("There is not config for setting MQTT. Please Passing Config!")

        # TODO extract feature if user need publish by using different client/ random client
        if cfg.client_id is None:
            self.__client_id + datetime.datetime.now().strftime('%m%d') + \
                str(''.join(random.choice(string.ascii_lowercase) for i in range(4)))

        self.__server = cfg.server
        self.__port = cfg.port
        self.__alive = cfg.alive
        self.__username = cfg.username
        self.__password = cfg.password
        self.__client_id = cfg.client_id
        self.__qos = cfg.qos

    def _get_conn(self):
        if self.__mqtt_conn is None:
            mqtt_client = mqtt.Client(client_id=self.__client_id, protocol=mqtt.MQTTv311, transport="tcp")
            mqtt_client.username_pw_set(username=self.__username, password=self.__password)
            mqtt_client.connect(self.__server,
                                self.__port,
                                self.__alive)

            mqtt_client.loop_start()
            self.__mqtt_conn = mqtt_client
            # also put on log record: logger.info("Create MQTT connection successfully!")

        return self.__mqtt_conn

    def publish(self, topic: str, payload) -> None:
        """Publish message to IOT device.
        Args:
            topic (str): publish topic
            payload:
        Returns:
            None
        Notes:
            be careful when sent dictionary type structure to device,
            space would cause device can not understand the message / command.
        """
        try:
            self._get_conn().publish(topic,
                                     json.dumps(payload, separators=(',', ':'), ensure_ascii=False),
                                     qos=self.__qos)

        except Exception as e:
            # It can also put log record: logger.exception(f"MQTT Publish ERROR message: {str(e)}")
            print(f"MQTT Publish ERROR message: {str(e)}")
            raise e
