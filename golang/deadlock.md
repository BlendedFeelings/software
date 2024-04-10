---
b: https://blendedfeelings.com/software/golang/deadlock.md
---

# Deadlock in Go
occurs when a set of goroutines are waiting for each other to release resources, but none of them can proceed because the resources they need are held by another waiting goroutine. This results in a situation where the program cannot continue to execute because there are no goroutines that can make progress.

Here's an example of how a deadlock might occur in Go:

```go
package main

import (
	"fmt"
	"sync"
)

func main() {
	var mu sync.Mutex
	mu.Lock() // Lock the mutex

	go func() {
		fmt.Println("Trying to lock the mutex from goroutine...")
		mu.Lock() // This will block forever since the main goroutine has already locked the mutex
	}()

	mu.Unlock() // This will never be reached because the main goroutine is waiting for the child goroutine which is blocked
}
```

In this example, the main goroutine locks a mutex and then starts a new goroutine that also attempts to lock the same mutex. However, the main goroutine never unlocks the mutex, so the child goroutine will wait forever. The main goroutine is waiting for the child goroutine to finish (implicitly, because the program would exit when `main` returns), which will never happen because it's blocked on the mutex lock. This is a deadlock.

Deadlocks can also occur with other synchronization primitives like channels. Here's an example with channels:

```go
package main

func main() {
	ch := make(chan int)

	go func() {
		ch <- 1 // This send operation will block because there's no corresponding receive
	}()

	// There should be a receive operation here to match the send operation in the goroutine
	// Since there's no receive, the send operation in the goroutine will block forever, causing a deadlock

	// The main goroutine is also blocked because it's waiting for the child goroutine to finish
}
```

In this case, the goroutine is trying to send a value on a channel, but there's no corresponding receive operation, so the send blocks indefinitely. The main goroutine is also waiting for the child goroutine to finish, which will never happen, leading to a deadlock.

To prevent deadlocks, make sure that:

- Mutexes are always unlocked.
- Channels have corresponding send and receive operations.
- The design of the concurrency in your program doesn't lead to circular waiting conditions.