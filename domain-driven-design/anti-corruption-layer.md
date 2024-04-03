---
b: https://blendedfeelings.com/software/domain-driven-design/anti-corruption-layer.md
---

# Anti-Corruption Layer (ACL) 
is a concept in Domain-Driven Design (DDD) that refers to an isolation layer used to protect a domain model from being contaminated by another system's domain model. It acts as a translator between two bounded contexts or systems, allowing them to communicate with each other without compromising their respective models.

### Purpose of Anti-Corruption Layer:

1. **Protect Integrity**: The ACL protects the integrity of a bounded context's model by preventing foreign concepts from another context from seeping in.

2. **Translation**: It translates or transforms data and requests between different bounded contexts, ensuring that each context only deals with its own ubiquitous language and model.

3. **Isolation**: The ACL isolates the bounded context from changes in external systems or contexts, reducing the impact of those changes on the internal model.

4. **Integration**: It facilitates integration with external systems, legacy systems, or third-party services by providing a clear boundary and translation mechanism.

### Characteristics of Anti-Corruption Layer:

- **Translation Logic**: Contains the logic necessary to convert data from the external model to the internal model and vice versa.
- **Separation**: It is separate from both the internal domain model and the external system's model, acting as a buffer between them.
- **Adaptation**: It adapts the functionality and data of the external system to the needs and semantics of the internal bounded context.

### Examples of Anti-Corruption Layer Components:

- **Translator**: A component that translates data structures between systems.
- **Adapter**: A component that adapts an external system's API to the internal bounded context's API.
- **Gateway**: A component that encapsulates the communication with the external system.

### How to Implement an Anti-Corruption Layer:

An ACL can be implemented using various patterns such as Facades, Adapters, or Gateways. Here's an example in C# of a simple translation mechanism within an ACL:

```csharp
// External system's data model
public class ExternalCustomerData
{
    public string FullName { get; set; }
    public string EmailAddress { get; set; }
    // Other fields from the external model...
}

// Internal bounded context's domain model
public class Customer
{
    public string FirstName { get; private set; }
    public string LastName { get; private set; }
    public Email Email { get; private set; }
    // Other fields and methods...
}

// Translator within the Anti-Corruption Layer
public class CustomerTranslator
{
    public Customer Translate(ExternalCustomerData externalData)
    {
        var names = externalData.FullName.Split(' ');
        var email = new Email(externalData.EmailAddress);
        return new Customer(names[0], names[1], email);
    }
}
```

### Considerations When Working with Anti-Corruption Layers:

- **Complexity**: The ACL can add complexity to the system, so it should be used when the benefits of isolation outweigh the overhead.
- **Performance**: Consider the performance impact of data translation and ensure the ACL is not a bottleneck.
- **Evolution**: As external systems evolve, the ACL may need to be updated to accommodate changes.
- **Duplication**: Be wary of duplicating logic that exists in the external system; the ACL should focus on translation, not business logic replication.

The Anti-Corruption Layer is a valuable tool in strategic design for managing integrations and preserving the purity of a bounded context's domain model. It allows different parts of a system to evolve independently while still being able to communicate and interact with each other.