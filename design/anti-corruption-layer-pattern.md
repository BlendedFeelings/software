---
b: https://blendedfeelings.com/software/design/anti-corruption-layer-pattern.md
---

# Anti-Corruption Layer (ACL) pattern 
is a concept in software architecture that acts as a barrier between two systems (or subsystems) to prevent one system's changes or lower-quality design from corrupting the other. It is particularly useful in scenarios where you're integrating a new system with an old one, or when dealing with third-party systems or legacy systems that you cannot or do not want to change.

The ACL serves as a translator or adapter that converts data and requests between the two systems. It ensures that the client system does not have to deal with the server system's internal model or logic directly. By doing so, the ACL helps to maintain the integrity and the bounded context of the client system's domain model.

Here are some key points about the Anti-Corruption Layer pattern:

1. **Translation**: The ACL translates data structures and operations from the format and semantics of one system to those of another. This can include transforming data formats, adapting interface calls, or even encapsulating complex legacy logic.

2. **Isolation**: By isolating the two systems, the ACL ensures that changes in one system do not have unintended side effects on the other. This is important when dealing with legacy systems that may not be well-documented or when the cost of modifying such systems is prohibitive.

3. **Bounded Context**: In Domain-Driven Design (DDD), the concept of a bounded context refers to the clear boundaries within which a particular domain model is defined and applicable. The ACL helps maintain these boundaries by not allowing foreign concepts or models to leak into the client system.

4. **Facilitating Evolution**: When you want to evolve or refactor one system without affecting its consumers, an ACL can provide the necessary decoupling. This allows for independent lifecycles of the systems involved.

5. **Integration Interface**: The ACL can expose a well-defined API that is designed according to the client system's needs, rather than forcing the client to conform to the server system's API.

6. **Complexity Management**: The ACL can encapsulate the complexity of the system it's protecting against, providing a simplified interface to the client system. This can make the client system easier to develop and maintain.

Implementing an Anti-Corruption Layer can be done through various technical means, such as:

- **Facades**: Creating a simplified interface that hides the complexity of the legacy system.
- **Adapters**: Converting data and calls from one system's interface to another's.
- **Gateways**: Acting as a point of entry that channels and possibly enriches communication between systems.
- **Translators**: Converting data between different representations or data models.

It's important to note that while the ACL can help manage complexity and protect the integrity of systems, it also introduces an additional layer that needs to be developed and maintained. Therefore, it should be used judiciously when the benefits outweigh the overhead.