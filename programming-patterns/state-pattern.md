---
b: https://blendedfeelings.com/software/programming-patterns/state-pattern.md
---

# State Pattern
is a behavioral design pattern that allows an object to alter its behavior when its internal state changes. This pattern is used to encapsulate varying behavior for the same object, based on its internal state. This can be a cleaner way for an object to change its behavior at runtime without resorting to large monolithic conditional statements and thus improve maintainability.

The State Pattern is typically implemented by creating a context class that has a reference to a state object representing the current state of the system, and a state interface or abstract class that defines the methods that all concrete state classes should implement.

Here's a conceptual breakdown of the State Pattern:

1. **State Interface/Abstract Class**: This defines the common interface for all states, declaring methods for handling various requests, which will be implemented by the concrete state classes.

2. **Concrete State Classes**: These classes implement the behaviors associated with a state of the context. Each class represents a different state.

3. **Context Class**: This class maintains an instance of a concrete state subclass that defines the current state. The context delegates the request from the client to the current state object to handle.

4. **Client**: The client interacts with the context class. The client may trigger state transitions by calling methods on the context.


```java
// Define the State interface
interface State {
    void handle();
}

// Define the ConcreteState classes
class ConcreteStateA implements State {
    public void handle() {
        // Implementation of ConcreteStateA's handle method
    }
}

class ConcreteStateB implements State {
    public void handle() {
        // Implementation of ConcreteStateB's handle method
    }
}

// Define the Context class
class Context {
    private State state;

    public void setState(State state) {
        this.state = state;
    }

    public void handle() {
        state.handle();
    }
}

// Example usage
State stateA = new ConcreteStateA();
State stateB = new ConcreteStateB();

Context context = new Context();
context.setState(stateA);
context.handle();

context.setState(stateB);
context.handle();

```