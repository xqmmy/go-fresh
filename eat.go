package main

import "fmt"

func main() {
	msg := "inner main"
	{
		msg := "eat better at home"
		fmt.Println(msg)
	}
	fmt.Println(msg)
}
