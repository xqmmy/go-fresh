package main

import "fmt"

//func main() {
//	fmt.Println("test1")
//	//defer之后只能是函数调用 不能是表达式 比如 a++
//	defer fmt.Println("defer test1")
//	defer fmt.Println("defer test2")
//	defer fmt.Println("defer test3")
//	/*
//	defer 语句是go体用的一种用于注册延迟调用的机制， 它可以让当前函数执行完毕之后执行
//	对于python的with语句来说，
//	 */
//	//此处有大量的逻辑需要读取文件
//	fmt.Println("test2")
//	//1. 如果有多个defer会出现什么情况 多个defer是按照先入后出的顺序执行
//}

//func main()  {
//	//defer语句执行时的拷贝机制
//	test := func () {
//		fmt.Println("test1")
//	}
//	defer test()
//	test = func () {
//		fmt.Println("test2")
//	}
//	fmt.Println("test3")
//}

//func main()  {
//	//defer语句执行时的拷贝机制
//	x := 10
//	defer func (a *int) {
//		fmt.Println(*a)
//	}(&x)
//	x++
//}

//func main()  {
//	//defer语句执行时的拷贝机制
//	x := 10
//	//此处的defer函数并没有参数，函数内部使用的值是全局的值
//	defer func (a int) {
//		fmt.Println(x)
//	}(x)
//	x++
//}

func f1() int {
	x := 10
	defer func() {
		x++
	}()
	tmp := x //x是int类型 值传递
	return tmp
}

func f2() *int {
	a := 10
	b := &a
	defer func() {
		*b++
	}()
	temp_data := b
	return temp_data
}
func main() {
	fmt.Println(f1()) //是不是就意味着 defer中影响不到外部的值呢
	fmt.Println(*f2())
	//defer本质上是注册了一个延迟函数，defer函数的执行顺序已经确定
	//defer 没有嵌套 defer的机制是要取代try except finally
	//https://www.cnblogs.com/zhangboyu/p/7911190.html
	//https://studygolang.com/articles/24044?fr=sidebar
}
