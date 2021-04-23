#一个简单的计算器
# a = int(input("请输入第一个数："))
# op = input("操作符：")
# b = int(input("请输入第二个数："))
#
# def add(a, b):
#     return a+b
# def sub(a, b):
#     return a-b
# def div(a, b):
#     return a/b
# def mul(a,b):
#     return add
#     # return a*b
#
# op_dict = {
#     "+": add,
#     "-": sub,
#     "/": div,
#     "*": mul,
# }
#
# func = op_dict[op]
# print(func(a, b)(a,b))

#把函数当做普通的变量使用， 还可以当做一个返回值 这个特性就是一等公民的特性

def add(*args, **kwargs):
    sum = 0
    first = kwargs["first"]
    for v in args:
        sum += int(v)
    return sum

def printInfo(name="", age=18):
    print("姓名:{}, 年龄:{}".format(name, age))

datas = [1,2,3,4,5,"6"]
print(add(first=12, last=9))
# printInfo(age=18, name="bobby")
import threading
#有一些情况是需要两种操作都出现 1. 文件 （打开，close） 2. 数据库的连接 （开启连接， 关闭连接） 3. 锁(获取、释放)
def read_file(file_name):
    f = open(file_name)
    with open(file_name) as f:
        sum = 0
        data = [1,2]
        for line in f:
            sum += int(line) #这一行代码可能有异常  很多容易出现异常
        # f.close()
        print("before return")
        re_data = data #data是list类型 值传递  re_data中有一个拷贝=3
        lock = threading.Lock()
        lock.acquire()
        try:
            #此处是多行处理逻辑 这些就可能抛出异常
            pass
        except Exception as e:
            pass
        finally:
            lock.release()  # 此处可能抛出异常
        #此处跳往finally执行
        return re_data
    #1. 代码出现异常导致f.close执行不到 2. 我们忘记close了吧 无论是否正常运行到吗都能够执行到指定的逻辑
print(read_file("xxx.txt"))
#代码很丑陋，一旦逻辑复制 这种代码大量的充斥了我们的代码中， java
#finally有一些细节我们需要知道 就有了第一个印象：finally会在return之后运行
#事实上真的是这样吗？
#原因： 实际上finally是在return之前调用的
#finally中是可以return的 而且这个地方一旦有了return就会覆盖原本的return
