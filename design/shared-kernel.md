---
b: https://blendedfeelings.com/software/design/shared-kernel.md
---

# Shared Kernel 
is a concept that refers to a common subset of the domain model that is shared between multiple bounded contexts. A bounded context is a clear boundary within which a particular domain model is defined and applicable. The bounded context defines the linguistic and conceptual limits of a sub-domain.

The Shared Kernel has several important characteristics:

1. **Common Ground**: It contains the shared domain model elements, such as entities, value objects, services, and domain events, that are common to multiple bounded contexts.

2. **Ownership**: Despite being shared, the Shared Kernel is typically owned by a specific team, which is responsible for its integrity and evolution. However, changes to the Shared Kernel must be negotiated and agreed upon by all teams that use it.

3. **Integration**: The Shared Kernel facilitates integration between different bounded contexts by providing a common language and understanding.

4. **Minimality**: It should be as minimal as possible to reduce coupling between bounded contexts. The less you share, the more freedom teams have to evolve their contexts independently.

5. **Contract**: The Shared Kernel is effectively a contract between teams. Changes to the Shared Kernel should be carefully managed, as they can impact all teams that rely on it.

6. **Documentation**: It is important to have good documentation for the Shared Kernel, so that all teams understand how to use it and what guarantees it provides.

7. **Versioning**: Like any shared library, the Shared Kernel should be versioned. This allows teams to upgrade their usage of the Shared Kernel on their own schedules.

The Shared Kernel is a strategic design decision in DDD that requires careful consideration. It can be a powerful tool for integration but can also introduce tight coupling if not managed properly. When using a Shared Kernel, it's important to balance the benefits of standardization against the need for autonomy and loose coupling between bounded contexts.