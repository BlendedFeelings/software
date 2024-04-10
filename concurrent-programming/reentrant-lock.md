# Reentrant lock 
also known as a recursive lock, is a synchronization primitive that can be acquired multiple times by the same thread without causing a deadlock. This kind of lock keeps track of the number of times it has been locked, and requires the same number of unlocks to be completely released.

The main feature of a reentrant lock is that it allows the thread that holds the lock to reacquire it without blocking. This is useful in scenarios where a synchronized method or block of code calls another synchronized method that requires the same lock.

Here's an example of how a reentrant lock might be used in Java:

```java
import java.util.concurrent.locks.ReentrantLock;

public class Example {
    private final ReentrantLock lock = new ReentrantLock();

    public void methodOne() {
        lock.lock();
        try {
            // Critical section
            methodTwo(); // This method also requires the same lock
        } finally {
            lock.unlock();
        }
    }

    public void methodTwo() {
        lock.lock();
        try {
            // Another critical section
        } finally {
            lock.unlock();
        }
    }
}
```

In the example above, when `methodOne` is called, it acquires the lock. Then it calls `methodTwo`, which also acquires the lock. Since the lock is reentrant, the same thread can acquire it again without getting blocked. When `methodTwo` completes, it releases the lock once, but the lock is not fully released until `methodOne` also releases it.

Reentrant locks often provide additional features, such as the ability to check if the lock is held, attempt to acquire the lock without blocking, and interruptibly acquire the lock. In Java, the `ReentrantLock` class in the `java.util.concurrent.locks` package provides such functionality.