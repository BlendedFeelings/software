---
b: https://blendedfeelings.com/software/programming-patterns/flyweight-pattern.md
---

# Flyweight Pattern
is a structural design pattern that is used to minimize memory usage and improve performance in situations where a large number of similar objects are used. It does this by sharing as much data as possible with related objects; the shared data is called the intrinsic state and is immutable, meaning that it does not change over the lifetime of the object.

The parts of the Flyweight pattern are:

**Flyweight**: This is the interface through which flyweights can receive and act on extrinsic states.
ConcreteFlyweight: Implements the Flyweight interface and stores intrinsic state. ConcreteFlyweights must be sharable and any state they store must be intrinsic, that is, independent of the flyweight's context.
UnsharedConcreteFlyweight: Not all Flyweight subclasses need to be shared. The Flyweight interface enables sharing; it doesn't enforce it. It's common for UnsharedConcreteFlyweight objects to have ConcreteFlyweight objects as children at some level in the flyweight object structure.
Flyweight Factory: Manages flyweight objects and creates them too. It ensures that flyweights are shared properly. When a client requests a flyweight, the Flyweight Factory object supplies an existing instance or creates one, if none exists.

**Client**: Maintains a reference to flyweights in addition to computing and storing the extrinsic state of flyweights.
The pattern is often used when dealing with large numbers of objects that have some shared state. For instance, in a word processor, rather than creating an object for each character in a document, a flyweight can be used to minimize the number of objects created.

```java
// Define the Flyweight interface
interface Flyweight {
    void operation();
}

// Define the ConcreteFlyweight class
class ConcreteFlyweight implements Flyweight {
    private String intrinsicState;

    public ConcreteFlyweight(String intrinsicState) {
        this.intrinsicState = intrinsicState;
    }

    public void operation() {
        // Implementation of ConcreteFlyweight's operation
    }
}

// Define the FlyweightFactory class
class FlyweightFactory {
    private Map<String, Flyweight> flyweights = new HashMap<>();

    // Factory method that returns a Flyweight object
    public Flyweight getFlyweight(String intrinsicState) {
        if (!flyweights.containsKey(intrinsicState)) {
            flyweights.put(intrinsicState, new ConcreteFlyweight(intrinsicState));
        }
        return flyweights.get(intrinsicState);
    }
}

// Usage
FlyweightFactory factory = new FlyweightFactory();
Flyweight flyweight1 = factory.getFlyweight("state1");
Flyweight flyweight2 = factory.getFlyweight("state2");
print(flyweight1 == flyweight2) //true, are the same objects
```