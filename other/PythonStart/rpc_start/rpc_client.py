import json

import requests

#自己实现了一个demo级别的rpc封装 代理
class ClientStub:
    def __init__(self, url):
        self.url = url

    def add(self, a, b):
        #1. call id
        #2. 序列化和反序列化
        #3. 传输协议 http
        rsp = requests.get(f"{self.url}/?a={a}&b={b}")
        return json.loads(rsp.text).get("result", 0)


#这不是就是写一个web服务器 无非就是自己封装一下client
#不想知道过多的细节 只想像本地一样调用
client = ClientStub("http://127.0.0.1:8003")
print(client.add(1,2))
print(client.add(2,3))
print(client.add(22,33))