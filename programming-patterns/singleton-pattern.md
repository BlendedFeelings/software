---
b: https://blendedfeelings.com/software/programming-patterns/singleton-pattern.md
---

# Singleton pattern
is a software design pattern that ensures a class has only one instance and provides a global point of access to that instance. It is often used when exactly one object is needed to coordinate actions across the system, such as a configuration manager or a connection pool.

Here's how the Singleton pattern is typically implemented:

1. **Make the constructor private** to prevent direct construction calls with the `new` operator.
2. **Create a static method** that acts as a constructor. This method calls the constructor to create an instance if one doesn't exist or returns the reference to the existing instance.
3. **Store the single instance** in a static field within the class.
4. **Ensure that the class is thread-safe**, so that concurrent threads can't create multiple instances. This can be done by locking, lazy initialization, or other synchronization mechanisms.
5. Optionally, **prevent instance cloning** to ensure that cloning the instance does not create a new instance.
6. Optionally, **prevent deserialization** from creating a new instance if the class is serializable.


```java
// Define the Singleton class
class Singleton {
    private static Singleton instance;

    // Private constructor to prevent instantiation from outside the class
    private Singleton() {}

    // Public static method that returns the Singleton instance
    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }

    // Public method that can be called on the Singleton instance
    public void someMethod() {
        // Implementation of someMethod
    }
}

// Example usage
Singleton singleton = Singleton.getInstance();
singleton.someMethod();

```