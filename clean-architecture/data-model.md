---
b: https://blendedfeelings.com/software/clean-architecture/data-model.md
---

# Data Models
in the context of clean architecture, refer to the structures that are used to transfer data between different layers of an application, particularly between the interface adapters and the external agencies such as databases, web APIs, or file systems. These models are specifically tailored to the needs of the external interfaces and are distinct from the entities and domain models used in the business logic layer.

### Characteristics of Data Models:

1. **External Representation**: Data models represent how data is structured for external purposes, such as for storage in a database or for transmission over a network.

2. **Mapping to/from Domain Models**: They are often mapped to and from domain models (entities) to separate the concerns of the core business logic from external data representation.

3. **Persistence Models**: In the context of databases, data models are often referred to as persistence models or database models. They match the structure of the database tables and are used by ORMs (Object-Relational Mapping) or data access layers.

4. **DTOs (Data Transfer Objects)**: For communication with external services or for sending data to the UI, data models can take the form of DTOs, which are simple containers for data without any business logic.

5. **Serialization**: Data models are designed to be easily serializable and deserializable to formats like JSON or XML for network transmission.

6. **Validation**: While data models may include some validation, it is typically focused on structural validation rather than deep business rules.

### Implementation:

Data models are typically implemented as simple classes or structures in the programming language being used. They are designed to be lightweight and are often devoid of complex logic. Here's an example of what data models might look like in C#:

```csharp
// Data model for a customer as stored in the database
public class CustomerEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Email { get; set; }
    // Other fields that match the database schema for customers
}

// Data transfer object for sending customer information over a network
public class CustomerDTO
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Email { get; set; }
    // Other fields suitable for network transfer
}

// Data model for a customer as used in the UI layer
public class CustomerViewModel
{
    public string FullName { get; set; }
    public string EmailAddress { get; set; }
    // Other fields and properties tailored to the UI
}
```

In this example, `CustomerEntity` is a data model that matches the database schema and is used by the data access layer to interact with the database. `CustomerDTO` is a data transfer object used to send customer information over a network, possibly to a client application or a third-party service. `CustomerViewModel` is a model used by the UI layer to display customer information in a way that is convenient for the user interface.

It is common to use tools like AutoMapper in .NET or similar libraries in other languages to automate the mapping between domain models and data models, reducing the amount of boilerplate code needed to convert between different representations of data.

Data models are essential for communicating data across the boundaries of the clean architecture layers, ensuring that each layer can focus on its specific responsibilities without being coupled to the concerns of other layers.