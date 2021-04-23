package main

import "fmt"

func main() {
	//go中的map ->python中的dict
	//go语言中的map的key和value类型申明的就要指明
	//1. 字面值
	m1 := map[string]string{
		"m1": "v1",
	}
	fmt.Printf("%v\n", m1)

	//2. make函数 make函数可以创建slice 可以创建map
	m2 := make(map[string]string) //创建时，里面不添加元素
	m2["m2"] = "v2"
	fmt.Printf("%v\n", m2)

	//3. 定义一个空的map
	m3 := map[string]string{}
	fmt.Printf("%v\n", m3)

	//map中的key 不是所有的类型都支持，改类型需要支持 == 或者 != 操作
	//int rune
	//a := []int{1,2,3}
	//b := []int{1,2,3}
	//var m1 map[[]int]string

	//a := [3]int{1,2,3}
	//b := [3]int{1,2,3}
	//if a == b {
	//
	//}
	//map的基本
	m := map[string]string{
		"a": "va",
		"b": "vb",
		"d": "",
	}

	//1. 进行增加，修改
	m["c"] = "vc"
	m["b"] = "vb1"
	fmt.Printf("%v\n", m)

	//查询，你返回空的字符串到底是没有获取到还是值本身就是这样空字符串呢
	v, ok := m["d"]
	if ok {
		fmt.Println("找到了", v)
	} else {
		fmt.Println("没找到")
	}
	fmt.Println(v, ok)

	//删除
	//delete(m, "a")
	//delete(m, "e")
	//delete(m, "a")
	//fmt.Printf("%v", m)

	//遍历
	for k, v := range m {
		fmt.Println(k, v)
	}

	//go语言中也有一个list 就是数据结构中提到的链表
	//指针 //为什么指针在java python等很多语言中不存在
}
