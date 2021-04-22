package main

import (
	"fmt"
	"strings"
)

func main() {
	/**
	字符串基本操作
	1.字符串的长度
	返回的是字节的长度
	涉及到中文问题就产生了变化
	Unicode字符集，存储的时候需要utf8编码规则，utf8编码是一个动态的编码规则
	utf8编码，还能够用一个字节表示英文
	**/
	var name string = "phil:\"慕\""
	fmt.Println(len(name))
	/**
	类型转换
	**/
	name_arr := []int32(name)
	fmt.Println(len(name_arr))
	fmt.Println(len("phil:"))

	date := "2020\\06\\18"
	fmt.Println(date)
	//是否包含某个子串
	var name1 string = "phil:\"慕课网\""
	fmt.Println(strings.Contains(name1, "慕课网"))
	fmt.Println(strings.Index(name1, "慕课网"))
	//统计出现的次数
	fmt.Println(strings.Count(name, "b"))
	//前缀和后缀
	fmt.Println(strings.HasPrefix(name, "h"))
	fmt.Println(strings.HasSuffix(name, "\""))

	//4. 大小写转换
	fmt.Println(strings.ToUpper("bobby"))
	fmt.Println(strings.ToLower("BOBBY"))

	//5. 字符串的比较
	fmt.Println(strings.Compare("ab", "aa")) //字符的比较就是ascii的比较 返回-1， 1， 0
	fmt.Println(strings.Compare("b", "a"))   //字符的比较就是ascii的比较 返回-1， 1， 0
	fmt.Println(strings.Compare("b", "b"))   //字符的比较就是ascii的比较 返回-1， 1， 0

	//6. 去掉空格和指定字符串
	fmt.Println(strings.TrimSpace(" bobby "))
	fmt.Println(strings.TrimLeft("bobby", "b"))
	fmt.Println(strings.Trim("bobby", "b"))

	//7. split方法
	fmt.Println(strings.Split("bobby imooc", " "))

	//8. 合并 join方法将字符串数组连接起来
	arrs := strings.Split("bobby imooc", " ")
	fmt.Println(strings.Join(arrs, "-"))

	//9. 字符串替换
	fmt.Println(strings.Replace("bobby: 18 电话：18888888", "18", "19", 2))
}
