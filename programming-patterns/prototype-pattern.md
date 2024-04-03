---
b: https://blendedfeelings.com/software/programming-patterns/prototype-pattern.md
---

# Prototype Pattern
is a creational design pattern used in software development. It is one of the patterns included in the "Gang of Four" design patterns. The Prototype Pattern is particularly useful when the creation of an object is costly or complex, and it is more efficient to copy an existing instance.

The main idea behind the Prototype Pattern is that you can create new objects by copying existing ones (prototypes) rather than creating new objects from scratch. This is achieved by implementing a prototype interface that tells objects to clone themselves. The pattern allows for adding any number of concrete prototypes at runtime.

Here's how the Prototype Pattern typically works:

1. **Prototype Interface**: This defines a method for cloning itself. Often this is simply called `clone()`.

2. **Concrete Prototype**: Classes that implement the Prototype interface and define the method to clone itself.

3. **Client**: The class that wants to create new objects. Instead of creating objects directly, it asks a prototype to clone itself.

In many programming languages, this pattern can be implemented using a shallow or deep copy, depending on whether the cloned object should share some of the original object's property references or not.

```java
// Define the interface for the prototype
interface Prototype {
    clone(): Prototype;
}

// Define a concrete prototype
class ConcretePrototype implements Prototype {
    field1: string;
    field2: number;

    constructor(field1: string, field2: number) {
        this.field1 = field1;
        this.field2 = field2;
    }

    clone(): Prototype {
        return new ConcretePrototype(this.field1, this.field2);
    }
}

// Client code
let prototype = new ConcretePrototype("field1", 123);
let clone1 = prototype.clone();
let clone2 = prototype.clone();
```