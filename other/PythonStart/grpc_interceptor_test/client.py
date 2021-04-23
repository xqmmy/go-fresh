import grpc

from grpc_hello.proto import helloworld_pb2, helloworld_pb2_grpc

#1. 这个问题能改吗？
#2. 其他语言有没有这个问题 其他语言 go语言 python 不服气
class DefaultInterceptor(grpc.UnaryUnaryClientInterceptor):
    def intercept_unary_unary(self, continuation, client_call_details, request):
        from datetime import datetime
        start = datetime.now()
        rsp = continuation(client_call_details, request)
        print((datetime.now()-start).microseconds/1000)
        return rsp


if __name__ == "__main__":
    from grpc_interceptor.retry import RetryInterceptor
    default_interceptor = DefaultInterceptor()
    retry_codes = [grpc.StatusCode.UNKNOWN, grpc.StatusCode.UNAVAILABLE, grpc.StatusCode.DEADLINE_EXCEEDED]
    retry_interceptor = RetryInterceptor(retry_codes=retry_codes)
    with grpc.insecure_channel("localhost:50051") as channel:
        intecept_channel = grpc.intercept_channel(channel, default_interceptor, retry_interceptor)
        stub = helloworld_pb2_grpc.GreeterStub(intecept_channel)
        hello_request = helloworld_pb2.HelloRequest()
        hello_request.name = "bobby"
        rsp: helloworld_pb2.HelloReply = stub.SayHello(hello_request, timeout=1)

        print(rsp.message)