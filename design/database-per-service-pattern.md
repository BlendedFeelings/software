---
b: https://blendedfeelings.com/software/design/database-per-service-pattern.md
---

# Database per Service pattern 
is a design approach used in [microservices architecture](microservices-pattern.md) where each microservice has its own database schema and manages its data independently. This pattern is a departure from the traditional [monolithic architecture](monolithic-architecture-pattern.md), where a single database serves the data needs of the entire application.

Here are the key characteristics and considerations of the Database per Service pattern:

1. **Service Independence**: Each microservice is responsible for its data persistence, data model, and database migrations. This allows services to evolve independently without affecting others.

2. **Decentralization**: The pattern promotes decentralization of data management, which aligns with the microservices philosophy of building a distributed system with loosely coupled components.

3. **Data Encapsulation**: Services encapsulate their data and expose it through APIs. Other services that need to access this data must do so through these APIs rather than direct database access.

4. **Polyglot Persistence**: Since each service manages its database, teams can choose the database technology that best fits their service's needs (e.g., SQL, NoSQL, graph databases) without being constrained by a single database choice for the entire application.

5. **Autonomy**: Services can be developed, deployed, scaled, and maintained independently, which can lead to faster development cycles and easier deployment processes.

6. **Resilience**: The pattern can improve system resilience, as a failure in one service's database does not directly impact the databases of other services.

However, the Database per Service pattern also comes with challenges:

1. **Data Consistency**: Maintaining data consistency across services can be complex, especially when transactions involve multiple services. Techniques like distributed transactions or eventual consistency may be required.

2. **Data Duplication**: Some data may need to be duplicated across services, leading to challenges in keeping this data synchronized.

3. **Complexity**: The system's overall complexity can increase, as there are more databases to manage, and developers must implement mechanisms for inter-service communication.

4. **Operational Overhead**: More databases mean more work for operations teams in terms of backups, monitoring, and maintenance.

5. **Data Access Patterns**: Careful design is required to avoid inefficient access patterns, such as excessive inter-service communication or complex data aggregations.

6. **Migration**: Migrating from a monolithic database to a database per service can be challenging and requires careful planning and execution.

When implementing the Database per Service pattern, it's important to weigh the benefits against the challenges and consider whether the pattern fits the application's requirements and the team's capabilities. This pattern is well-suited for systems that require high levels of scalability, flexibility, and resilience, and where service independence is a key concern.