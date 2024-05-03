---
b: https://blendedfeelings.com/software/golang/fan-out-fan-in.md
---

# Fan-out and Fan-in 
are concurrency patterns used in Go (Golang) to manage multiple goroutines and channel operations. These patterns help to distribute work among multiple goroutines (fan-out) and then collect the results (fan-in).

### Fan-out:

Fan-out is a pattern where you start multiple goroutines to handle input from a channel. Each goroutine processes part of the data concurrently, which can lead to more efficient use of CPU resources when the tasks are CPU-bound or when I/O operations can be done in parallel.

Here's a simple example of fan-out in Go:

```go
package main

import (
	"fmt"
	"sync"
)

func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Printf("Worker %d started job %d\n", id, j)
		results <- j * 2 // example of some work
		fmt.Printf("Worker %d finished job %d\n", id, j)
	}
}

func main() {
	jobs := make(chan int, 100)
	results := make(chan int, 100)

	// Start 3 worker goroutines (fan-out)
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	// Send 9 jobs and then close the channel to indicate that's all the work
	for j := 1; j <= 9; j++ {
		jobs <- j
	}
	close(jobs)

	// Collect all the results
	for a := 1; a <= 9; a++ {
		<-results
	}
}
```

### Fan-in:

Fan-in is a pattern where you combine multiple results from goroutines into a single channel. This can be useful for aggregating results or for simplifying channel management by having a single point of consumption.

Here's a simple example of fan-in in Go:

```go
package main

import (
	"fmt"
	"sync"
)

// mergeChannels takes multiple channels of int and returns a single channel that closes when all input channels are closed
func mergeChannels(cs ...<-chan int) <-chan int {
	var wg sync.WaitGroup
	out := make(chan int)

	// Start an output goroutine for each input channel in cs
	output := func(c <-chan int) {
		for n := range c {
			out <- n
		}
		wg.Done()
	}

	wg.Add(len(cs))
	for _, c := range cs {
		go output(c)
	}

	// Start a goroutine to close out once all the output goroutines are done
	go func() {
		wg.Wait()
		close(out)
	}()

	return out
}

func main() {
	in1 := make(chan int, 10)
	in2 := make(chan int, 10)

	// Start sending numbers to the input channels
	go func() {
		for i := 0; i < 10; i++ {
			in1 <- i
		}
		close(in1)
	}()
	go func() {
		for i := 10; i < 20; i++ {
			in2 <- i
		}
		close(in2)
	}()

	// Merge the input channels and consume the merged output
	for n := range mergeChannels(in1, in2) {
		fmt.Println(n)
	}
}
```

In these examples, `worker` is the function that processes jobs in the fan-out pattern, and `mergeChannels` is the function that merges multiple channels into one in the fan-in pattern. The fan-in pattern often uses a `sync.WaitGroup` to wait for all processing to complete before closing the final output channel.