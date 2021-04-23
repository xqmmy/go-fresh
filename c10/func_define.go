package main

import (
	"errors"
	"fmt"
)

//相比较其他静态语言，go语言的函数有很多两点
//函数的几个要素： 1. 函数名 2. 参数 3. 返回值
//函数第一种定义方法
func add(a, b int) int {
	var sum int
	sum = a + b
	return sum
}

//函数的第二种定义方法
func add2(a, b int) (sum int) {
	sum = a + b
	return sum
}

//函数的第三种定义方法
func add3(a, b int) (sum int) {
	sum = a + b
	return
}

//函数的第4种定义方法
// 被除数等于0 ，要返回多个值 -一个非常有用的特性
//go语言的返回设置花样很多
func div(a, b int) (int, error) {
	var result int
	var err error
	if b == 0 {
		err = errors.New("被除数不能为0")
	} else {
		result = a / b
	}

	return result, err
}

func div2(a, b int) (result int, err error) {
	if b == 0 {
		err = errors.New("被除数不能为0")
	} else {
		result = a / b
	}

	return
}

func main() {
	result, err := div2(12, 3)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(result)
		fmt.Println(a1)
	}
}
