---
b: https://blendedfeelings.com/software/domain-driven-design/domain-driven-design.md
---

# Domain-Driven Design (DDD) 
is an approach to software development that focuses on creating software that reflects complex domain models and uses a common language between developers and domain experts to describe the solutions. It was introduced by Eric Evans in his book "Domain-Driven Design: Tackling Complexity in the Heart of Software."

Here are the key concepts and components of DDD:

1. **Ubiquitous Language**: A common vocabulary used by developers and domain experts to ensure clear communication and a shared understanding of the domain.

2. **Bounded Contexts**: These are logical boundaries within which a particular domain model is defined and applicable. Different bounded contexts can have different models for the same concept.

3. **Entities**: Objects that are defined not by their attributes, but by a thread of continuity and identity, like a person with a social security number.

4. **Value Objects**: Objects that are defined entirely by their attributes. They are immutable and are often used to measure, quantify, or describe things in the domain.

5. **Aggregates**: A cluster of domain objects that can be treated as a single unit for data changes. Each aggregate has a root entity, known as the Aggregate Root, which is the only object that outside objects are allowed to hold references to.

6. **Repositories**: These are used to retrieve domain objects from the database. They abstract the underlying data access technology and provide a collection-like interface for accessing domain objects.

7. **Domain Events**: These are significant business events that domain experts care about, which may trigger side effects within the domain.

8. **Services**: When an operation does not conceptually belong to any object, it can be defined as a service. Services are stateless and are typically used to perform operations that involve multiple domain objects.

9. **Factories**: These are used to create complex domain objects and ensure that the created objects are valid and in a consistent state.

10. **Strategic Design**: This is a high-level view of the system's design that focuses on the relationships between bounded contexts and their integration.

11. **Tactical Design**: This involves the application of patterns like Entities, Value Objects, Aggregates, Repositories, Domain Events, and Services in the context of individual bounded contexts.

12. **Context Mapping**: This is the process of identifying and making explicit the relationships and interactions between different bounded contexts within the system.

13. **Anti-Corruption Layer**: A layer that translates between different bounded contexts or systems, preventing unwanted dependencies and ensuring that the domain model remains clean.

14. **Specification Pattern**: A way to encapsulate business rules that determine whether or not a particular object satisfies certain criteria.

DDD is particularly useful in complex domains where the cost of misunderstanding the domain is high. It encourages deep understanding of the domain, continuous learning, and close collaboration between technical and domain experts. It is also well-suited for microservices architectures where bounded contexts can align with microservices boundaries.