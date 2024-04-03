---
b: https://blendedfeelings.com/software/concepts/single-responsibility-principle-srp.md
---

# Single Responsibility Principle (SRP) 
is one of the five SOLID principles of object-oriented design, which were introduced by Robert C. Martin. SRP states that a class should have only one reason to change, meaning it should have only one job or responsibility.

### Understanding SRP

The idea behind the Single Responsibility Principle is that a class should not be overloaded with multiple responsibilities. Instead, each responsibility should be encapsulated in its own class. This leads to several benefits:

- **Maintainability**: It's easier to maintain and modify code that has a clear and single focus.
- **Testability**: Classes with a single responsibility are easier to test because there are fewer dependencies and less context to deal with.
- **Reusability**: Single-responsibility classes can often be reused in other parts of the codebase without modification, as they represent a single, coherent functionality.
- **Lower Coupling**: SRP reduces the interdependencies between classes, leading to a more decoupled and flexible codebase.

### Examples of SRP

Consider a class that manages user information in a system. According to SRP, this class should only handle data related to the user. If the same class is also responsible for persisting user data to a database and sending notifications to the user, it is violating SRP because these are separate concerns.

To adhere to SRP, you would refactor this hypothetical class into three separate classes:

1. `User` - Manages user information and business logic related to users.
2. `UserRepository` - Handles persistence logic, such as saving and retrieving user data from a database.
3. `UserNotificationService` - Manages the logic for sending notifications to users.

### Applying SRP

When applying SRP, it's essential to identify the axes of change, which are the reasons a class might need to be modified. If a class has more than one axis of change, it likely has more than one responsibility and should be refactored.

It's also important to note that what constitutes a single responsibility can sometimes be subjective and dependent on the context of the application. A responsibility is often defined in terms of business logic or user requirements, and it's crucial to have a clear understanding of these to apply SRP effectively.

In summary, SRP is about ensuring that a class or module has one, and only one, reason to change by focusing on a single concern or functionality. This principle is foundational for creating a codebase that is easier to maintain, understand, and extend.