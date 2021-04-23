from rocketmq.client import PushConsumer, ConsumeStatus
import time

topic = "order_reback"


def callback(msg):
    print(msg.id, msg.body.decode("utf-8"), msg.get_property("name"))
    return ConsumeStatus.CONSUME_SUCCESS


def start_consume_message():
    consumer = PushConsumer("python_consumer")
    consumer.set_name_server_address("192.168.0.104:9876")
    consumer.subscribe(topic, callback)
    print("开始消费消息")
    consumer.start()

    while True:
        time.sleep(3600)

if __name__ == "__main__":
    start_consume_message()