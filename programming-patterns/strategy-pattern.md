---
b: https://blendedfeelings.com/software/programming-patterns/strategy-pattern.md
---

# Strategy Pattern
is a behavioral design pattern that enables selecting an algorithm's runtime behavior among a family of algorithms. It defines a set of algorithms, encapsulates each one, and makes them interchangeable within that family. The strategy pattern lets the algorithm vary independently from clients that use it.

Here's a basic overview of how the Strategy Pattern works:

1. **Context**: This is the class that has a reference to a Strategy. It may define an interface that lets the Strategy access its data.
2. **Strategy Interface**: This defines a common interface for all supported algorithms. Context uses this interface to call the algorithm defined by a ConcreteStrategy.
3. **ConcreteStrategy**: These are classes that implement the Strategy interface; each represents a different algorithm or behavior.

The main advantage of the Strategy Pattern is that it enables the hot-swapping of algorithms or behaviors without changing the objects that use them, thus adhering to the open/closed principle.

```java
// Define the Strategy interface
interface Strategy {
    void execute();
}

// Define the ConcreteStrategy classes
class ConcreteStrategyA implements Strategy {
    public void execute() {
        // Implementation of ConcreteStrategyA's execute method
    }
}

class ConcreteStrategyB implements Strategy {
    public void execute() {
        // Implementation of ConcreteStrategyB's execute method
    }
}

// Define the Context class
class Context {
    private Strategy strategy;

    public Context(Strategy strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(Strategy strategy) {
        this.strategy = strategy;
    }

    public void executeStrategy() {
        strategy.execute();
    }
}

// Usage
Strategy strategyA = new ConcreteStrategyA();
Strategy strategyB = new ConcreteStrategyB();

Context context = new Context(strategyA);
context.executeStrategy();

context.setStrategy(strategyB);
context.executeStrategy();

```