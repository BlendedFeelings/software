---
b: https://blendedfeelings.com/software/programming-patterns/immutable-object-pattern.md
---

# Immutable Object Pattern
is a design pattern in software engineering where an object, once created, cannot be changed. This means that its state is read-only after its construction, and any modifications to it would result in the creation of a new object rather than changes to the existing one.

Here are some key characteristics and benefits of using immutable objects:

**Thread Safety**: Immutable objects are naturally thread-safe since their state cannot change after construction, eliminating the need for synchronization when they are shared between threads.

**Consistency**: Since the state of an immutable object never changes, it is consistent and reliable throughout its lifetime, which can simplify programming logic and reduce the potential for errors.

**Safe Sharing**: Immutable objects can be shared freely without the need for defensive copies, as they cannot be modified by any code that has a reference to them.

**Caching**: Immutable objects are excellent candidates for caching since their hash code remains constant. This makes them suitable for use as keys in maps or elements in sets.

**Functional Programming**: Immutability is a core principle in functional programming languages and encourages a style of programming that relies on functions without side effects.

To implement an immutable object in a programming language like Java, you would:

Declare all fields final so they can only be assigned once.
Set all fields via the constructor.
Provide no setters or methods that modify the fields or state.
If the object holds references to mutable objects, ensure that these references are not exposed directly. Instead, provide access to copies or immutable views.

```java 
class Person {
    private final String name;
    private final int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}
```