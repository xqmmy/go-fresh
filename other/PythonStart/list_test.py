#
from typing import List
from copy import deepcopy
def print_list(course: List[str]):
    course[0] = "bobby"
    print(course)

#引用传递
courses = ["django", "scrapy", "tornado", "python", "asyncio"]
# print_list(deepcopy(courses))
# print(type(courses))
sub_courses = courses[1:4] #左闭右开的区间[1:4) #新的list,底层的数据是复制出来的
my_list = list
sub_courses[0] = "imooc"
print(sub_courses)
print(type(sub_courses))
print(courses)
# if "scrapy" in courses: #内部无非就是实现了一个魔法方法 __contains__
#     print("yes")
#python的list进行切片操作以后返回的是新的list
a = [1,2,3]
b = a[:]
b[0] = 8
print(a)
print(b)

m = {
    "a":"va",
    "b":"vb"
}

a = None
b = None
print(id(a), id(b))
print(m.get("d", "bobby"))
if "a" in m:
    print("yes")

