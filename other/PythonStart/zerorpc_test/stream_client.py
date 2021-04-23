import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

#1. 生态 - grpc
#2. 语言的支持 python nodejs go
#3. grpc
for item in c.streaming_range(10, 20, 2):
    print(item)