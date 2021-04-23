import zerorpc

#生成器
def hello():
    yield "ni"
    yield "hao"
    yield "bobby"

#在功能体验上 client端没有太大的差异
#性能上 服务端上
for data in hello():
    print(data)

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")
#python中的生成器和迭代器
print(c.hello("慕课网")) #希望大家思考一下