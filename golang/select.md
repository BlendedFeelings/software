---
b: https://blendedfeelings.com/software/golang/select.md
---

# Select statement in Go 
lets a goroutine wait on multiple communication operations. It is similar to a switch statement but for channels. The `select` statement blocks until one of its cases can run, then it executes that case. If multiple cases are ready, it picks one at random.

Here's an example of how to use the `select` statement in Go:

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	ch1 := make(chan string)
	ch2 := make(chan string)

	go func() {
		time.Sleep(1 * time.Second)
		ch1 <- "Message from channel 1"
	}()

	go func() {
		time.Sleep(2 * time.Second)
		ch2 <- "Message from channel 2"
	}()

	for i := 0; i < 2; i++ {
		select {
		case msg1 := <-ch1:
			fmt.Println("Received:", msg1)
		case msg2 := <-ch2:
			fmt.Println("Received:", msg2)
		}
	}
}
```

In this example, there are two channels `ch1` and `ch2`. Two separate goroutines send messages to these channels after sleeping for 1 and 2 seconds, respectively. The `main` function uses a `select` statement inside a loop to receive messages from whichever channel is ready first. Once a message is received, the `select` case for that channel will execute, and the message will be printed to the console.

The `select` statement is often used in conjunction with goroutines and channels to handle asynchronous communication in concurrent Go programs.