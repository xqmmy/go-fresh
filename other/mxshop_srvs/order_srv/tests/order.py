import grpc

import consul
from order_srv.proto import order_pb2, order_pb2_grpc
from order_srv.settings import settings


class OrderTest:
    def __init__(self):
        #连接grpc服务器
        c = consul.Consul(settings.CONSUL_HOST, port=settings.CONSUL_PORT)
        services = c.agent.services()
        for key, value in services.items():
            if value["Service"] == settings.SERVICE_NAME:
                ip = value["Address"]
                port = value["Port"]
                break
        ip = "192.168.0.104"
        port = 41334
        if not ip:
            raise Exception("订单服务不可用")
        channel = grpc.insecure_channel(f"{ip}:{port}")
        self.order_stub = order_pb2_grpc.OrderStub(channel)

    def create_cart_item(self):
        rsp = self.order_stub.CreateCartItem(
            order_pb2.CartItemRequest(goodsId=422, userId=1, nums=3)
        )
        print(rsp)

    def create_order(self):
        rsp = self.order_stub.CreateOrder(
            order_pb2.OrderRequest(userId=1, address="北京市", mobile="18787878787",
                                   name="bobby", post="请尽快发货")
        )
        print(rsp)

    def order_list(self):
        rsp = self.order_stub.OrderList(order_pb2.OrderFilterRequest(userId=1))
        print(rsp)


if __name__ == "__main__":
    order = OrderTest()
    # order.create_cart_item()
    # order.create_order()
    order.order_list()