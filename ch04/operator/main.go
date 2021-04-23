package main

import "fmt"

func main() {
	//var a bool = true
	//var b bool = false
	//if a && b {
	//	fmt.Printf("第一行 - 条件为 true\n" )
	//}
	//if a || b  {
	//	fmt.Printf("第二行 - 条件为 true\n" )
	//}
	///* 修改 a 和 b 的值 */
	//a = false
	//b = true
	//if a && b  {
	//	fmt.Printf("第三行 - 条件为 true\n" )
	//} else {
	//	fmt.Printf("第三行 - 条件为 false\n" )
	//}
	//if !(a && b) {
	//	fmt.Printf("第四行 - 条件为 true\n" )
	//}

	var a int = 21
	var c int

	c = a
	fmt.Printf("第 1 行 - =  运算符实例，c 值为 = %d\n", c)

	c += a
	//c = 42
	fmt.Printf("第 2 行 - += 运算符实例，c 值为 = %d\n", c)

	c -= a //c = 21
	fmt.Printf("第 3 行 - -= 运算符实例，c 值为 = %d\n", c)

	c *= a //441
	fmt.Printf("第 4 行 - *= 运算符实例，c 值为 = %d\n", c)

	c /= a //c=21
	fmt.Printf("第 5 行 - /= 运算符实例，c 值为 = %d\n", c)

	c = 200

	c <<= 2
	fmt.Printf("第 6行  - <<= 运算符实例，c 值为 = %d\n", c)

	c >>= 2
	fmt.Printf("第 7 行 - >>= 运算符实例，c 值为 = %d\n", c)

	c &= 2
	fmt.Printf("第 8 行 - &= 运算符实例，c 值为 = %d\n", c)

	c ^= 2
	fmt.Printf("第 9 行 - ^= 运算符实例，c 值为 = %d\n", c)

	c |= 2
	fmt.Printf("第 10 行 - |= 运算符实例，c 值为 = %d\n", c)

}
