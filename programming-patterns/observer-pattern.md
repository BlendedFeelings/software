---
b: https://blendedfeelings.com/software/programming-patterns/observer-pattern.md
---

# Observer Pattern
is a software design pattern that defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. This pattern is mainly used to implement distributed event handling systems, in a manner that is decoupled and efficient.

The Observer Pattern is typically implemented with two types of objects:

**Subject (Observable)**: This is the object that holds the state and sends notifications to observers when its state changes. It maintains a list of its observers and provides an interface for attaching and detaching observer objects.

**Observer**: This is the object that wishes to be notified when the state of the subject changes. Observers register themselves with the subject to receive updates.

Here's a conceptual overview of how the pattern works:

- The subject maintains a list of its observers and provides methods to add and remove observers from this list.
- The observer provides an update interface that is invoked when the subject's state changes.
- When the subject's state changes, it sends a notification to all its observers by calling their update method.
- The observers then can take the appropriate action in response to the state change.

```java
// Define the Subject interface
interface Subject {
    void attach(Observer observer);
    void detach(Observer observer);
    void notifyObservers();
}

// Define the Observer interface
interface Observer {
    void update(Subject subject);
}

// Define the ConcreteSubject class
class ConcreteSubject implements Subject {
    private List<Observer> observers = new ArrayList<>();
    private String state;

    public void attach(Observer observer) {
        observers.add(observer);
    }

    public void detach(Observer observer) {
        observers.remove(observer);
    }

    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(this);
        }
    }

    public void setState(String state) {
        this.state = state;
        notifyObservers();
    }

    public String getState() {
        return state;
    }
}

// Define the ConcreteObserver class
class ConcreteObserver implements Observer {
    private String name;

    public ConcreteObserver(String name) {
        this.name = name;
    }

    public void update(Subject subject) {
        System.out.println(name + " received update with state: " + ((ConcreteSubject) subject).getState());
    }
}

// Usage
ConcreteSubject subject = new ConcreteSubject();
ConcreteObserver observer1 = new ConcreteObserver("Observer1");
ConcreteObserver observer2 = new ConcreteObserver("Observer2");

subject.attach(observer1);
subject.attach(observer2);

subject.setState("state1");

subject.detach(observer2);

subject.setState("state2");

```