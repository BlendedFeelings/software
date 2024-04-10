---
b: https://blendedfeelings.com/software/clean-architecture/stable-abstractions-principle-sap.md
---

# Stable Abstractions Principle (SAP) 
is designed to manage the dependencies between different parts of a system, ensuring that stable components (those that are unlikely to change) are also highly abstract. This makes them more flexible and less likely to require changes as the details of the system's implementation evolve.

The Stable Abstractions Principle states that:

> A component should be as abstract as it is stable.

Here's what each part of the principle means:

- **Stability**: A stable component is one that has many dependents. A change in a stable component would require a lot of other components to change as well. Therefore, stability is a measure of how much a component is depended on.
  
- **Abstraction**: An abstract component is one that contains interfaces, abstract classes, or abstract methods. It defines behavior but leaves the implementation of that behavior to be defined by other, more concrete components.

According to the SAP, the more stable a component is, the more it should use abstract classes and interfaces. This allows the details that are likely to change to be easily swapped out without affecting the clients that depend on the abstract component.

The SAP is often visualized using the Main Sequence, a line drawn on a graph where one axis represents the degree of abstraction (from concrete to abstract) and the other axis represents stability (from unstable to stable). Ideally, components should lie close to the line that represents the ideal balance between abstraction and stability.

By adhering to the Stable Abstractions Principle, developers can create a system architecture that is easier to maintain and extend over time. It helps to avoid the rigidity that comes from components that are both concrete and stable, which would be difficult to change, and the uselessness of components that are abstract but unstable, which nobody relies on.