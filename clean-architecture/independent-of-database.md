---
b: https://blendedfeelings.com/software/clean-architecture/independent-of-database.md
---

# Independent of Database
in clean architecture emphasizes that the application's core business logic should not be tied to any specific database or persistence mechanism. This allows the underlying database technology to be changed without impacting the business rules and use cases of the application. Here are the key benefits and implementations of this principle:

### Benefits:

1. **Flexibility**: Being able to switch out the database without changing the business logic allows the application to adapt to different storage requirements, such as moving from a relational database to a NoSQL database if the need arises.

2. **Maintainability**: Decoupling the database from the business logic simplifies maintenance because changes to the database schema or the type of database used do not require changes to the business rules.

3. **Testability**: Independent database design makes it easier to write tests for the business logic without setting up a real database, which can be time-consuming and error-prone. Test doubles, like in-memory databases or mocks, can be used instead.

4. **Performance Optimization**: Different use cases might require different types of databases for optimal performance (e.g., read-heavy vs. write-heavy, need for transactions, etc.). Independence from a specific database allows for selecting the best tool for the job.

### Implementation:

To achieve database independence, the following architectural components and patterns are often used:

- **Entities**: These represent the domain objects or business entities and should not be concerned with database details.

- **Use Cases/Interactors**: These contain the application's business rules and interact with the entities. They should be able to operate without direct knowledge of how data is stored or retrieved.

- **Interface Adapters**: This layer includes Data Access Objects (DAOs) or repositories that provide an abstraction over data storage and retrieval mechanisms. They implement interfaces defined by the use cases.

- **Data Models**: Separate data models may be used for the persistence layer, which can be mapped to and from the business entities.

- **Dependency Inversion**: The core logic depends on abstractions (interfaces) rather than concrete implementations. Concrete implementations of these interfaces are provided at runtime, often using dependency injection.

- **Repository Pattern**: This pattern is commonly used to create an abstraction layer between the business logic and the data access layer. Repositories encapsulate all the logic needed to access data sources.

- **ORMs and Data Mappers**: Object-Relational Mapping (ORM) frameworks or custom data mappers can be used to translate between the database and the application's data models, further decoupling the business logic from the database schema.

By adhering to these practices, the application's core logic remains agnostic to the specifics of data persistence, which can be modified or replaced without necessitating changes to the business rules or the rest of the application. This architecture supports long-term sustainability and flexibility of the software system.