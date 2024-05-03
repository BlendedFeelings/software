---
b: https://blendedfeelings.com/software/domain-driven-design/application-service.md
---

# Application services are 
a layer that coordinates the application's activities. They are responsible for orchestrating the flow of data between the domain layer (where the core business logic resides) and the infrastructure or interface layers (where data is presented or persisted). Application services are part of the outer layers of the DDD architecture and serve to separate the domain concerns from the user interface or external systems.

Here are some key characteristics and responsibilities of application services in DDD:

1. **Coordination of Workflows**: Application services handle the orchestration of domain objects and domain services to perform specific business use cases or workflows. They ensure that the correct domain logic is executed in the right order.

2. **Transaction Management**: These services often manage transactions, ensuring that a series of domain operations either complete successfully as a unit of work or are rolled back together in case of failure.

3. **Domain Logic Delegation**: While application services coordinate tasks, they delegate the business logic to the domain entities and domain services. They should not contain business logic themselves; their role is to call upon the domain model to perform business operations.

4. **Interface Adaption**: Application services adapt the inputs and outputs of the domain model to the needs of the different client interfaces, such as web, API, or desktop applications.

5. **Security and Permissions**: They may handle authentication and authorization, ensuring that only permitted users can execute certain operations.

6. **Validation**: Application services can perform validation of input data before it is passed to the domain model for processing.

7. **DTOs and View Models**: They often use Data Transfer Objects (DTOs) or view models to transfer data between the domain layer and the presentation layer, thus avoiding exposing internal domain objects to the client.

8. **Logging and Auditing**: These services may also be responsible for logging and auditing operations for diagnostic and compliance purposes.