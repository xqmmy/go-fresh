package main

import (
	"fmt"
)

func printArray(toPrint [5]string) {
	//[]string这是切片类型
	toPrint[0] = "bobby"
	fmt.Println(toPrint)
}

func main() {
	//go语言中的数组和python的list可以对应起来理解，slice和python的list更像
	//静态语言中的数组： 1. 大小确定 2. 类型一致
	//数组的申明
	//var courses [10] string
	//var courses = [5]string{"django", "scrapy", "tornado"}
	course := [5]string{"django", "scrapy", "tornado"}
	//静态语言要求严格， 动态语言是一门动态类型的

	//1. 修改值， 取值： 删除值， 添加某一个值， 数组一开始就要指定大小
	//取值， 修改值
	fmt.Println(course[0])
	//修改值
	course[0] = "django3"
	fmt.Println(course)

	//数组的另一种创建方式
	//var a [4] float32
	var a = [4]float32{1.0}
	fmt.Println(a)

	var c = [5]int{'A', 'B'}
	fmt.Println(c)

	//首次接触到了省略号
	d := [...]int{1, 2, 3, 4, 5}
	fmt.Println(d)

	e := [5]int{4: 100}
	fmt.Println(e)

	f := [...]int{0: 1, 4: 1, 9: 100}
	fmt.Println(f)

	//数组操作第一种场景： 求长度
	fmt.Println(len(f))
	//数组操作第二种场景： 遍历数组

	for i, value := range course {
		fmt.Println(i, value)
	}

	//使用for range求和
	sum := 0
	for _, value := range f {
		sum += value
	}
	fmt.Println(sum)

	//使用for语句也可以遍历数组
	sum = 0
	for i := 0; i < len(course); i++ {
		sum += f[i]
	}
	fmt.Println(sum)

	//数组是值类型
	courseA := [3]string{"django", "scrapy", "tornado"}
	courseB := [...]string{"django1", "scrapy1", "tornado1", "python+go", "asyncio"}
	//courseA和courseB应该是同一种类型， 都是数组类型
	//在go语言中，courseA和courseB都是数组，但是不是同一种类型
	fmt.Printf("%T\n", courseA)
	fmt.Printf("%T\n", courseB)
	//如果courseA和courseB是一种类型的话 为什么前面要加一个数组， 长度不一样的数组类型是不一样
	//正是基于这些，在go语言中函数传递参数的时候，数组作为参数 实际调用的时候是值传递
	printArray(courseB)
	fmt.Println(courseB)
}
