---
b: https://blendedfeelings.com/software/concurrency/active-object-pattern.md
---

# Active Object Pattern
is a concurrency pattern used in software engineering, which decouples method execution from method invocation for objects that each run in their own thread of control. The goal of the Active Object pattern is to introduce concurrency, by using asynchronous method invocation and a scheduler for handling requests.

Here's a breakdown of the key components in the Active Object pattern:

**Proxy**: This is the object that client code calls directly. It provides an interface that looks like the actual object's interface. When a method is called on the proxy, it doesn't execute the method but instead passes the request to the scheduler.

**Method Request**: This encapsulates all the information needed to call a method, including the method name, parameters, and the object instance on which the method will be called.

**Scheduler**: The scheduler maintains a queue of method requests. It decides which request to execute next based on a scheduling algorithm, which might involve priorities, FIFO ordering, or other criteria.

**Servant**: This is the actual object containing the business logic. It is only accessed by the Active Object's scheduler, which ensures that method calls are made safely from the correct thread.

**Future**: This object is returned immediately by the proxy to the caller. It acts as a placeholder for the result of the asynchronous method call. The client can use the future to query whether the computation is complete or to wait for the computation to finish and retrieve the result.

**Dispatcher**: In some implementations, the dispatcher handles the dispatching of method requests to the appropriate servant methods. It might be considered part of the scheduler or a separate component depending on the design.

The Active Object pattern is useful in scenarios where you want to avoid blocking the caller until the method execution is complete, especially in UI applications where responsiveness is critical. It's also used in distributed systems where operations might involve network latency.

```java
// ActiveObject interface
public interface ActiveObject {
    Future<String> doSomething(String message);
}

// Servant class that contains the actual business logic
public class Servant {
    public String doSomething(String message) {
        // Simulate some processing time
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        return "Processed: " + message;
    }
}

// Proxy class that submits tasks to the scheduler
public class Proxy implements ActiveObject {
    private final ExecutorService scheduler = Executors.newSingleThreadExecutor();
    private final Servant servant = new Servant();

    public Future<String> doSomething(String message) {
        return scheduler.submit(() -> servant.doSomething(message));
    }
}

// Example of how a client might use the ActiveObject
public class ActiveObjectDemo {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ActiveObject activeObject = new Proxy();

        // Asynchronously call the doSomething method
        Future<String> futureResult = activeObject.doSomething("Hello, World!");

        // Do other work while the method is being processed...

        // Retrieve the result of the asynchronous operation
        String result = futureResult.get(); // This call blocks until the result is available
        System.out.println(result);

        // Shut down the executor service
        if (activeObject instanceof Proxy) {
            ((Proxy) activeObject).shutdown();
        }
    }
}

```