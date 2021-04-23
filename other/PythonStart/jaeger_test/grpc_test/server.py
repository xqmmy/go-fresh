from concurrent import futures
import logging
import time
from random import randint

import grpc
from grpc_opentracing import open_tracing_server_interceptor
from jaeger_client import Config
from grpc_opentracing.grpcext import intercept_server

from grpc_hello.proto import helloworld_pb2
from grpc_hello.proto import helloworld_pb2_grpc

log_level = logging.DEBUG
logging.getLogger('').handlers = []
logging.basicConfig(format='%(asctime)s %(message)s', level=log_level)

config = Config(
    config={  # usually read from some yaml config
        'sampler': {
            'type': 'const',  # 全部
            'param': 1,  # 1 开启全部采样 0 表示关闭全部采样
        },
        'local_agent': {
            'reporting_host': '192.168.0.104',
            'reporting_port': '6831',
        },
        'logging': True,
    },
    service_name='helloworld-srv',
    validate=True,
)
tracer = config.initialize_tracer()


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        #如何在这里找到父的span
        with tracer.start_span('execute', child_of=context.get_active_span()) as execute_span:
            time.sleep(randint(1, 9) * 0.1)
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tracing_interceptor = open_tracing_server_interceptor(tracer)
    server = intercept_server(server, tracing_interceptor)

    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    tracer.close()


if __name__ == '__main__':
    logging.basicConfig()
    serve()