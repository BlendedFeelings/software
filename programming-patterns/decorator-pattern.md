---
b: https://blendedfeelings.com/software/programming-patterns/decorator-pattern.md
---

# Decorator Pattern
is a structural design pattern that allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class. This pattern is particularly useful for adhering to the Open/Closed Principle, one of the SOLID principles of object-oriented design, which states that software entities should be open for extension but closed for modification.

The Decorator Pattern involves the following components:

**Component**: This is an interface or abstract class defining the operations that can be altered by decorators.

**ConcreteComponent**: A class that implements the Component interface or extends an abstract Component class. It represents the object to which additional responsibilities can be attached.

**Decorator**: An abstract class that implements the Component interface and has a reference to a Component object. It forwards requests to the Component object and may perform additional actions before or after forwarding.

**ConcreteDecorator**: Classes that extend the Decorator class. Each ConcreteDecorator adds its own behavior either before or after delegating the task to the Component object it decorates

```java
// Define the interface for the component
interface Component {
    operation();
}

// Define the concrete component
class ConcreteComponent implements Component {
    operation() {
        // Do something
    }
}

// Define the abstract decorator
abstract class Decorator implements Component {
    Component component;

    Decorator(Component component) {
        this.component = component;
    }

    operation() {
        component.operation();
    }
}

// Define concrete decorators
class ConcreteDecorator1 extends Decorator {
    ConcreteDecorator1(Component component) {
        super(component);
    }

    operation() {
        super.operation();
        // Do something extra
    }
}

class ConcreteDecorator2 extends Decorator {
    ConcreteDecorator2(Component component) {
        super(component);
    }

    operation() {
        super.operation();
        // Do something else extra
    }
}

// Client code
Component component = new ConcreteComponent();
component = new ConcreteDecorator1(component);
component = new ConcreteDecorator2(component);
component.operation();
```