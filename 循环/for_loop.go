package main

import "fmt"

func main() {
	//for init;condition;post{} calculate sum 1-10
	sum := 0
	for i := 1; i <= 10; i++ {
		sum += i
	}
	fmt.Println(sum)

	j := 0
	for ; j < 10; j++ {
		fmt.Println("phil")
	}

	name := "phil:ai"
	for index, value := range name {
		fmt.Printf("%c\n", value)
		fmt.Println(index, value)
	}
	//1. name是一个字符串， 2. 字符串是字符串的数组
	name_arr := []rune(name)
	for i := 0; i < len(name_arr); i++ {
		fmt.Printf("%c\n", name_arr[i])
		//2. 在做字符串遍历的时候要尽量使用range
	}
}
