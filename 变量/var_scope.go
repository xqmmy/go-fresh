package main

import "fmt"

var c = 20

func main() {
	/**
	变量的作用域
	局部变量
	缩进的习惯
	静态语言写起来代码多，但是严谨性很好
	在go中字符和字符串不是一种类型 字符类型是单引号 字符串是双引号
	**/
	sex := "Female"
	if sex == "Female" {
		outStr := "女"
		fmt.Println(outStr)
	}
	fmt.Printf("%T", '慕')
	fmt.Printf("%T", "慕")
}
