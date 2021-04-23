from xmlrpc.server import SimpleXMLRPCServer

#python中类的命名方式遵循驼峰命名法
#1. 没有出现url的映射
#2. 没有编码和解码
#序列化和反序列化协议是 xml json
class Calculater:
    def add(self, x, y):
        return x + y
    def multiply(self, x, y):
        return x * y
    def subtract(self, x, y):
        return abs(x-y)
    def divide(self, x, y):
        return x/y

obj = Calculater()
server = SimpleXMLRPCServer(("localhost", 8088))
# 将实例注册给rpc server
server.register_instance(obj)
print("Listening on port 8088")
server.serve_forever()