package main

import (
	"fmt"
	"strconv"
)

func main() {
	//1. 基本的类型转换
	//a := int(3.0)
	//fmt.Println(a)
	////在go语言中不支持变量间的隐式类型转换
	////1. 变量间类型转换不支持
	//var b int = 5.0 //常量,常量到变量是会进行隐式转换
	//fmt.Println(b)
	//
	//c := 5.1
	//fmt.Printf("%T\n", c)
	//var d int = int(c)
	//fmt.Println(d)

	//var a int64 = 56
	//var b int32 = int32(a)
	//fmt.Println(b)
	//
	////int转字符串 itoa
	//fmt.Printf("%T\n", strconv.Itoa(int(a)))
	////字符串转int aoti
	//data, _ := strconv.Atoi("12")
	//fmt.Println(data)
	//parse类的函数
	//b, err := strconv.ParseBool("False")
	//fmt.Println(err)
	//fmt.Println(b)
	//f, err := strconv.ParseFloat("3.1415", 32)
	//fmt.Println(err)
	//fmt.Printf("%T\n", f)
	//i, err := strconv.ParseInt("012", 0, 64)
	//fmt.Println(err)
	//fmt.Printf("%T %d\n", i, i)
	//u, err := strconv.ParseUint("42", 10, 64)

	//其他类型转字符串
	//s := strconv.FormatBool(true)
	//fmt.Println(s)
	//s := strconv.FormatFloat(3.1415, 'E', -1, 64)
	//fmt.Println(s)
	//s := strconv.FormatInt(-42, 16) //表示将-42转换为16进制数，转换的结果为-2a。
	//s := strconv.FormatUint(42, 10)
	//fmt.Println(s)
	var data int
	var err error
	if data, err = strconv.Atoi("12"); err != nil {
		fmt.Println("转换出错")
	}
	fmt.Println(data)

}
