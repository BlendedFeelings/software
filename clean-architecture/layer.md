---
b: https://blendedfeelings.com/software/clean-architecture/layer.md
---

# Layers 
clean architecture organizes the software into distinct layers, each with its own responsibility and rules about how it can interact with other layers. These layers form a series of concentric circles, with the most stable and business-critical components at the center, and the details and components that are more likely to change at the outer edges. The layers, starting from the innermost to the outermost, are:

1. **Entities**: These are the core business objects of the application. They encapsulate enterprise-wide business rules and are the most stable part of the application. Entities are the least likely to change when something external changes, such as the UI or database.

2. **Use Cases (Interactors)**: This layer contains the application-specific business rules. Use cases orchestrate the flow of data to and from the entities and direct those entities to use their enterprise-wide business rules to achieve the goals of the use case. They represent the actions that can be taken with the entities.

3. **Interface Adapters**: This layer consists of adapters that convert data between the form that is most convenient for use cases and entities, and the form that is most convenient for some external agency such as a database or the web. It includes controllers, presenters, gateways, and repositories.

4. **Frameworks and Drivers**: This is the outermost layer and includes frameworks, tools, and drivers such as the database, web framework, UI framework, and any other external libraries or applications. This layer is kept separate from the rest of the application so that it can change without affecting the rest of the application.

### Dependency Rule

One of the key rules in clean architecture is the "Dependency Rule," which states that source code dependencies can only point inwards. Nothing in an inner circle can know anything at all about something in an outer circle. In particular, the name of something declared in an outer circle must not be mentioned by the code in an inner circle. That includes functions, classes. variables, or any other software entities.

By following this rule, the dependencies between layers are strictly controlled, which leads to a system that is more maintainable and adaptable to change. For example, the UI can change without changing the business rules, and the database can be swapped out without changing the use cases.

### Communication Across Layers

When a request from the external world comes into the system, it passes through the layers inwards, typically being transformed at each layer until it reaches the use cases. The response follows a similar path outwards, being transformed back into the form most convenient for the external agency (e.g., the user interface).

Each layer communicates with the layer directly inside it via interfaces or abstractions, ensuring that the inner layers remain independent of the outer layers. This allows for the construction of a system where the business logic is testable, the UI is flexible, the database is interchangeable, and external agencies can be easily integrated or replaced.