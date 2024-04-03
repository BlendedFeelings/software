---
b: https://blendedfeelings.com/software/domain-driven-design/context-mapping.md
---

# Context Mapping 
is a strategic tool in Domain-Driven Design (DDD) that helps teams understand and visualize the relationships between different parts of a system, specifically between bounded contexts. It is a way of making explicit the connections and boundaries between various models within a system.

### Purpose of Context Mapping:

1. **Clarify Boundaries**: It helps clarify the boundaries of each bounded context and how they are defined within the larger system.

2. **Understand Relationships**: Context Mapping enables teams to understand how different bounded contexts relate to and depend on each other.

3. **Integration Strategies**: It provides insights into how bounded contexts should integrate, communicate, and share data.

4. **Highlight Shared Kernels**: Identifies shared parts of the model that are common between contexts (Shared Kernel).

5. **Reveal Anticorruption Layers**: Reveals where translation layers (Anticorruption Layers) are needed to protect one bounded context from the changes in another.

6. **Identify Upstream and Downstream Relationships**: Determines which bounded contexts are upstream (providers) and which are downstream (consumers) in terms of data flow and influence.

### Key Concepts in Context Mapping:

- **Bounded Context**: A distinct area within the domain where a particular domain model is defined and applicable.

- **Upstream/Downstream**: Describes the flow of data and dependency between two bounded contexts. The upstream context may influence the model of the downstream context.

- **Integration Points**: Specific locations where bounded contexts interact with each other.

- **Shared Kernel**: A common subset of the domain model that is shared by two or more bounded contexts.

- **Anticorruption Layer (ACL)**: A layer that translates between bounded contexts, protecting one context from the changes or idiosyncrasies of another.

- **Open Host Service (OHS)**: A bounded context that provides a well-defined, stable interface for other contexts to consume.

- **Published Language**: A common language or protocol agreed upon by multiple bounded contexts for communication.

- **Conformist**: A pattern where one bounded context adopts the model of another without translation, typically when one context must conform to another's model due to a power dynamic.

- **Customer/Supplier**: A relationship where one bounded context (the supplier) provides data or functionality that another bounded context (the customer) depends on.

### How to Create a Context Map:

1. **Identify Bounded Contexts**: Start by identifying all the bounded contexts within the system.

2. **Determine Relationships**: Analyze how each bounded context relates to the others. Look for dependencies, data flows, and shared models.

3. **Choose Integration Patterns**: Select appropriate integration patterns for each relationship (e.g., ACL, OHS, Shared Kernel).

4. **Document the Map**: Create a visual representation of the bounded contexts and their relationships, often using diagrams.

5. **Review and Refine**: Regularly review the Context Map with team members and stakeholders to ensure it remains accurate and useful.

Context Mapping is an essential part of the strategic design in DDD, as it helps teams to navigate and manage the complexity of large systems with multiple bounded contexts. It enables effective planning for system integration and provides a clear understanding of how changes in one part of the system may impact others.