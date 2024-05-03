---
b: https://blendedfeelings.com/software/golang/worker-pools.md
---

# Worker pools in Go (Golang) 
are a pattern used to perform a large number of tasks concurrently by distributing them across multiple worker goroutines. This pattern is useful for controlling the number of goroutines that are active at any one time and for managing concurrency.

Here's a simple example of how to implement a worker pool in Go:

1. Define the task that needs to be performed.
2. Create a channel to send tasks to the workers.
3. Start a number of worker goroutines that read from the tasks channel and execute the tasks.
4. Send tasks to the tasks channel.
5. Close the tasks channel once all tasks have been sent.
6. Wait for all workers to finish processing.

Below is a sample code snippet that demonstrates this pattern:

```go
package main

import (
	"fmt"
	"sync"
	"time"
)

// Task is a function that performs a job.
type Task func()

// WorkerPool starts the specified number of workers and sends tasks to them.
func WorkerPool(tasks []Task, numWorkers int) {
	var wg sync.WaitGroup
	taskChan := make(chan Task)

	// Start workers.
	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		go worker(taskChan, &wg)
	}

	// Send tasks to the workers.
	for _, task := range tasks {
		taskChan <- task
	}

	// Close the channel to signal to the workers that no more tasks will be sent.
	close(taskChan)

	// Wait for all workers to finish.
	wg.Wait()
}

// worker is a goroutine that processes tasks from the taskChan.
func worker(taskChan <-chan Task, wg *sync.WaitGroup) {
	defer wg.Done()
	for task := range taskChan {
		task() // Perform the task.
	}
}

// Example task that just prints a number after a delay.
func exampleTask(number int) Task {
	return func() {
		time.Sleep(100 * time.Millisecond) // Simulate work by sleeping.
		fmt.Println("Processing task", number)
	}
}

func main() {
	// Create a slice of tasks.
	var tasks []Task
	for i := 1; i <= 10; i++ {
		tasks = append(tasks, exampleTask(i))
	}

	// Start the worker pool with 3 workers.
	WorkerPool(tasks, 3)
}
```

In this example, the `WorkerPool` function takes a slice of `Task` functions and the number of workers. It creates a channel to send tasks to the workers and starts the specified number of worker goroutines. Each worker reads from the `taskChan` and executes the tasks. The main function waits for all workers to finish before exiting.

By adjusting the number of workers, you can control the level of concurrency. This pattern is particularly useful for limiting the number of goroutines to prevent excessive resource usage.