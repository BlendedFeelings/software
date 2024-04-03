---
b: https://blendedfeelings.com/software/domain-driven-design/bounded-context.md
---

# Bounded Contexts 
are a central pattern in Domain-Driven Design (DDD) that define the boundaries within which a particular domain model is defined and applicable. They serve as a way to divide a complex system into manageable parts, each with its own domain model and ubiquitous language.

### Purpose of Bounded Contexts:

1. **Manage Complexity**: By breaking down a large system into smaller contexts, you can manage complexity more effectively.
2. **Reduce Ambiguity**: Within a bounded context, terms and concepts have specific, unambiguous meanings.
3. **Encourage Cohesion**: Bounded contexts help to keep related concepts together, which promotes a cohesive model.
4. **Enable Autonomy**: Teams can work independently on different contexts, reducing the coordination overhead.
5. **Facilitate Integration**: Bounded contexts define clear contracts for how different parts of the system interact with each other.

### Characteristics of Bounded Contexts:

- **Model Boundary**: Each bounded context has its own domain model that does not need to be consistent with models in other contexts.
- **Ubiquitous Language**: The ubiquitous language within a bounded context is specific to that context and may vary from one context to another.
- **Context Map**: A context map is used to understand and document the relationships between different bounded contexts.

### How to Define Bounded Contexts:

1. **Identify Subdomains**: Start by identifying subdomains within the larger domain, which are potential candidates for bounded contexts.
2. **Define Boundaries**: Establish clear boundaries based on business capabilities, organizational structure, or technical considerations.
3. **Develop Models**: For each bounded context, develop a domain model that addresses its specific concerns.
4. **Align Teams**: Align development teams with bounded contexts, often one team per context.
5. **Establish Integrations**: Define how bounded contexts will interact with each other using well-defined interfaces or shared kernels.

### Types of Relationships Between Bounded Contexts:

- **Partnership**: Two contexts cooperate to fulfill a business goal.
- **Shared Kernel**: Contexts share a common subset of the domain model.
- **Customer/Supplier**: One context provides a service that another context consumes.
- **Conformist**: One context conforms to the model of another context to avoid complexity.
- **Anticorruption Layer**: A context protects its model from being polluted by another context's model.
- **Open Host Service**: A context provides a service with a well-defined protocol that other contexts can use.
- **Published Language**: A common language is established for contexts to communicate, often seen in public APIs.

### Challenges:

- **Boundary Identification**: Determining the optimal boundaries for contexts can be challenging and may require adjustments as understanding evolves.
- **Integration**: Integrating bounded contexts while maintaining their autonomy requires careful design of communication mechanisms.
- **Team Coordination**: When multiple teams are involved, coordination can become complex, especially when teams are responsible for multiple contexts.

Bounded Contexts are a powerful way to deal with complexity in software development. They allow teams to work on different parts of a system without stepping on each other's toes and help maintain a clean and consistent domain model within each context. When used effectively, bounded contexts can greatly improve the maintainability and scalability of a software system.