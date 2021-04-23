from concurrent import futures
import logging

import grpc

from grpc_hello.proto import helloworld_pb2
from grpc_hello.proto import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        # context.set_code(grpc.StatusCode.NOT_FOUND)
        # context.set_details("记录不存在")
        import time
        time.sleep(5)
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()