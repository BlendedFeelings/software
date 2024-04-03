---
b: https://blendedfeelings.com/software/programming-patterns/double-checked-locking-pattern.md
---

# Double-Checked Locking
is a software design pattern used to reduce the overhead of acquiring a lock by testing the locking criterion (the 'lock hint') before acquiring the lock. It is typically used to improve performance when implementing lazy initialization in a multithreaded environment, particularly when the overhead of acquiring a lock every time an instance is requested is considered high.

The pattern is called "double-checked" because there are two checks for the resource's initialization:

The first check is without the overhead of acquiring the lock. If the resource is already initialized, it returns the resource immediately.
If the resource is not initialized, a lock is obtained, and then the resource is checked again to make sure it hasn't been initialized by another thread while the current thread was waiting to acquire the lock.

```java
public class MyClass {
    Object instance;
    Lock lock = new Lock();
    Object GetInstance() {
        //first check
        if (instance == null) {
            lock.Acquire();
            //second check
            if (instance == null) {
                instance = new Singleton();
            }
            lock.Release();
        }
        return instance;
    }
}

```