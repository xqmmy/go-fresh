from rocketmq.client import Producer, Message

topic = "TopicTest"

#延迟消息
def create_message():
    msg = Message(topic)
    msg.set_keys("imooc")
    msg.set_tags('bobby')
    msg.set_delay_time_level(2) #1s 5s 10s 30s 1m 2m 3m 4m 5m 6m 7m 8m 9m 10m 20m 30m 1h 2h
    msg.set_property("name", "micro services")
    msg.set_body("微服务开发")
    #1. 如何解决远程解释器出问题
    #2. 将缺失的依赖库装好
    #3. 关闭防火墙， 重启docker和rocketmq
    return msg


def send_message_sync(count):
    producer = Producer("test")
    producer.set_name_server_address("192.168.0.104:9876")

    #首先要启动producer
    producer.start()
    for n in range(count):
        msg = create_message()
        ret = producer.send_sync(msg)
        print(f"发送状态:{ret.status}, 消息id:{ret.msg_id}")
    print("消息发送完成")
    producer.shutdown()


if __name__ == "__main__":
    #发送普通消息
    send_message_sync(5)