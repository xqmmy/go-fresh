package main

import (
	"fmt"
	"sync"
)

//如何解决主的goroutine在子协程结束后自动结束
var wg sync.WaitGroup

//WaitGroup提供了三个很有用的函数
/*
Add
Done
Wait
Add的数量和Done的数量必须相等
*/
func f(n int) {
	defer wg.Done()
	fmt.Println(n)
}
func main() {
	wg.Add(5)
	for i := 0; i < 5; i++ {
		go f(i)
	}
	wg.Wait()
}
