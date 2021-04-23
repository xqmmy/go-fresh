package main

import "fmt"

type Course struct {
	name  string
	price int
}

type Callable interface {
}

type handle func(str string)

func main() {
	//go语言中的关键词 type
	//1. 给一个类型定义别名, 实际上为什么会有byte， 就是我为了强调我们现在处理的对象是字节类型 这种别名实际上还是为了代码的可读性， 这个实际上本质上仍然是uint8 无非就是在代码编码阶段可读性强而已
	type myByte = byte
	var b uint8
	fmt.Printf("%T\n", b)

	//2. 第二种 就是基于一个已有的类型定义一个新的类型
	type myInt int
	var i myInt
	fmt.Printf("%T\n", i)

	//3. 定义结构体
	//4. 定义接口
	//5. 定义函数别名
}
