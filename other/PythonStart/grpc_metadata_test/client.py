import grpc

from grpc_metadata_test.proto import helloworld_pb2, helloworld_pb2_grpc

#1. 这个问题能改吗？
#2. 其他语言有没有这个问题 其他语言 go语言 python 不服气
if __name__ == "__main__":
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        hello_request = helloworld_pb2.HelloRequest()
        hello_request.name = "bobby"
        response, call = stub.SayHello.with_call(
            hello_request,
            metadata=(
                ('name', 'bobby'),
                ('password', 'imooc')
            ))

        print(response.message)