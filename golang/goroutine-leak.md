---
b: https://blendedfeelings.com/software/golang/goroutine-leak.md
---

# Goroutine leak in Go 
refers to a situation where goroutines are spawned but never terminated, causing them to remain in memory indefinitely. This can lead to increased memory usage and eventually exhaust the system's resources, leading to performance degradation or crashes.

Goroutine leaks typically occur for a few reasons:

1. **Blocking on Channels**: A goroutine is waiting for a message on a channel that is never sent, or all references to the channel are lost without closing it.

    ```go
    func leakyGoroutine() {
        ch := make(chan int)
        go func() {
            val := <-ch // This will wait forever if nothing is sent on ch
        }()
        // No value is ever sent to ch, and there's no way to stop the goroutine
    }
    ```

2. **Blocking on Synchronization Primitives**: A goroutine is waiting on a synchronization primitive (like a `sync.WaitGroup`, `sync.Mutex`, etc.) that never gets released.

    ```go
    var wg sync.WaitGroup
    wg.Add(1)
    go func() {
        // ... some code that might return early or panic before calling Done
        // wg.Done() is never called
    }()
    wg.Wait() // This will wait forever
    ```

3. **Deadlock**: All goroutines are waiting for each other to release resources, and none can proceed.

    ```go
    func deadlock() {
        ch1 := make(chan int)
        ch2 := make(chan int)

        go func() {
            <-ch1
            ch2 <- 1
        }()

        go func() {
            <-ch2
            ch1 <- 1
        }()
        // Both goroutines are waiting for each other and will never proceed
    }
    ```

4. **Abandoned Goroutines**: A goroutine that is detached from the main flow of the program and has no way to receive a signal to exit.

    ```go
    func abandonedGoroutine() {
        go func() {
            for {
                // Do some work...
                time.Sleep(1 * time.Second) // Sleep for a second
            }
            // There's no condition to break out of this loop
        }()
        // The main function returns and the program exits, but the goroutine is still running
    }
    ```

To prevent goroutine leaks:

- Always make sure that goroutines have a way to exit, for example by using `select` with a `context.Context` to handle cancellation.
- Be careful with channel operations; consider using `select` with a `default` case to avoid blocking indefinitely.
- Clean up resources properly and ensure that all paths of execution signal completion to any synchronization primitives.
- Use buffered channels where appropriate to prevent goroutines from blocking each other.
- Monitor your goroutines. Tools like `runtime` package can help you track the number of running goroutines.

Detecting and fixing goroutine leaks often involves careful code review, profiling, and sometimes using specialized tools like `go-leak` to monitor goroutine behavior over time. It's important to have a clear understanding of concurrency patterns and potential pitfalls when working with goroutines.