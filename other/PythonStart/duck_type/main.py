#go语言的接口（protol 协议）设计是参考了鸭子类型（python）和java的接口
#什么是鸭子类型？ 什么叫协议
#当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子
#采用的是面向对象的类继承
class Animal:
    def born(self):
        pass
    def walk(self):
        pass

class Dog():
    def born(self):
        pass
    def walk(self):
        pass

class Cat(Animal):
    pass

dog = Dog()
#dog是不是动物类 实际上dog就是动物类 忽略了鸭子类型， 对于用惯面向对象的人来说呢 这个做法有点奇怪
#python语言本身的设计上来讲是基于鸭子类型实现的
#Animal实际上只是定义了一些方法的名称而已 其他的任何类只要实现了这个Animal里面的方法那你类就是Animal类型

from typing import Iterable #实际上list没有继承Iterable 好比是一份协议
a = []
print(type(a))
print(isinstance(a, Iterable)) #__iter__ 魔法方法
b = tuple()
print(isinstance(a, Iterable))


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    def __iter__(self):
        return iter(self.employee)


company = Company([100, 110, 120])
for em in company:
    print(em)

#for语句 可以对dict， list tuple set等等类型进行for循环
#for语句可以对iterable类型进行操作 只要你实现了__iter__那你就可以进行for循环
#你的类继承了什么不重要 你的类名称不重要 重要的是你实现了什么魔法方法
# if isinstance(company, Iterable):
#     print("company是iterable类型")
# else:
#     print("company不是iterable类型")
price = (100, 200, 300) #python本身是基于鸭子类型设计的一门语言 - 协议最重要
print(sum(company))
#强调 什么是鸭子类型  非常推荐大家去好好的学习python中的魔法方法

#django+xadmin
#scrapy