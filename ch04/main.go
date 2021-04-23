package main

import (
	"fmt"
)

func main() {
	//定义bool类型
	//var gender bool = true
	gender := true
	fmt.Println(gender)
	//相比python而言，go语言为什么有这么多种整数类型
	//年龄，分数都是有上线 年龄不超过0-200 分数0-150
	//很多场景之下，数字有上限，我们可以选择合适的数据类型来降低内存的占用，
	//int是一种动态类型，取决机器本身是多少位，64位机器上运行那么int 就是int64，如果是32位机器上那么就是4个字节
	//一般情况下我们都会指明int占用多少个字节
	//var age int = 18
	//fmt.Println(unsafe.Sizeof(age))

	//float类型, float类型最大数
	//var weight float64 = 71.2
	//fmt.Println(math.MaxFloat32)
	//fmt.Println(math.MaxFloat64)
	////为什么64位的float最大值远大于int64，float底层存储和int的存储不一样
	////float32和float64两者占用内存不一样，64位的最大数和精度都比32位高
	//weight := 71.2
	//fmt.Printf("%T\n", weight)
	//age := 18
	//fmt.Printf("%T\n", age)

	//byte和rune
	//byte类型
	//静态语言中中文处理很容易出错
	//var a byte = 18
	//fmt.Println(a)

	a := 'a'
	//这里注意一下 1. a+1可以和数字计算 2.a+1的类型是32 3. int类型可以直接变成字符
	fmt.Printf("%T\n", a+1)
	fmt.Printf("a+1=%c", a+1)
}
