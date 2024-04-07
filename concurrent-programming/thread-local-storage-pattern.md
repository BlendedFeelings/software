---
b: https://blendedfeelings.com/software/concurrent-programming/thread-local-storage-pattern.md
---

# Thread-Local Storage Pattern
is a design pattern used in concurrent programming to provide each thread with its own storage space for variables. This pattern is particularly useful when you want to avoid synchronization issues by not sharing data between threads, which can lead to race conditions, deadlocks, or other concurrency-related bugs.

Here's what you need to know about the TLS pattern:

- **Thread-Specific Data**: Each thread has its own separate instance of a variable or object. This means that the data is not shared among different threads, and each thread sees only its own data.
- **Avoids Synchronization**: Since each thread has its own copy of the data, there's no need for synchronization mechanisms like mutexes or locks when accessing that data. This can lead to more efficient multithreading.
- **Use Cases**: TLS is useful for situations where you need to maintain thread-specific state, such as user sessions in a web server or transaction contexts in a database system.


- **Language Support**: Many programming languages provide built-in support for TLS. For example, in Java, you can use `ThreadLocal<T>`; in C++, you can use the `thread_local` keyword; and in C#, you can use `ThreadStaticAttribute` or `ThreadLocal<T>`.
- **APIs and Libraries**: Some operating systems and libraries offer APIs to manage TLS. For example, POSIX threads (pthreads) have functions like `pthread_getspecific` and `pthread_setspecific`.

```java
public class MyThreadLocalClass {
    //variable is static in context of one thread
   static ThreadLocal<Integer> threadLocalVariable = new ThreadLocal<Integer>(0);

   void Increment() {
      threadLocalVariable.set(threadLocalVariable.get() + 1);
   }

   int GetValue() {
      return threadLocalVariable.get();
   }
}

```