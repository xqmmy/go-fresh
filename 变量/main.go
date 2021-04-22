package main

import "fmt"

func main() {
	/**变量
	静态的语言的变量和动态语言的变量定义差异很大
	1、最基础的变量定义
	var i int
	i = 20
	定义并初始化
	var i int = 10
	2、根据值自行判断变量类型(类型推断)
	var i = 100
	3、省略 var
	i := 100
	var a int = 10
	var b = 10
	c := 10
	多变量定义
	var a,b,c int
	a,b,c = 10,20,30
	var a,b,c int = 10,20,30
	集合类型
	var(
	 	a int
		name string
	)
	var i int = 10
	i = 20
	匿名变量，变量一旦被定义
	变量 -
	const PI = 3.1415926
	r := 2.0
	运行过程中， 代码写的不好 一不小心在某个地方将PI给改掉了
	枚举
	const(
		Unknown = 0
		Female = 1
		Male = 2
	)
	常量组如不指定类型和初始化值，该类型和值和上一行的类型一致
	1、常量的数据可以是布尔，数字和字符串
	2、不曾使用的常量，在编译的时候不会报错
	const常量iota,常量计数器 枚举
	0,1,2 本身不重要， 这三个值不一样
	iota 该常量的值等于上一个常量的表达式
	1. iota只能在常量组中是使用
	2. 不同的const定义块互相不干扰
	3. 没有表达式的常量定义复用上一行的表达式
	4. 从第一行开始，iota从0逐行加1
	**/
	const (
		Book = iota
		Cloth
		Phone = 88
		DeskTop
	)
	fmt.Println(Book, Cloth, Phone, DeskTop)

	const (
		a = iota
		b = 10
		c
		d, e = iota, iota
		f    = iota
	)
	fmt.Println(a, b, c, d, e, f)
}
