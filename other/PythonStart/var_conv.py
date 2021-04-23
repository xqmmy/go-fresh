#1. python的类型相比go而言少很多 int float
#1. 字符串转int
data = "21"
int_data = int(data, 16)
print(type(int_data), int_data)

#2. int转字符串
data_str = str(int_data)
print(type(data_str), data_str)

#3. float类型转换
data_float = float("3.1415")
print(type(data_float), data_float)

float_str = str(data_float)
print(type(float_str), float_str)

#4. bool类型转换 , 字符串转bool只要字符串不是空字符串 都是true
# bool_data = bool("12")
# print(bool_data)

from distutils.util import strtobool
bool_data = strtobool("2")
print(bool_data)

