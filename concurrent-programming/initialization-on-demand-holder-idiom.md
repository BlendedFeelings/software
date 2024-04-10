---
b: https://blendedfeelings.com/software/concurrent-programming/initialization-on-demand-holder-idiom.md
---

# Initialization-on-Demand Holder idiom 
is a design pattern used in Java to lazily initialize an instance of a class in a thread-safe way without the need for synchronization on the instance-level. It takes advantage of the Java language's guarantee that a class is only loaded and initialized when it is used for the first time.

Here's how the idiom works:

1. The class that we want to lazily initialize is kept with a static inner class (the holder class).
2. The inner class contains a static field with an instance of the class that we want to initialize.
3. The first call to the getInstance() method of the outer class leads to the loading and initialization of the inner class. This is when the instance is created.
4. Since class initialization is guaranteed to be sequential in Java, no further synchronization is necessary.

Below is an example of the Initialization-on-Demand Holder idiom:

```java
public class Singleton {
    // Private constructor prevents instantiation from other classes
    private Singleton() { }

    // This inner class is not loaded until the getInstance() method is called
    private static class LazyHolder {
        // The instance is created at the time of class loading
        private static final Singleton INSTANCE = new Singleton();
    }

    // Global access point
    public static Singleton getInstance() {
        // Only when this method is called, the LazyHolder class gets loaded and creates the Singleton instance
        return LazyHolder.INSTANCE;
    }
}
```

In this example, `Singleton` is the class that we want to instantiate lazily. The `LazyHolder` static inner class contains the `INSTANCE` of `Singleton`. The `getInstance()` method provides the global point of access to the `Singleton` instance and triggers the loading and initialization of the `LazyHolder` class, which in turn initializes the `INSTANCE`.

This idiom is a widely used approach to implementing singletons in Java, as it provides an efficient and thread-safe way to instantiate a class only when it is needed.