#python3.8提供了一个新的运算符 - 海象运算符 可以为我们的表达式赋值

course_list = ["django", "scrapy", "tornado"]
# if (course_size := len(course_list)) >= 3:
#     print("课程较多， 课程数量： {}".format(course_size))

# course_size = len(course_list)
# powers = [course_size, course_size**2, course_size**3]
# print(powers)

# powers = [course_size:=len(course_list), course_size**2, course_size**3]
# print(powers)

# import re
# desc = "bobby:18"
# if m := re.match("bobby:(.*)", desc):
#     age = m.group(1)
#     print(age)

age = 18
age += 5

#类型注解
#动态语言不需要声明变量类型，这种做法在很多人眼里是不好 不好维护的代名词
#len(course_list)调用了两边, len(course_list)只调用了一次

#变量的类型说明， 一般情况下我们会通过变量名来隐含的说明该变量的类型
age: int = 18 #说明该类型是int类型
#python有大量的内置类型 int float bool str bytes
name: str = "bobby"
sex: bool = True
weight: float = 75
x: bytes = b"test"

age = "18"

#类型的申明，不会实际影响使用,hints 提示作用，pycharm是支持这种提示的
print(age)
#但是实际上这种做也会有明显的缺点，损失了python本身的灵活性。
#复杂数据类型的申明
courses: list = ["django", "scrapy", "tornado"] #有问题，
from typing import List, Set, Dict, Tuple
courses: List[str] = ["django", "scrapy", "tornado"]
courses.append("asyncio")
courses.append(1)
print(courses)

user_info: Dict[str, float] = {"bobby": 75.2}
names: Tuple[int, ...] = (1,2,3)
name: str
name = "bobby"

#函数变量类型的声明其实意义更大