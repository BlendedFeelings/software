---
b: https://blendedfeelings.com/software/domain-driven-design/strategic-design.md
---

# Strategic Design 
in Domain-Driven Design (DDD) refers to the high-level approach to understanding and designing the overall structure and boundaries of a system based on its domain. It involves making decisions about the large-scale structure of a software system, how different parts of the system relate to each other, and how to align the software architecture with business goals.

Strategic Design focuses on the following key concepts:

1. **Bounded Contexts**: Identifying distinct areas of the domain where a particular model applies, and defining the boundaries within which the model is consistent and applicable. Each bounded context can have its own ubiquitous language, and the same term can mean different things in different bounded contexts.

2. **Context Mapping**: Understanding and visualizing the relationships between bounded contexts. This includes identifying how they communicate and integrate with each other, and what kind of data or model is shared between them.

3. **Subdomains**: Dividing the domain into various subdomains, each representing a different area of business expertise. Subdomains can be core, supporting, or generic, depending on their strategic importance to the business.

4. **Core Domain**: Identifying the core domain, which is the most central part of the business model and provides competitive advantage. Focusing on the core domain is crucial, as it should be the most sophisticated and well-designed part of the system.

5. **Ubiquitous Language**: Establishing a common language that is shared by developers and domain experts within each bounded context. This language should be used consistently in code, documentation, and discussions.

6. **Integration Patterns**: Deciding on the patterns and mechanisms for integrating different bounded contexts, such as shared kernel, customer/supplier, anticorruption layer, open host service, and published language.

7. **Distillation**: The process of identifying the essential concepts of the domain model and refining them to create a more focused and coherent model.

8. **Large-Scale Structure**: Defining the high-level architecture and patterns that will guide the development of the system, such as layers, services, and modules.

Strategic Design is about the big-picture decisions that shape the overall design and architecture of the system. It ensures that the software structure aligns with business goals and that the complexity of the domain is managed effectively through clear boundaries and well-defined relationships between different parts of the system.

By applying Strategic Design, teams can create a blueprint for a complex software system that allows for scalability, maintainability, and the ability to adapt to changing business needs over time. It also helps to coordinate the efforts of multiple teams by providing a clear understanding of the system's overall structure and how their work fits into the bigger picture.