---
b: https://blendedfeelings.com/software/domain-driven-design/tactical-design.md
---

# Tactical Design 
in Domain-Driven Design (DDD) refers to the fine-grained approach to modeling and implementing the individual parts of a system based on its domain. It focuses on the details of the domain model and how to implement it in code. Tactical Design involves applying a set of patterns and practices to create a rich, expressive domain model that encapsulates business logic and rules.

Key concepts and patterns in Tactical Design include:

1. **Entities**: Objects that have a distinct identity that runs through time and different states. They are defined not just by their attributes but by a thread of continuity and identity.

2. **Value Objects**: Objects that are defined entirely by their attributes and are immutable. They have no conceptual identity and are often used to describe aspects of the domain.

3. **Aggregates**: A cluster of domain objects that can be treated as a single unit for the purpose of data changes. An Aggregate has an Aggregate Root, which is the only object that outside objects are allowed to hold references to.

4. **Repositories**: Abstractions that manage the retrieval and persistence of Aggregates or Entities from a data store, providing a collection-like interface for accessing domain objects.

5. **Domain Events**: Events that signify a state change within the domain that is of interest to the business or other parts of the system. They can be used to trigger side effects or integrate with other bounded contexts.

6. **Services**: When an operation does not conceptually belong to any object, it is defined as a Service. Services are stateless and are typically used to perform operations that involve multiple domain objects.

7. **Factories**: Methods or classes that handle the creation of complex domain objects, ensuring that they are created in a valid and consistent state.

8. **Specifications**: A pattern that encapsulates business rules that determine whether or not a particular object satisfies certain criteria.

Tactical Design is about the implementation details of the domain model within a bounded context. It helps developers create a model that is closely aligned with the business concepts and rules, ensuring that the software is both functional and understandable by domain experts.

Here's an overview of how these concepts might relate to each other in a DDD implementation:

- An **Aggregate** might be composed of several **Entities** and **Value Objects**, with one of the Entities acting as the **Aggregate Root**.
- A **Repository** would be used to retrieve and persist the **Aggregate** as a whole, treating it as a single unit.
- **Domain Events** might be raised from within an **Entity** or **Service** when something significant occurs (e.g., an Order is placed).
- A **Service** could orchestrate a complex process involving several **Entities** or **Aggregates** (e.g., processing a payment transaction).
- **Factories** would be responsible for creating instances of **Aggregates** or complex **Entities**, ensuring they are in a valid state upon creation.
- **Specifications** might be used within a **Repository** to encapsulate the criteria for finding particular **Entities** or **Aggregates**.

Tactical Design provides the tools and techniques necessary for developers to translate the strategic design into working software that effectively embodies the domain model. It ensures that the codebase is a faithful representation of the domain, with clear rules and logic that reflect the business's needs and priorities.