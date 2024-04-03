---
b: https://blendedfeelings.com/software/programming-patterns/aggregation-pattern.md
---

# Aggregation Patter
is a type of composition, where one object (the composite) contains one or more instances of another object (the component), and delegates some of its behavior to the component. It allows you to create complex object structures by combining simple objects in a recursive manner, while keeping the objects loosely coupled.

```java
// The component interface
interface Component {
    void operation();
}

// The leaf component
class Leaf implements Component {
    void operation() {
        // ...
    }
}

// The composite component
class Composite implements Component {
    private List<Component> children = new ArrayList<>();

    void add(Component component) {
        children.add(component);
    }

    void remove(Component component) {
        children.remove(component);
    }

    void operation() {
        for (Component child : children) {
            child.operation();
        }
    }
}

// Usage
Component leaf1 = new Leaf();
Component leaf2 = new Leaf();
Component composite1 = new Composite();
composite1.add(leaf1);
composite1.add(leaf2);
Component leaf3 = new Leaf();
Component composite2 = new Composite();
composite2.add(leaf3);
composite2.add(composite1);
composite2.operation();
```