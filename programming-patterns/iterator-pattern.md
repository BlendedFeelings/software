---
b: https://blendedfeelings.com/software/programming-patterns/iterator-pattern.md
---

# Iterator pattern
provides a way to access elements of a collection sequentially without exposing its underlying structure. It allows you to traverse through a collection of objects without having to know how the collection is implemented.

```java
// Define the Iterator interface
interface Iterator {
    boolean hasNext();
    Object next();
}

// Define the ConcreteIterator class
class ConcreteIterator implements Iterator {
    private Object[] items;
    private int position = 0;

    public ConcreteIterator(Object[] items) {
        this.items = items;
    }

    public boolean hasNext() {
        if (position >= items.length || items[position] == null) {
            return false;
        } else {
            return true;
        }
    }

    public Object next() {
        Object item = items[position];
        position++;
        return item;
    }
}

// Define the Aggregate interface
interface Aggregate {
    Iterator createIterator();
}

// Define the ConcreteAggregate class
class ConcreteAggregate implements Aggregate {
    private Object[] items;

    public ConcreteAggregate(Object[] items) {
        this.items = items;
    }

    public Iterator createIterator() {
        return new ConcreteIterator(items);
    }
}

// Usage
Object[] items = { "item1", "item2", "item3" };
Aggregate aggregate = new ConcreteAggregate(items);
Iterator iterator = aggregate.createIterator();

while (iterator.hasNext()) {
    Object item = iterator.next();
    // Do something with item
}

```