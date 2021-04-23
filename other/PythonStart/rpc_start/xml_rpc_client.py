from xmlrpc import client

#xmlrpc挺好用的 和我们调用django的服务器 django这种web框架来说一定是可以做到xmlrpc的效果 django的目的不是这种
# requests调用 httpie postman http协议
#rpc强调的是本地调用效果
#rpc在内部调用很多

server = client.ServerProxy("http://localhost:8088")
print(server.add1(2, 3))