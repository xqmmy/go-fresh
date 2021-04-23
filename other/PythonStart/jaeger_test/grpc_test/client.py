import grpc
import logging
import time
from random import randint
from jaeger_client import Config
from grpc_opentracing import open_tracing_client_interceptor
from grpc_opentracing.grpcext import intercept_channel

from grpc_hello.proto import helloworld_pb2, helloworld_pb2_grpc

#1. 这个问题能改吗？
#2. 其他语言有没有这个问题 其他语言 go语言 python 不服气
if __name__ == "__main__":
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
        service_name='mxshop-grpc',
        validate=True,
    )
    tracer = config.initialize_tracer()
    tracing_interceptor = open_tracing_client_interceptor(tracer)

    with grpc.insecure_channel("localhost:50051") as channel:
        tracing_channel = intercept_channel(channel, tracing_interceptor)

        stub = helloworld_pb2_grpc.GreeterStub(tracing_channel)
        hello_request = helloworld_pb2.HelloRequest()
        hello_request.name = "bobby"
        rsp: helloworld_pb2.HelloReply = stub.SayHello(hello_request)

        print(rsp.message)

    time.sleep(2)  # yield to IOLoop to flush the spans - https://github.com/jaegertracing/jaeger-client-python/issues/50
    tracer.close()