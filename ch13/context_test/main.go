package main

import (
	"fmt"
	"sync"
	"time"
)

var wg sync.WaitGroup
var quit bool

func f() {
	defer wg.Done()
	for {
		if quit {
			break
		}
		fmt.Println("bobby")
		time.Sleep(time.Second)
	}
}

func main() {
	go f()
	time.Sleep(time.Second * 3)
	quit = true
	wg.Wait()
}
