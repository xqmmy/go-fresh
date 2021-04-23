package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func consumer(msg chan int) {
	defer wg.Done()
	fmt.Println(<-msg)
}

func main() {
	var msg chan int
	msg = make(chan int)
	wg.Add(1)
	go consumer(msg)
	msg <- 1 //当你进行 放数据到msg中的时候 这个时候会阻塞的，阻塞之前会获取一把锁， 这把锁什么时候释放 肯定是要等到数据被消费之后
	wg.Wait()
	//channel是多个goroutine之间线程安全， 如何保证的呢 使用锁？
	//如果你是没有缓冲的channel 在没有启动一个消费者之前 你放数据就会报错
	//data := <- msg
	//fmt.Println(data)
}
