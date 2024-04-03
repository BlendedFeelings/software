---
b: https://blendedfeelings.com/software/programming-patterns/proxy-pattern.md
---

# Proxy Pattern
is a structural pattern that provides an object that acts as a substitute or placeholder for another object. A proxy controls access to the original object, allowing it to perform tasks before or after the access to the object it represents. This can be useful for various reasons, such as controlling when a costly object should be instantiated, adding security around the actual object, or providing a simplified interface to a complex system.

The Proxy Pattern involves three main components:

1. **Subject**: This is an interface that defines the common operations for both the RealSubject and the Proxy. It allows a client to work with the RealSubject and its Proxy in a uniform way.

2. **RealSubject**: This is the real object that the Proxy represents. It contains the actual business logic or data that the client is interested in.

3. **Proxy**: This is the object that controls access to the RealSubject. It implements the same interface as the RealSubject and holds a reference to it. It can perform additional tasks such as lazy initialization, logging, access control, caching, etc., when the client makes a call to the RealSubject through the Proxy.

```java
// Define the interface for the subject
interface Subject {
    request();
}

// Define the concrete subject
class ConcreteSubject implements Subject {
    request() {
        // Do something
    }
}

// Define the proxy
class Proxy implements Subject {
    subject: Subject;

    request() {
        if (!this.subject) {
            this.subject = new ConcreteSubject();
        }

        // Do something before the request
        this.subject.request();
        // Do something after the request
    }
}

// Client code
let proxy = new Proxy();
proxy.request();
```