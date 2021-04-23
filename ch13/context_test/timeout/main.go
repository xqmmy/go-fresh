package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

var wg sync.WaitGroup

func readCpu(ctx context.Context) {
	defer wg.Done()
	for {
		select {
		case <-ctx.Done():
			fmt.Println("退出监控")
			return
		default:
			fmt.Println("获取到cpu信息")
			time.Sleep(1 * time.Second)
		}
	}
}

func main() {
	wg.Add(1)
	ctx, _ := context.WithTimeout(context.Background(), 3*time.Second)
	go readCpu(ctx)
	wg.Wait()
}
