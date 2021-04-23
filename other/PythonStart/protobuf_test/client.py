from protobuf_test.proto import hello_pb2

#生成的pb文件不要去改
request = hello_pb2.HelloRequest()
request.name = "bobby"
res_str = request.SerializeToString()
print(len(res_str))
res_json = {
    "name":"bobby"
}
import json
print(len(json.dumps(res_json)))
#如何通过字符串反向生成对象
request2 = hello_pb2.HelloRequest()
request2.ParseFromString(res_str)
print(request2.name)

#和json对比一下
