package main

import (
	"fmt"
	"time"
)

func f1() {
	defer func() {
		err := recover()
		if err != nil {
			fmt.Println("捕获到了")
		}
	}()

	go func() {
		defer func() {
			err := recover()
			if err != nil {
				fmt.Println("捕获到了2")
			}
		}()

		panic("出错了")
	}()
	time.Sleep(10 * time.Second)
}

func main() {
	f1()
	//http.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
	//	//go func() {
	//	//	panic("error")
	//	//}()
	//	//操作redis的，有人觉得这段代码可以放到协程中去运行。有一个非常大的隐患了
	//	//panic("error")
	//	w.Write([]byte("hello world!"))
	//})
	//
	//http.ListenAndServe("127.0.0.1:8080", nil)

	//panic会引起主线程的挂掉， 同时会导致其他的协程都挂掉
	//为什么直接在, 在父协程中无法捕获子协程中出现的异常
}
