---
b: https://blendedfeelings.com/software/clean-architecture/independent-of-frameworks.md
---

# Independent of Frameworks
in the context of clean architecture is about designing the software in such a way that it does not rely heavily on any specific frameworks or libraries for its core functionality. This principle has several important implications:

1. **Framework as a Tool**: The software uses the framework as a tool, rather than being constrained by it. The framework should serve the application, not the other way around. This means that the application's core logic should be able to function without the framework if necessary.

2. **Reduced Coupling**: By keeping the core logic independent of frameworks, the coupling between the application and the framework is reduced. This makes the application more resilient to changes in the framework, such as updates or deprecations.

3. **Portability**: An application that is not tightly coupled to a specific framework is more portable. If needed, it can be more easily adapted to work with a different framework or moved to a different environment that does not support the original framework.

4. **Testability**: When the core logic is independent of the framework, it is easier to write tests for that logic without having to instantiate the framework or mock out large parts of it. This leads to faster and more reliable tests.

5. **Flexibility**: Framework independence allows developers to choose the best tools for the job at hand, rather than being forced to use whatever tools the framework provides. It also makes it easier to replace or update those tools as better options become available.

6. **Focus on Business Logic**: By separating the core business logic from the framework, developers can focus on implementing the business rules and use cases without getting distracted by the framework-specific details.

To achieve framework independence, developers typically:

- Use abstractions such as interfaces or abstract classes to define how the application interacts with frameworks or external libraries.
- Implement these abstractions with concrete classes that are specific to the framework or library being used.
- Use dependency injection to provide the concrete implementations to the application's core logic, which only knows about the abstractions.

This approach ensures that the application's core logic remains untouched when changes are made to the framework-specific code, and it allows for greater flexibility and maintainability of the software system.