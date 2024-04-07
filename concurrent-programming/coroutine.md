---
b: https://blendedfeelings.com/software/concurrent-programming/coroutine.md
---

# Coroutines 
are a computer programming concept that generalizes subroutines for non-preemptive multitasking. They allow for multiple entry points for suspending and resuming execution at certain locations. Unlike subroutines, coroutines can exit by suspending execution and later resume from the point they were suspended. This makes them useful for tasks that can be paused and resumed, such as cooperative multitasking, concurrency, and asynchronous programming.

Also check: [Coroutine vs Subroutine](coroutine-vs-subroutine.md)

In the context of programming languages, coroutines are implemented in various ways:

1. **Generators/Yield-based Coroutines**: In languages like Python and JavaScript, the `yield` keyword is used to pause the execution of a function, turning it into a generator. Execution can later be resumed from the point where it yielded.

   Python example:
   ```python
   def simple_coroutine():
       print('Start of coroutine')
       yield 'Coroutine paused'
       print('End of coroutine')

   coro = simple_coroutine()
   next(coro)  # Starts the coroutine and prints 'Start of coroutine'
   next(coro)  # Resumes and finishes the coroutine, prints 'End of coroutine'
   ```

2. **Coroutine Libraries/Frameworks**: Some languages, like C# and Java, use libraries or frameworks to implement coroutines. In C#, the `async` and `await` keywords are used in conjunction with the Task Parallel Library for asynchronous programming.

   C# example:
   ```csharp
   async Task<string> GetDataAsync()
   {
       // Simulate an asynchronous operation
       await Task.Delay(1000);
       return "Data received";
   }
   ```

3. **Native Language Support**: Some newer languages, like Kotlin and Go, have built-in support for coroutines. Kotlin uses `suspend` functions, and Go uses goroutines with channels for communication.

   Kotlin example:
   ```kotlin
   suspend fun loadData(): Data {
       // Code to load data asynchronously
   }
   ```

   Go example:
   ```go
   func doSomething(c chan int) {
       // Perform some work and send a value on the channel
       c <- 42
   }

   func main() {
       c := make(chan int)
       go doSomething(c)
       result := <-c  // Receive the value from the channel
       fmt.Println(result)
   }
   ```

Coroutines are a powerful concept that allows for writing non-blocking and concurrent code in a more straightforward and readable manner. They are particularly useful in scenarios where tasks involve I/O-bound operations, such as web requests, file reading/writing, or any long-running computations that can be paused and resumed.