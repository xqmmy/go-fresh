package main

import "fmt"

type Course struct {
	name  string
	price int
	url   string
}
type Printer interface {
	printInfo() string
}

func (c Course) printInfo() string {
	return "课程信息"
}

//func print(x interface{}){
//	if v, ok := x.(int); ok{
//		fmt.Printf("%d(整数)\n", v)
//	}
//	if s, ok := x.(string); ok {
//		fmt.Printf("%s(字符串)\n", s)
//	}
//	//牵扯到go的另一个默认的问题
//	//fmt.Printf("%v\n", i)
//}

type AliOss struct {
}

type LocalFile struct {
}

func store(x interface{}) {
	switch v := x.(type) {
	case AliOss:
		//此处要做一些特殊的处理，我设置阿里云的权限问题
		fmt.Println(v)
	case LocalFile:
		//检查路径的权限
		fmt.Println(v)
	}
}

func print(x interface{}) {
	switch v := x.(type) {
	case string:
		fmt.Printf("%s(字符串)\n", v)
	case int:
		fmt.Printf("%d(整数)\n", v)
	}
}

func main() {
	//空接口
	var i interface{} //空接口
	//空接口可以类似于我们java和python中的object
	//i = Course{}
	//fmt.Println(i)
	i = 10
	print(i)
	i = "bobby"
	print(i)
	i = []string{"django", "scrapy"}
	print(i)
	//空接口的第一个用途 可以把任何类型都赋值给空接口变量
	//2. 参数传递
	//3. 空接口可以作为map的值
	var teacherInfo = make(map[string]interface{})
	teacherInfo["name"] = "bobby"
	teacherInfo["age"] = 18
	teacherInfo["weight"] = 75.2
	teacherInfo["courses"] = []string{"django", "scrapy", "sanic"}
	fmt.Printf("%v", teacherInfo)
	//类型断言
	//接口的一个坑, 接口引入了
	// 接口有一个默认的规范  接口的名称一般以 er结尾
	//c := &Course{}
	//var c Printer = Course{}
	//c.printInfo()

}
