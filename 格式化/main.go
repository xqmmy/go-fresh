package main

import (
	"fmt"
)

func main() {
	//name := "phil"
	//age := 18
	//fmt.Printf("name: %T,age: %T \n",name, age)
	//fmt.Println("name:"+name+",age"+strconv.Itoa(age))
	//fmt.Printf("name: %T,age: %T \n",name, age)
	//fmt.Printf("name:%s, age:%x,\n ", name, age)
	//desc := fmt.Sprintf("name:%s, age:%x,\n ", name, age)
	//fmt.Println(desc)
	//
	//
	//data := 65
	//fmt.Printf("%q\n", data)
	//fmt.Printf("%e", 65.1)
	//
	////输入
	//var n string
	//var a int
	////fmt.Println("请输入你的姓名和年龄:")
	////fmt.Scanln(&n, &a)
	////fmt.Println(n, a)
	//
	////通过scanf输入
	//fmt.Println("请输入你的姓名和年龄:")
	////输入的内容必须符合指定的格式
	//fmt.Scanf("请输入你的姓名和年龄:%s %d", &n, &a)
	//fmt.Println(n, a)

	var name string
	var age byte
	var sal float32
	var isPass bool
	fmt.Println("请输入姓名 ")
	//当程序执行到 fmt.Scanln(&name),程序会停止在这里，等待用户输入，并回车
	fmt.Scanln(&name)
	fmt.Println("请输入年龄 ")
	fmt.Scanln(&age)
	fmt.Println("请输入薪水 ")
	fmt.Scanln(&sal)
	fmt.Println("请输入是否通过考试 ")
	fmt.Scanln(&isPass)
	fmt.Printf("名字是 %v \n 年龄是 %v \n 薪水是 %v \n 是否通过考试 %v \n", name, age, sal, isPass)
	// 方式2 fmt.Scanf,可以按指定的格式输入
	fmt.Println("请输入你的姓名，年龄，薪水, 是否通过考试， 使用空格隔开")
	fmt.Scanf("%s %d %f %t", &name, &age, &sal, &isPass)
	//fmt.Scanf("请输入你的姓名和年龄:%s %d", &n, &a)
	//fmt.Println(n, a)

}
