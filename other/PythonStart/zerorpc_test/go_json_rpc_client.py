import json
import socket

# request = {
# #     "id":0,
# #     "params":["bobby"],
# #     "method": "HelloService.Hello"
# # }
# # 
# # client = socket.create_connection(("localhost", 1234))
# # client.sendall(json.dumps(request).encode())
# # 
# # #获取服务器返回的数据
# # rsp = client.recv(1024)
# # rsp = json.loads(rsp.decode())
# # 
# # print(rsp["result"])

request = {
    "id":0,
    "params":["bobby"],
    "method": "HelloService.Hello"
}

import requests
rsp = requests.post("http://localhost:1234/jsonrpc", json=request)
print(rsp.text)
