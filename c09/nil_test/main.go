package main

import (
	"fmt"
	"unsafe"
)

func main() {
	//make和new函数
	//new函数用法
	//var p *int //申明了一个变量p 但是变量没有初始值 没有内存
	//*p = 10
	//默认值 int byte rune float bool string 这些类型都有默认值
	//指针， 切片 map， 接口这些默认值是nil 理解为none
	var a int
	a = 10
	fmt.Println(a)

	//对于指针来说或者说其他的默认值是0的情况来说 如何一开始申明的时候就分配内存
	var p *int = new(int) //go的编译器就知道先申请一个内存空间，这里的内存中的值全部设置为0
	*p = 10

	//int使用make就不行
	//除了new函数可以申请内存以外 还有一个函数就是make,更加常用的是make函数， make函数一般用于切片 map
	var info map[string]string = make(map[string]string)
	info["c"] = "bobby"

	//new函数返回的是这个值的地址 指针 make函数返回的是指定类型的实例
	//nil的一些细节
	var info2 map[string]string
	if info2 == nil {
		fmt.Println("map的默认值是 nil")
	}

	var slice []string
	if slice == nil {
		fmt.Println("slice的默认值是 nil")
	}

	var err error
	if err == nil {
		fmt.Println("error的默认值是 nil")
	}

	//python中的None和go语言中的nil类型不一样，None是全局唯一的
	//go语言中 nil是唯一可以用来表示部分类型的零值的标识符， 它可以代表许多不同内存布局的值
	fmt.Println(unsafe.Sizeof(slice), unsafe.Sizeof(info2))

}
