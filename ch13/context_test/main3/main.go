package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

var wg sync.WaitGroup

func f2(ctx context.Context) {
	defer wg.Done()
	//Loop:
	for {
		//select {
		//case <- ctx.Done():
		//	break Loop
		//default:
		//}
		fmt.Println("f2 is running")
		time.Sleep(time.Second)
	}
}

func f(ctx context.Context) {
	defer wg.Done()
	go f2(ctx)
Loop:
	for {
		select {
		case <-ctx.Done():
			break Loop
		default:
		}
		fmt.Println("f1 is running")
		time.Sleep(time.Second)
	}
}

func main() {
	ctx, cancel := context.WithCancel(context.TODO())
	wg.Add(1)
	go f(ctx)
	time.Sleep(time.Second * 3)
	cancel()
	wg.Wait()
	time.Sleep(time.Second * 3)
}
