# Synchronization between goroutines 
can be achieved using various synchronization primitives provided by the `sync` package. Here are some of the most common ways to synchronize goroutines:

1. **WaitGroups**: A `sync.WaitGroup` is used to wait for a collection of goroutines to finish executing. You can call `Add()` to set the number of goroutines to wait for, `Done()` to signal that a goroutine has finished, and `Wait()` to block until all goroutines have called `Done()`.

   ```go
   var wg sync.WaitGroup

   for i := 0; i < 5; i++ {
       wg.Add(1)
       go func(i int) {
           defer wg.Done()
           // Do some work
       }(i)
   }

   wg.Wait() // Wait for all goroutines to finish
   ```

2. **Mutexes**: A `sync.Mutex` is used to ensure that only one goroutine can access a piece of code or data at a time. This prevents race conditions and ensures that data is not corrupted by concurrent access.

   ```go
   var mu sync.Mutex
   var count int

   for i := 0; i < 5; i++ {
       go func() {
           mu.Lock()
           // Only one goroutine can access this at a time
           count++
           mu.Unlock()
       }()
   }
   ```

3. **Channels**: Channels are a built-in way to communicate between goroutines. They can be used for signaling and passing data. You can use channels to synchronize goroutines by sending and receiving messages.

   ```go
   done := make(chan bool)

   go func() {
       // Do some work
       done <- true // Signal that work is done
   }()

   <-done // Wait for the signal
   ```

4. **Condition Variables**: A `sync.Cond` can be used for signaling between goroutines, allowing one or more goroutines to wait for an event before continuing execution.

   ```go
   var mu sync.Mutex
   cond := sync.NewCond(&mu)

   go func() {
       mu.Lock()
       // Wait for the condition to be signaled
       cond.Wait()
       mu.Unlock()
       // Do work after the condition is met
   }()

   // Signal the condition
   mu.Lock()
   cond.Signal()
   mu.Unlock()
   ```

5. **Once**: A `sync.Once` is used to ensure that a piece of code is only executed once, regardless of how many goroutines reach it. This is useful for initialization that should only happen once.

   ```go
   var once sync.Once

   initFunc := func() {
       // Initialization code here
   }

   for i := 0; i < 5; i++ {
       go func() {
           once.Do(initFunc)
       }()
   }
   ```

6. **Semaphores**: While not directly provided by the `sync` package, semaphores can be implemented using buffered channels to control access to a fixed number of resources.

   ```go
   var sem = make(chan struct{}, 3) // Semaphore with 3 slots

   for i := 0; i < 10; i++ {
       go func(i int) {
           sem <- struct{}{} // Acquire a slot
           // Do work
           <-sem // Release the slot
       }(i)
   }
   ```

These synchronization techniques can be used individually or in combination, depending on the requirements of your concurrent program. It's important to choose the right mechanism for the task to avoid common concurrency issues like deadlocks, race conditions, and livelocks.