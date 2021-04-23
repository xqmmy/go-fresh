from calc.add import add1

def sub(x: int, y:int) -> int :
    print(add1(x, y))
    return x - y

#每多一个文件就多了一个package

print(sub(1,2))