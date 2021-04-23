from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


def add(a, b):
    return a + b

#1. 实例化server
server = SimpleJSONRPCServer(('localhost', 8000))
#2. 将函数注册到server中
server.register_function(add)
#3. 启动server
server.serve_forever()

#多线程
#协程 go中 netty asyncio
#jsonrpclib如果只是完成了这样一个简单的调用那么jsonrpclib和xmlrpcserver几乎没有优势可言
#任何一个web服务如果不具备并发接收和处理的能力的话 那么这个server就没有用