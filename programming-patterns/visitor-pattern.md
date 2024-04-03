---
b: https://blendedfeelings.com/software/programming-patterns/visitor-pattern.md
---

# Visitor Pattern
is a design pattern used in object-oriented programming that allows you to add new operations to existing object structures without modifying the structures themselves. This is particularly useful when you have a complex object structure, like a composite tree, and you anticipate that operations on the structure might change or grow over time.

Here's how the Visitor pattern works:

1. **Element Interface**: This interface declares an `accept` method that takes a visitor object as an argument.
2. **Concrete Element**: These are classes that implement the Element interface and define the `accept` method. The `accept` method calls the visitor's `visit` method corresponding to the element's class.
3. **Visitor Interface**: This interface declares a set of `visit` methods for each type of concrete element in the object structure. These methods define the operation to be performed on the corresponding element.
4. **Concrete Visitor**: Classes that implement the Visitor interface and define the actual operations that need to be performed on elements of the object structure.

The key idea is that you can add new operations by creating new visitor classes without changing the classes of the elements on which it operates.

```java
// Define the interface for the visitor
interface Visitor {
    visit(Element element);
}

// Define the interface for the element
interface Element {
    accept(Visitor visitor);
}

// Define concrete elements
class ConcreteElement1 implements Element {
    accept(Visitor visitor) {
        visitor.visit(this);
    }
}

class ConcreteElement2 implements Element {
    accept(Visitor visitor) {
        visitor.visit(this);
    }
}

// Define concrete visitors
class ConcreteVisitor1 implements Visitor {
    visit(ConcreteElement1 element) {
        // Do something with ConcreteElement1
    }

    visit(ConcreteElement2 element) {
        // Do something with ConcreteElement2
    }
}

class ConcreteVisitor2 implements Visitor {
    visit(ConcreteElement1 element) {
        // Do something else with ConcreteElement1
    }

    visit(ConcreteElement2 element) {
        // Do something else with ConcreteElement2
    }
}

// Client code
Element[] elements = { new ConcreteElement1(), new ConcreteElement2() };
Visitor[] visitors = { new ConcreteVisitor1(), new ConcreteVisitor2() };

foreach (Element element in elements) {
    foreach (Visitor visitor in visitors) {
        element.accept(visitor);
    }
}

```