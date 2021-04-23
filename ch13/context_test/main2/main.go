package main

import (
	"fmt"
	"sync"
	"time"
)

var wg sync.WaitGroup
var quit = make(chan bool)

func f() {
	defer wg.Done()
Loop:
	for {
		select {
		case <-quit:
			break Loop
		default:
		}
		fmt.Println("bobby")
		time.Sleep(time.Second)
	}
}

func main() {
	wg.Add(1)
	go f()
	time.Sleep(time.Second * 3)
	quit <- true
	wg.Wait()
}
