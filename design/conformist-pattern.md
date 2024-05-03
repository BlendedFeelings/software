---
b: https://blendedfeelings.com/software/design/conformist-pattern.md
---

# Conformist pattern 
is applied in situations where one bounded context needs to integrate with another, but there is a significant difference in power or control between them. The typical scenario is when one team cannot influence the design of the other team's model, often because the other team's model is part of a third-party system or a system that is owned by a more dominant part of the organization.

Here's how the Conformist pattern works:

- **Conform to the Model**: The team adopts the external bounded context's model as-is, without trying to change or influence it. This means conforming to the data structures, behaviors, and language of the external model.
- **Integration Simplicity**: By conforming to the external model, integration becomes simpler because there is no translation or adaptation layer between the systems. The team accepts the model even if it's not ideal for their needs.
- **Downsides**: The downside of this approach is that the team might have to deal with a model that doesn't fit well with their domain. This can lead to suboptimal solutions and can affect the team's productivity and the system's maintainability.
- **Upstream-Downstream Relationship**: In the Conformist pattern, the team with the bounded context that conforms is considered "downstream," while the team with the bounded context being conformed to is "upstream." The downstream team aligns with the upstream team's decisions.
- **Reduced Autonomy**: The Conformist pattern reduces the autonomy of the downstream team, as they are not in a position to negotiate changes or improvements to the upstream model.

When using the Conformist pattern, it is important for the downstream team to carefully consider the long-term implications of adopting another model wholesale. It may be the right choice in cases where the cost of translation or the risk of miscommunication is too high, or where the upstream model is stable and well-designed. However, if the external model is poor or does not align well with the downstream context, it can lead to technical debt and other challenges.

In DDD, the Conformist pattern is one of several strategic patterns for dealing with integration between bounded contexts, each with its own trade-offs. Other patterns include Anticorruption Layer, Shared Kernel, Partnership, Customer/Supplier, and Separate Ways. The choice of pattern depends on the nature of the relationship between the bounded contexts and the strategic goals of the organization.