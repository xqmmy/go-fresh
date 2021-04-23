import zerorpc


class HelloRPC(object):
    def hello(self, name):
        #调用了另一个服务
        #流处理
        #本地查询了数据， 源源不断的给数据给客户端
        return "Hello, %s" % name


#1. 实例化一个server
#2. 绑定我们的业务代码到server中
#3. 启动server
s = zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()