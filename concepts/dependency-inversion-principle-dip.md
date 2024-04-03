---
b: https://blendedfeelings.com/software/concepts/dependency-inversion-principle-dip.md
---

# Dependency Inversion Principle (DIP) 
is the last of the five SOLID principles of object-oriented design, and it was introduced by Robert C. Martin. DIP is about decoupling software modules so that instead of high-level modules depending on low-level modules, both will depend on abstractions. Additionally, these abstractions should not depend on details; rather, details should depend on abstractions.

### Understanding DIP

DIP addresses the issue of rigidity in software systems by inverting the typical dependency relationship between high-level and low-level modules. In traditional programming, high-level modules (which provide complex logic) are often directly dependent on low-level modules (which provide utility features). This can make the system hard to change and evolve because a change in a low-level module can affect the high-level modules that depend on it.

The principle consists of two key points:

1. **High-level modules should not depend on low-level modules. Both should depend on abstractions.**
   - This means that the core functionality of your application should not be dependent on details like data access or third-party libraries. Instead, it should depend on interfaces or abstract classes that define contracts or behaviors.

2. **Abstractions should not depend on details. Details should depend on abstractions.**
   - The interfaces or abstract classes should not be concerned with the details of their implementations. Instead, it's the implementations that should be designed to fulfill the requirements of the interface or abstract class.

### Examples of DIP

Consider a shopping cart application that directly uses a `MySQLDatabase` class to store data. This is a violation of DIP because the high-level shopping cart logic is directly dependent on a low-level MySQL database implementation.

To adhere to DIP, you would define an interface, such as `IDatabase`, that includes methods for data storage and retrieval. The `MySQLDatabase` class would then implement this interface. The shopping cart would depend on the `IDatabase` interface, not on the concrete `MySQLDatabase` class. This way, if you decide to switch to a different database technology in the future, you can create a new implementation of `IDatabase` without having to change the shopping cart code.

### Applying DIP

To apply DIP, developers should:

- Use interfaces or abstract classes to define the contracts between different parts of the application.
- Inject dependencies through constructors, methods, or properties rather than hard-coding them inside high-level modules.
- Utilize dependency injection containers or frameworks to manage the creation and binding of concrete implementations to abstractions.

By following DIP, you create a system where the high-level policy-making parts of the system are insulated from changes to the low-level parts that provide utility features. This leads to a more flexible and maintainable codebase where modules can be easily interchanged and updated as needed.