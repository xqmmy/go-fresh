def myfunc():
    sex = "Female"
    print("Female")
    #运行中才会发现很多问题，有很多问题可能会在你的程序已经部署到生产环境中运行到某些逻辑之下才会出现
    if sex == "Male":
        out_str = "性别: 男"
    print(out_str)


if __name__ == "__main__":
    # print(bin(7))
    #ord 并不是简单意义上ascii码值并不准确 ascii->gbk->unicode,
    # print('慕课网"')
    # print(ord("慕"))
    age = 18
    import sys
    #对于python来说，int占用字节是动态，python的int我们不用担心超过上限
    print(sys.getsizeof(age))
    print(sys.getsizeof(71.2))
    print('a'+1)   #“a”表示字符串   单引号不代表字符
    # myfunc()