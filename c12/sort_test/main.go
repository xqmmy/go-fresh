package main

import (
	"fmt"
	"sort"
)

type Course struct {
	Name  string
	Price int
	Url   string
}

type Courses []Course

func (c Courses) Len() int {
	return len(c)
}

func (c Courses) Less(i, j int) bool {
	return c[i].Price < c[j].Price
}

func (c Courses) Swap(i, j int) {
	c[i], c[j] = c[j], c[i]
}

func main() {
	//通过sort来排序
	//让你写一个排序算法， 冒泡 插入 快速 归并 桶排序 算法本质是一样 比较 计数排序
	//你的排序算法是否能应付各种类型的排序
	courses := Courses{
		Course{"django", 300, ""},
		Course{"scrapy", 100, ""},
		Course{"go", 400, ""},
		Course{"torando", 200, ""},
	}
	sort.Sort(courses) //协议 你的目的不是要告诉别人具体的类型，重要的是你的类型必要提供具体的方法
	for _, v := range courses {
		fmt.Println(v)
	}
	//grpc
	//go语言的包以及编码规范 包管理 1.12之前 go的没有包管理 python java maven go modules
}
