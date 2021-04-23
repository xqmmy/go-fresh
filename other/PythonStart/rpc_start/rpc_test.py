import json

def add(a, b):
    total = a + b
    return total

#现在想把add函数放到另一台服务器上去调用
#网络 web框架
#json http请求
#json 就是协议 json是一种数据格式 协议 json.dumps() 序列化 json.loads() 反序列化 成dict list


class Company:
    name = "慕课网"
    address = "北京市"


class Student:
    name = "bobby"
    company = Company()

    def to_json(self):
        json_data = {
            "name":self.name,
            "company":{
                "name":self.company.name,
                "address":self.company.address
            }
        }
        return json.dumps(json_data)


def print_info_rpc(student):
    #1. 建立连接 requests， socket
    #2. 将student变成json字符串 序列化
    #3. 发送json字符串
    #4. 等待对方发送结果过来 json - 去解析 反序列化 性能比较低 grpc
    #5. 继续解析的结果进行业务逻辑
    print(f"姓名:{student.name}, 公司：{student.company.name}")

#student的类， python的类， 不行
#服务器采用的是go语言
#这个内存中的对象可以变成一个网络中的对象， 二进制
#json
print_info_rpc(Student())

#http协议来说 有一个问题： 一次性 一旦对方返回了结果 连接断开 http2.0 长连接 grpc