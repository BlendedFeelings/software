---
b: https://blendedfeelings.com/software/clean-architecture/independent-of-any-external-agency.md
---

# Independent of any external agency
in clean architecture extends the ideas of independence from frameworks, UI, and databases to all external systems and services. An external agency can be anything outside the application's core business logic, such as third-party APIs, microservices, file systems, network protocols, or hardware devices.

The goal of this principle is to ensure that the core business logic is not directly coupled to any external libraries, services, or systems. This allows the core logic to remain stable, testable, and maintainable, even as the external components evolve or are replaced.

### Benefits:

1. **Adaptability**: The application can adapt more easily to changes in external services or APIs without requiring changes to the business logic.

2. **Testability**: The core logic can be tested independently of any external services, which might be unreliable, slow, or difficult to set up for testing environments.

3. **Resilience**: The application is less vulnerable to changes or failures in external services, as these do not directly impact the core business logic.

4. **Interchangeability**: External services or components can be replaced with alternatives without affecting the rest of the system.

### Implementation:

To achieve independence from external agencies, the following architectural components and patterns are often used:

- **Entities**: The core business objects that encapsulate enterprise-wide business rules.

- **Use Cases/Interactors**: These capture application-specific business rules and orchestrate the flow of data between entities and external agencies.

- **Interface Adapters**: This layer includes adapters, gateways, and presenters that convert data between the format most convenient for use cases and entities and the format required by external agencies.

- **External Interfaces**: Define interfaces that represent the operations provided by external agencies, which the application might need to call.

- **Dependency Inversion**: The core logic depends on abstractions (interfaces) rather than concrete implementations of external services. Concrete implementations are provided at runtime, typically using dependency injection.

- **Service Locator Pattern**: An alternative to dependency injection, this pattern can be used to locate services at runtime, providing flexibility in service instantiation.

- **Anti-Corruption Layer (ACL)**: This is a layer that translates between the application's domain model and the external agency's model to prevent the external model from "corrupting" the internal model.

- **Adapter Pattern**: Used to convert the interface of an external agency into one that the application expects, allowing for easier integration and exchangeability.

By keeping the application's core logic independent of external agencies, developers ensure that the system's business rules are not affected by changes or issues in those external components. This leads to a more robust, flexible, and maintainable application.