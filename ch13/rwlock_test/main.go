package main

import (
	"fmt"
	"sync"
	"time"
)

/*
锁 - 资源竞争
1. 按理说： 最后的结果应该是0
2. 实际的情况： 1. 不是0 2. 每次的运行结果还不一样
*/
var total int
var wg sync.WaitGroup
var rwLock sync.RWMutex

func read() {
	defer wg.Done()
	rwLock.RLock()
	fmt.Println("开始读取数据")
	time.Sleep(time.Second)
	fmt.Println("读取成功")
	rwLock.RUnlock()
}

func write() {
	defer wg.Done()
	rwLock.Lock()
	fmt.Println("开始修改数据")
	time.Sleep(time.Second * 10)
	fmt.Println("修改成功")
	rwLock.Unlock()
}

func main() {
	wg.Add(6)
	for i := 0; i < 5; i++ {
		go read()
	}

	for i := 0; i < 1; i++ {
		go write()
	}
	wg.Wait()
	fmt.Println(total)
}
