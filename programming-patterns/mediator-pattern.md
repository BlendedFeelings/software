---
b: https://blendedfeelings.com/software/programming-patterns/mediator-pattern.md
---

# Mediator Pattern
allows objects to communicate with each other through a central mediator object, rather than directly communicating with each other. This central mediator object acts as a middleman to manage the interaction between objects, reducing the coupling between them and making the system more flexible and easier to maintain.

Here's how the Mediator Pattern works:

**Components**: Instead of interacting with each other directly, components (also known as colleagues) interact with a mediator object.
**Mediator Interface**: This defines the interface for communication with components.
**Concrete Mediator**: Implements the mediator interface and coordinates communication between components. It knows about all of the components and their methods and facilitates the interactions between them.
**Communication**: When a component needs to talk to another component, it sends a message to the mediator instead of communicating directly with the other component. The mediator then decides how to pass these messages and to which components.

```java
// Define the Mediator interface
interface Mediator {
    void notify(Component sender, String event);
}

// Define the Component abstract class
abstract class Component {
    protected Mediator mediator;

    public Component(Mediator mediator) {
        this.mediator = mediator;
    }

    public void send(String event) {
        mediator.notify(this, event);
    }

    public abstract void receive(String event);
}

// Define the ConcreteComponent classes
class ConcreteComponentA extends Component {
    public ConcreteComponentA(Mediator mediator) {
        super(mediator);
    }

    public void receive(String event) {
        // Implementation of ConcreteComponentA's receive method
    }
}

class ConcreteComponentB extends Component {
    public ConcreteComponentB(Mediator mediator) {
        super(mediator);
    }

    public void receive(String event) {
        // Implementation of ConcreteComponentB's receive method
    }
}

// Define the ConcreteMediator class
class ConcreteMediator implements Mediator {
    private ConcreteComponentA componentA;
    private ConcreteComponentB componentB;

    public void setComponentA(ConcreteComponentA componentA) {
        this.componentA = componentA;
    }

    public void setComponentB(ConcreteComponentB componentB) {
        this.componentB = componentB;
    }

    public void notify(Component sender, String event) {
        if (sender == componentA) {
            componentB.receive(event);
        } else if (sender == componentB) {
            componentA.receive(event);
        }
    }
}

// Example usage
ConcreteMediator mediator = new ConcreteMediator();
ConcreteComponentA componentA = new ConcreteComponentA(mediator);
ConcreteComponentB componentB = new ConcreteComponentB(mediator);
mediator.setComponentA(componentA);
mediator.setComponentB(componentB);

componentA.send("event1");
componentB.send("event2");

```