---
b: https://blendedfeelings.com/software/concurrent-programming/cooperative-cancellation.md
---

# Cooperative cancellation in concurrent programming 
is a design pattern that allows multiple threads or tasks to work together in a way that they can be cancelled at any point during their execution. This is particularly important in scenarios where tasks are long-running, and there might be a need to stop them before they complete, either due to user action, a change in application state, or the occurrence of an error.

The cooperative aspect of this pattern is key; it implies that the tasks or threads being cancelled are designed to periodically check for cancellation requests and then gracefully terminate their operation if such a request has been made. This is in contrast to preemptive cancellation, where the task is forcibly terminated by an external entity, which can lead to resource leaks or inconsistent state if not handled carefully.

Here's how cooperative cancellation can be implemented in various programming environments:

### .NET (C#)
In .NET, the `CancellationToken` and `CancellationTokenSource` classes are used to implement cooperative cancellation.

```csharp
using System;
using System.Threading;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        var cancellationTokenSource = new CancellationTokenSource();
        var token = cancellationTokenSource.Token;

        var task = LongRunningOperationAsync(token);

        // Cancel the operation after a delay
        cancellationTokenSource.CancelAfter(TimeSpan.FromSeconds(5));

        try
        {
            await task;
        }
        catch (OperationCanceledException)
        {
            Console.WriteLine("Operation was cancelled.");
        }
    }

    static async Task LongRunningOperationAsync(CancellationToken token)
    {
        for (int i = 0; i < 10; i++)
        {
            // Simulate work
            await Task.Delay(1000);

            // Check for cancellation
            token.ThrowIfCancellationRequested();
        }
    }
}
```

### Java
In Java, you can use the `Future` interface and `ExecutorService` to run tasks that can be cancelled.

```java
import java.util.concurrent.*;

public class CooperativeCancellationExample {
    public static void main(String[] args) throws InterruptedException {
        ExecutorService executor = Executors.newSingleThreadExecutor();
        Future<?> future = executor.submit(() -> {
            try {
                while (!Thread.currentThread().isInterrupted()) {
                    // Simulate work
                    Thread.sleep(1000);
                    System.out.println("Task is running");
                }
            } catch (InterruptedException e) {
                // Restore the interrupted status
                Thread.currentThread().interrupt();
            }
        });

        // Cancel the task after a delay
        Thread.sleep(5000);
        future.cancel(true); // true to interrupt if running

        executor.shutdownNow();
    }
}
```

### Python
In Python, you can use the `threading` module and `Event` objects for a similar effect.

```python
import threading
import time

def long_running_operation(stop_event):
    while not stop_event.is_set():
        print("Task is running")
        time.sleep(1)
    print("Task was cancelled")

stop_event = threading.Event()
thread = threading.Thread(target=long_running_operation, args=(stop_event,))
thread.start()

# Cancel the task after a delay
time.sleep(5)
stop_event.set()
thread.join()
```

### JavaScript (Node.js)
In JavaScript, especially in a Node.js environment, you can use promises with a cancellation token-like mechanism.

```javascript
let shouldCancel = false;

function longRunningOperation() {
    return new Promise((resolve, reject) => {
        const intervalId = setInterval(() => {
            if (shouldCancel) {
                clearInterval(intervalId);
                reject('Operation was cancelled');
            }
            console.log('Task is running');
        }, 1000);
    });
}

const promise = longRunningOperation();

// Cancel the task after a delay
setTimeout(() => {
    shouldCancel = true;
}, 5000);

promise.catch(error => console.log(error));
```

In each of these examples, the running task checks for a cancellation signal at regular intervals. If it detects that a cancellation has been requested, it stops its execution in a controlled manner. This allows resources to be freed up and ensures that the program can continue to run without issues related to the cancelled task.