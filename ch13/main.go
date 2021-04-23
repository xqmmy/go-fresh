package main

import (
	"fmt"
	"time"
)

func main() {
	for i := 0; i < 1000; i++ {
		go func(i int) {
			for {
				fmt.Println(i)
				time.Sleep(time.Second * 1)
			}
		}(i)
	}
}
