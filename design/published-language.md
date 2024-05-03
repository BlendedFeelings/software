---
b: https://blendedfeelings.com/software/design/published-language.md
---

# Published Language 
refers to a language that is shared between different bounded contexts. A bounded context is a central pattern in DDD, defining the limits of a particular domain model. Within these contexts, the domain model and the Ubiquitous Language (the shared language used by developers and domain experts) are consistent and specific to that context.

However, when different bounded contexts need to communicate with each other or with external systems, they often do so through an interface that translates between the Ubiquitous Languages of each bounded context. This interface uses a Published Language, which is a language that has been specifically designed for inter-context communication.

The Published Language can take various forms, such as:

1. **API Contracts**: These are formal definitions of the services provided by a system, including the data structures, endpoints, and protocols used for communication.

2. **Integration Events**: These are events that are designed to be understood by multiple bounded contexts and can trigger behaviors or data synchronization between them.

3. **Data Transfer Objects (DTOs)**: These are objects that carry data between processes, and they often implement the Published Language to ensure that data is communicated in a form that is understood by both the sender and receiver contexts.

4. **Message Schemas**: These define the structure and types of messages exchanged between systems, ensuring that all parties involved can understand and process the messages correctly.

5. **Shared Kernel**: This is a shared subset of the domain model that different teams agree to use as a common foundation, minimizing the translation needed between different Ubiquitous Languages.

The Published Language is designed to be stable and well-documented so that it can be used reliably over time, even as individual bounded contexts evolve. It is also typically more formal and less rich than the Ubiquitous Language used within a single bounded context, because it needs to be more general to serve the needs of multiple contexts.