package main

import "fmt"

type Teacher struct {
	Name  string
	Age   int
	Title string
}

func (t Teacher) teacherInfo() {
	fmt.Printf("姓名:%s, 年龄:%d, 职称:%s", t.Name, t.Age, t.Title)
}

type Course struct {
	Teacher //如果讲师的信息比较多怎么办 将另一个结构体的变量放进来
	Name    string
	Price   int
	Url     string
}

//匿名嵌套, 这种做法其实就是 语法糖 还不算是继承 有了前面的方法和这里的内嵌结构体 实际上 继承 封装
func (c Course) courseInfo() {
	fmt.Printf("课程名:%s, 价格:%d, 讲师信息：%s %d %s", c.Name, c.Price, c.Teacher.Name, c.Age, c.Title)
}

//这种继承的效果说实话 有点说服不了人
func main() {
	//go语言的继承 组合
	t := Teacher{
		Name:  "bobby",
		Age:   18,
		Title: "程序员",
	}
	c := Course{
		Teacher: t,
		Price:   100,
		Url:     "",
		Name:    "django",
	}
	c.courseInfo()

}
