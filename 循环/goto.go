package main

import "fmt"

//import "fmt"
//
//func main() {
//	//定义局部变量
//	var a int = 10
//	LOOP:for a<20{
//		if a == 15{
//			a = a+1
//			goto LOOP
//		}
//		fmt.Printf("a的值为 : %d\n",a)
//	}
//}

//func main() {
//	var breakAgain bool
//	for x:=0;x<10;x++{
//		for y:=0;y<10;y++{
//			if y==2 {
//				breakAgain = true
//				break
//			}
//		}
//		if breakAgain {
//			break
//		}
//	}
//	fmt.Println("done")

//}
func main() {
	//goto能不用则不用，goto过于， label过多，整个程序到后期维护就会麻烦
	//最容易理解的代码逐行的执行，哪怕多一个函数的调用对于我们都是理解上的负担
	for x := 0; x < 10; x++ {
		for y := 0; y < 10; y++ {
			if y == 2 {
				// 跳转到标签
				goto breakHere
			}
		}
	}
	// 手动返回, 避免执行进入标签
	return
	// 标签
breakHere:
	fmt.Println("done")
}
