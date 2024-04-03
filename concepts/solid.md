---
b: https://blendedfeelings.com/software/concepts/solid.md
---

# SOLID principles 
are a set of five design principles in object-oriented programming that, when combined, make it more likely that a developer will create a system that is easy to maintain and extend over time. These principles were promoted by Robert C. Martin and are part of the agile or adaptive software development movement.

The acronym SOLID stands for:

1. **S**ingle Responsibility Principle (SRP)
   - A class should have one, and only one, reason to change, meaning it should have only one job or responsibility.

2. **O**pen/Closed Principle (OCP)
   - Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification. This means that the behavior of a module can be extended without modifying its source code.

3. **L**iskov Substitution Principle (LSP)
   - Objects in a program should be replaceable with instances of their subtypes without altering the correctness of the program. Subtypes must be completely substitutable for their base types.

4. **I**nterface Segregation Principle (ISP)
   - No client should be forced to depend on methods it does not use. Instead of one fat interface, numerous smaller interfaces are preferred based on groups of methods, each one serving one submodule.

5. **D**ependency Inversion Principle (DIP)
   - High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions.

### Benefits of SOLID Principles

Following the SOLID principles can provide several benefits:

- **Maintainability**: Code that adheres to SOLID principles is typically easier to maintain. Changes in one part of the system have minimal impact on other parts.
- **Scalability**: Systems designed with SOLID principles in mind are more likely to be scalable, allowing for the addition of new features with less risk of breaking existing functionality.
- **Reusability**: The principles encourage the development of more granular components, which can be reused in different contexts.
- **Testability**: SOLID principles lead to a decoupled architecture, which tends to be easier to test due to the reduced dependencies between components.
- **Flexibility**: A system built with SOLID principles can be more easily adapted to changes in business requirements or technology.

### Applying SOLID Principles

Applying SOLID principles often involves a trade-off between the complexity of the code and the benefits of maintainability and flexibility. It's important for developers to understand these principles and apply them judiciously, considering the specific context and requirements of the project they are working on.

In practice, the SOLID principles are interrelated and often complement each other. For instance, applying SRP and ISP can make it easier to follow OCP, and DIP can facilitate both OCP and LSP. As with any set of guidelines, they should not be followed dogmatically; instead, they should be used as a guide to making informed design decisions.