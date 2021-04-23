from typing import get_type_hints
from functools import wraps
from inspect import getfullargspec

#函数参数和返回值的类型申明, 反射
def add2(a: int, b: float=3.5) -> float:
    return a+b

def validate_input(obj, **kwargs):
    hints = get_type_hints(obj)
    for para_name, para_type in hints.items():
        if para_name == "return":
            continue
        if not isinstance(kwargs[para_name], para_type):
            raise TypeError("参数：{} 类型错误,应该是：{}".format(para_name, para_type))


def type_check(decorator):
    @wraps(decorator)
    def wrapped_decorator(*args, **kwargs):
        func_args = getfullargspec(decorator)[0]
        kwargs.update(dict(zip(func_args, args)))

        validate_input(decorator, **kwargs)
        return decorator(**kwargs)
    return wrapped_decorator

@type_check
def add(a: int, b: int) -> int:
    return a+b

#调用的时候才能发现类型问题
if __name__ == "__main__":
    #有些人还并不满意
    # print(add("bobby: ", "18"))
    # from typing import get_type_hints
    # print(add.__annotations__)
    # print(get_type_hints(add))
    name = "bobby:'慕课网'"
    name.index("慕")
    name.count("b")
    name.startswith("b")
    name.endswith("网")
    if "慕课网" in name:
        print("yes")
    #in可以用在很多地方
    # print(name)
    print("bobby".upper())
    print("BOBBY".lower())
    print("bobby imooc".split())
    print(",".join(["bobby", "imooc"]))

    name = "bobby"
    age = 18
    print("name:%s, age: %d"%(name, age))
    print("name:{}, age:{}".format(name, age))
    print(f"name:{name}, age:{age}")
    # name = input("请输入你的姓名：")
    # print(name)
    #
    # age = int(input("请输入你的年龄："))
    # print(type(age))
    #python中对于for的用法很统一
    # for index, item in enumerate("bobby:慕课网"):
    #     print(index, item)

    name = "bobby:慕课网"
    print(name[6])
