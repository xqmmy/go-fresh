import grpc

from grpc_hello.proto import helloworld_pb2, helloworld_pb2_grpc

#1. 这个问题能改吗？
#2. 其他语言有没有这个问题 其他语言 go语言 python 不服气
if __name__ == "__main__":
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        hello_request = helloworld_pb2.HelloRequest()
        hello_request.name = "bobby"
        #grpc已经处理了语言之间的错误处理的不同方式
        #1. 网络抖动
        #2. 网络断开 A->B 10s
        try:
            #context
            rsp: helloworld_pb2.HelloReply = stub.SayHello(hello_request, timeout=3)
        except grpc.RpcError as e:
            d = e.details()
            status_code = e.code()
            print(status_code.name)
            print(status_code.value)
            print(f"code：{status_code.name}, detail: {d}")
