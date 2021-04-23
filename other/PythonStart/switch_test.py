#1. 采用dict映射
score = 80

switch = {
    90:lambda : print("A"),
    80:lambda : print("B"),
    70:lambda : print("C"),
    60:lambda : print("D"),
}
switch[score]()

