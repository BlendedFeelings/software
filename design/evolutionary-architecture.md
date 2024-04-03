---
b: https://blendedfeelings.com/software/design/evolutionary-architecture.md
---

# Evolutionary architecture 
is a term used to describe a method of designing software that allows for continuous and incremental changes without the need for large-scale rework. The concept is based on the idea that software systems should be able to evolve over time as requirements change and new technologies emerge.

Here are some key principles and practices associated with evolutionary architecture:

1. **Incremental Change**: The architecture is designed in such a way that changes can be made in small increments, rather than through big, disruptive leaps. This reduces risk and allows for continuous delivery and deployment.

2. **Fitness Functions**: These are objective metrics or criteria used to guide the architecture in evolving in the right direction. Fitness functions can be automated tests that validate architectural characteristics like performance, scalability, or maintainability.

3. **Modularity**: A modular design with well-defined interfaces allows for parts of the system to be changed or replaced without affecting the whole. This supports the idea of making small, isolated changes that can be tested and rolled back if necessary.

4. **Loose Coupling**: Components or services within the system should be loosely coupled, meaning they interact through well-defined interfaces and are not overly reliant on each other's internal workings. This allows for parts of the system to evolve independently.

5. **Reversibility**: Decisions should be made with reversibility in mind, so that if a change turns out to be detrimental, it can be undone or modified with minimal cost.

6. **Continuous Integration and Delivery (CI/CD)**: A robust CI/CD pipeline is essential for evolutionary architecture, as it allows for frequent integration of changes and ensures that the system is always in a releasable state.

7. **Experimentation and Learning**: An evolutionary architecture encourages experimentation to find the best solutions, and a culture of learning from both successes and failures.

8. **Data-Driven Decision Making**: Decisions about the evolution of the architecture should be based on data and evidence, rather than assumptions or opinions.

9. **Collaboration and Communication**: Architects, developers, and stakeholders must collaborate closely and communicate effectively to ensure that the architecture evolves in a way that meets the needs of the business and its users.

10. **Guided Evolution**: While the architecture is designed to evolve, it should be guided by a clear vision and architecture principles that align with the business goals.

Evolutionary architecture is particularly well-suited to environments where change is constant, such as in agile software development. It requires a mindset that embraces change and a willingness to invest in practices and infrastructure that support the ongoing evolution of the system.