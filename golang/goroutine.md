# Goroutine 
is a lightweight thread managed by the Go runtime. Goroutines are used to perform work concurrently within a program. Unlike threads in many other programming languages, goroutines are extremely cheap to create in terms of memory and CPU overhead, which allows you to start thousands or even millions of them in the same program without running into resource constraints.

Here's how you can work with goroutines in Go:

1. **Starting a Goroutine**: You start a goroutine by using the `go` keyword followed by a function call. This will execute the function concurrently with the rest of the program.

```go
package main

import (
	"fmt"
	"time"
)

func sayHello() {
	fmt.Println("Hello!")
}

func main() {
	go sayHello()
	time.Sleep(time.Second) // Wait for the goroutine to finish
}
```

2. **Anonymous Goroutines**: You can also start a goroutine with an anonymous function.

```go
go func() {
	fmt.Println("Hello from an anonymous function!")
}()
```

3. **Passing Arguments**: When you need to pass arguments to a goroutine, you do it in the same way as you would with a normal function call.

```go
go func(msg string) {
	fmt.Println(msg)
}("Hello with arguments!")
```

4. **Synchronization**: Since goroutines run concurrently, you often need a way to synchronize them. This is typically done using channels or synchronization primitives from the `sync` package, such as `WaitGroup`.

```go
package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func printCount(c chan int) {
	for count := range c {
		fmt.Println(count)
		wg.Done()
	}
}

func main() {
	c := make(chan int)
	wg.Add(2)
	go printCount(c)
	go func() {
		for i := 0; i < 2; i++ {
			c <- i
		}
		close(c)
		wg.Done()
	}()
	wg.Wait()
}
```

In this example, we use a `WaitGroup` to wait for both goroutines to finish their work. The channel `c` is used for communication between the goroutines.

Remember that when using goroutines, you must consider the potential for race conditions and design your program to handle concurrent access to shared resources safely. The `sync` package provides several utilities to help with this, such as `Mutex` and `RWMutex`.