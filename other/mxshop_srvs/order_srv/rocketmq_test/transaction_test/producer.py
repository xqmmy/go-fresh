from rocketmq.client import TransactionMQProducer, Message, TransactionStatus
import time

topic = "TopicTest"


def create_message(id):
    msg = Message(topic)
    msg.set_keys("imooc")
    msg.set_tags('bobby')
    msg.set_property("name", "micro services")
    msg.set_property("id", id)
    msg.set_body("微服务开发")
    return msg


def check_callback(msg):
    #消息回查， 做本地逻辑
    #TransactionStatus.COMMIT, TransactionStatus.ROLLBACK, TransactionStatus.UNKNOWN
    print(f"事务消息回查：{msg.body.decode('utf-8')}")
    return TransactionStatus.COMMIT

data_dict = {

}

import grpc
def local_execute(msg, user_args):
    # TransactionStatus.COMMIT, TransactionStatus.ROLLBACK, TransactionStatus.UNKNOWN
    #这里应该执行业务逻辑，订单表插入
    id = msg.get_property('id').decode("utf-8")
    print(f"本地执行：{id}")
    data_dict[id] = {
        "code": grpc.StatusCode.OK,
        "detail": "失败"
    }
    print(data_dict)
    return TransactionStatus.ROLLBACK


def send_transaction_message(count):
    #发送事务消息
    producer = TransactionMQProducer("test", check_callback)
    producer.set_name_server_address("192.168.0.104:9876")
    import uuid
    id = str(uuid.uuid4())
    #首先要启动producer
    producer.start()
    for n in range(count):
        msg = create_message(id)

        ret = producer.send_message_in_transaction(msg, local_execute, None)
        print(f"发送状态:{ret.status}, 消息id:{ret.msg_id}")
    print("消息发送完成")
    while True:
        if id in data_dict:
            print(data_dict[id])
            producer.shutdown()
            break
        time.sleep(0.1)


if __name__ == "__main__":
    #发送事务消息
    send_transaction_message(1)