from concurrent import futures
import logging

import grpc

from grpc_hello.proto import helloworld_pb2
from grpc_hello.proto import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        import time
        time.sleep(2)
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)


class LogInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        print("请求开始")
        print(type(handler_call_details))
        rsp = continuation(handler_call_details)
        print("请求结束")
        return rsp


def serve():
    interceptor = LogInterceptor()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=(interceptor,))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()