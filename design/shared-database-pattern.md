---
b: https://blendedfeelings.com/software/design/shared-database-pattern.md
---

# Shared Database pattern 
in software architecture refers to a design where multiple applications or services have access to the same database. This pattern is one of the simplest ways to integrate data among different parts of a software system.

Related: [Microservices](microservices-architecture-pattern.md), [Saga](saga-pattern.md), [Database per Service](database-per-service-pattern.md)

Here are some characteristics and considerations for the Shared Database pattern:

Characteristics:

1. **Centralized Data Storage**: All applications store and retrieve data from a single database.
2. **Consistent Data Model**: The database schema is shared, and therefore, the data model is consistent across all applications.
3. **Direct Data Access**: Applications access the database directly using SQL queries or through a database access layer.
4. **Simplified Deployment**: Since there is only one database, deployment is simplified in terms of managing data storage.
5. **Immediate Consistency**: Changes made by one application are immediately visible to all other applications using the database.

Advantages:

1. **Data Consistency**: Ensures that all applications are working with the same set of data, which can enhance data integrity.
2. **Reduced Duplication**: Since data is stored in a central location, there is no need for data duplication across systems.
3. **Simplified Integration**: Integrating multiple systems is easier because they all use the same database schema.

Disadvantages:

1. **Tight Coupling**: Applications are tightly coupled to the database schema, making it difficult to change the schema without affecting all connected applications.
2. **Scalability Issues**: The database can become a bottleneck as the number of applications or the volume of data grows.
3. **Risk of Single Point of Failure**: If the database goes down, all applications relying on it are affected.
4. **Concurrency and Locking**: With many applications accessing the same database, concurrency and locking can become significant issues.
5. **Security Concerns**: Having a single database accessed by multiple applications can lead to complex security management.

Use Cases:

The Shared Database pattern is often used in scenarios where applications are tightly related and require constant, consistent access to the same data set, such as:

- Enterprise applications within the same organization that need to share customer, product, or employee data.
- Microservices architecture where the services are not highly decoupled, and integration is more important than independence.
- Legacy systems integration where creating separate databases for each application is not feasible.

Alternatives:

To address some of the disadvantages of the Shared Database pattern, alternative patterns like Database per Service, Event Sourcing, or Command Query Responsibility Segregation (CQRS) can be considered. These patterns aim to reduce tight coupling, improve scalability, and enhance the overall resilience of the system.

In conclusion, the Shared Database pattern can be effective for certain types of applications and integration needs, but it's important to be aware of the potential drawbacks, especially when designing systems that require high scalability, flexibility, and independence between components.