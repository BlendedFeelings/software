---
b: https://blendedfeelings.com/software/programming-patterns/adapter-pattern.md
---

# Adapter Pattern
is a structural design pattern that allows objects with incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces. This pattern involves a single class, called an adapter, which is responsible for joining functionalities of independent or incompatible interfaces.

Here's a breakdown of the key components in the Adapter pattern:

**Client**: This is the class that wants to use a particular interface that it expects.

**Adaptee**: This is the class that has the functionality desired by the client but has an incompatible interface.

**Adapter**: This is the class that implements the expected interface and holds a reference to an instance of the Adaptee class. It translates calls from the interface into a form that the Adaptee understands.

```java
// Target interface that the client expects to use
interface Target {
    void request();
}

// Adaptee that needs to be adapted to the target interface
class Adaptee {
    void specificRequest() {
        // ...
    }
}

// Adapter that adapts the Adaptee to the Target interface
class Adapter implements Target {
    private Adaptee adaptee;

    Adapter(Adaptee adaptee) {
        this.adaptee = adaptee;
    }

    void request() {
        adaptee.specificRequest();
    }
}

// Client that uses the Target interface
class Client {
    void doSomething(Target target) {
        target.request();
    }
}

// Usage
Adaptee adaptee = new Adaptee();
Adapter adapter = new Adapter(adaptee);
Client client = new Client();
client.doSomething(adapter);
```