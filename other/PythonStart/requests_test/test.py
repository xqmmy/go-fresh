import requests
from collections import abc
# rsp = requests.post("http://127.0.0.1:8083/form_post", data={
#     "message":"你好",
#     "nick":"bobby"
# })
# print(rsp.text)

# rsp = requests.post("http://127.0.0.1:8083/post?id=1&page=2", data={
#     "name":"bobby",
#     "message":"慕课网"
# })
# print(rsp.text)
# from requests_test.proto import user_pb2
#
# user = user_pb2.Teacher()
#
# rsp = requests.get("http://127.0.0.1:8083/someProtoBuf")
# user.ParseFromString(rsp.content)
# print(user.name, user.course)

import requests

#登录
# rsp = requests.post("http://127.0.0.1:8083/loginJSON", json={
#     "user":"bo",
#     "password":"imooc"
# })
# print(rsp.text)

#注册
# rsp = requests.post("http://127.0.0.1:8083/signup", json={
#     "age":18,
#     "name":"bobby",
#     "email":"12@qq.com",
#     "password":"imooc",
#     "re_password":"imoc"
# })
# print(rsp.text)


rsp = requests.get("http://127.0.0.1:8083/ping", headers={
    "x-token":"boby"
})
print(rsp.text)
