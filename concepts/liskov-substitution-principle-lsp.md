---
b: https://blendedfeelings.com/software/concepts/liskov-substitution-principle-lsp.md
---

# Liskov Substitution Principle (LSP) 
is the third of the five SOLID principles of object-oriented design and was introduced by Barbara Liskov in 1987. LSP states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program. In other words, subclasses should be substitutable for their base classes.

### Understanding LSP

LSP extends the concept of subtyping to object-oriented programming. It emphasizes that a subclass should not only inherit the interface of its base class but also its behavior. This means that the subclass should be able to process the same set of messages as the base class and satisfy the expectations of any client of the base class.

The principle defines two key properties that a subtype must satisfy in relation to its base type:

1. **Signature compatibility**: The subtype must adhere to the base type's interface, meaning methods must have the same name, return type, and parameter list.
2. **Behavioral compatibility**: The subtype must behave in a manner consistent with the behavior that clients of the base type expect. This includes:
   - Respecting any invariants of the base type.
   - Ensuring that any postconditions established by the base type's operations are also true for the subtype.
   - Maintaining the preconditions of the base type, meaning that the subtype should not require more strict conditions than the base type.

### Examples of LSP

Suppose you have a class `Bird` with a method `fly()`. If you have a subclass `Penguin` that inherits from `Bird`, it would inherit the `fly()` method. However, penguins cannot fly, so if a client of `Bird` calls `fly()` on an instance of `Penguin`, it would violate LSP because the behavior does not conform to the expectation set by the `Bird` class.

To adhere to LSP, you could refactor the design by creating a more general class, such as `Animal`, and separate interfaces for `FlyingBird` and `NonFlyingBird`. `Bird` would no longer have a `fly()` method, but `FlyingBird` would. Then, classes like `Eagle` would implement `FlyingBird`, and `Penguin` would implement `NonFlyingBird`.

### Applying LSP

To apply LSP, developers should:

- Ensure that subclasses do not weaken the base class's guarantees.
- Avoid overriding methods in a subclass in a way that changes the behavior expected by the clients of the base class.
- Use interfaces or abstract classes to define and enforce contracts for behavior.
- Consider the use of design by contract, where preconditions, postconditions, and invariants are explicitly defined.

Violating LSP can lead to code that is fragile and difficult to maintain, as it introduces the risk of runtime errors and unexpected behavior when subclasses are used in place of their base classes. By adhering to LSP, software becomes more modular and easier to understand, as the relationships between classes are more predictable and consistent.