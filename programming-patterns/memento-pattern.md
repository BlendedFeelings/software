---
b: https://blendedfeelings.com/software/programming-patterns/memento-pattern.md
---

# Memento pattern
is a software design pattern that provides the ability to restore an object to its previous state (undo via rollback). The pattern is used to implement the concept of undo operations in software systems, allowing for the capture and externalization of an object's internal state without violating encapsulation.

Here's how the Memento pattern works:

**Originator**: This is the object whose state needs to be saved and restored. It creates a memento containing a snapshot of its current internal state and can also use the memento to restore its internal state to the saved state.

**Memento**: This is a value object that acts as a snapshot of the Originator's state. It stores the internal state of the Originator as it was at a particular point in time. The Memento must be immutable once it's created to ensure the integrity of the saved state.

**Caretaker**: This object is responsible for the lifecycle of the memento. It can request a memento from the Originator to save the current state and can pass the memento back to the Originator when an undo operation is requested. The Caretaker doesn't operate on or examine the contents of the memento.

```java
// Define the Memento class
class Memento {
    private String state;

    public Memento(String state) {
        this.state = state;
    }

    public String getState() {
        return state;
    }
}

// Define the Originator class
class Originator {
    private String state;

    public void setState(String state) {
        this.state = state;
    }

    public Memento createMemento() {
        return new Memento(state);
    }

    public void restoreMemento(Memento memento) {
        state = memento.getState();
    }
}

// Define the Caretaker class
class Caretaker {
    private List<Memento> mementos = new ArrayList<>();

    public void addMemento(Memento memento) {
        mementos.add(memento);
    }

    public Memento getMemento(int index) {
        return mementos.get(index);
    }
}

// Uage
Originator originator = new Originator();
Caretaker caretaker = new Caretaker();

originator.setState("state1");
caretaker.addMemento(originator.createMemento());

originator.setState("state2");
caretaker.addMemento(originator.createMemento());

originator.restoreMemento(caretaker.getMemento(0));

```