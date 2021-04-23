#错误和异常
#除法函数
def div(a, b):
    #稍微认真一点的程序员都会在除法函数中判断我们被除数(b)是否为0
    if b == 0:
        return None, "被除数不能为0"
        # raise Exception("被除数不能为0") #异常

    #dict访问了一个不存在的key， 在list中对空的list进行了data[0]
    user_info_dict = {
        "name":"bobby",
        "age":18
    }
    if "weight" in user_info_dict:
        user_info_dict["weight"]

    #如果每个地方都这样写那代码中的if就太多了，那就是你的bug，这种问题就一定要早发现
    return a/b, None

#如果你的这个函数-div返回的是None这个时候调用者不会出问题
#错误和异常 错误就是可以预先知道的出错的可能，这个时候我们把这情况叫做错误， 不可预知的问题叫做异常
#程序员写的代码不严谨造成的某个地方在某种情况下产生了异常

def cal():
    while 1:
        a = int(input())
        b = int(input())
        v, err = div(a, b)
        if err is not None:
            print(err)
        else:
            print(err)
        # try:
        #     div(a, b)
        # except Exception as e:
        #     print(e)
    #后面还有逻辑

    #被调用函数传递的异常会导致我们的cal函数出现异常


import re
desc = "bobby:18"
m = re.match("bobby1:(.*)", desc)
if m is not None:
    print(m.group(1))

def run():
    raise Exception("错误")

def run2():
    print("bobby")

import threading
if __name__ == "__main__":
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)
    t2.start()
    t1.start()
    t1.join()
    t2.join()


