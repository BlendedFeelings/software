---
b: https://blendedfeelings.com/software/domain-driven-design/shared-kernel.md
---

# Shared kernel 
refers to a common subset of the domain model that is shared between two or more bounded contexts. A bounded context is a central pattern in DDD, defining the limits of a particular sub-domain or business capability within which a particular domain model applies. It is essentially a boundary within which a particular "language" is consistent and applicable.

The shared kernel is a strategy for integrating bounded contexts by sharing some parts of the model between them. Here are some key points about the shared kernel:

1. **Shared Understanding**: The teams responsible for each bounded context agree on the shared kernel. It includes a common understanding of the domain elements it contains.

2. **Common Code**: The shared kernel is often a subset of the codebase that is physically shared between different bounded contexts. This could be in the form of shared libraries or services.

3. **Minimalism**: The shared kernel should be as small as possible to minimize the dependency between the teams and contexts. Only the essential parts of the domain that truly need to be shared should be included.

4. **Explicit Contracts**: Changes to the shared kernel require agreement between all teams involved. It is common to have an explicit contract that governs how changes are made to the shared kernel to ensure that all teams are aware and have agreed to the modifications.

5. **Continuous Integration**: To ensure that changes to the shared kernel do not break other contexts, teams often use continuous integration practices.

6. **Ownership and Governance**: Even though the shared kernel is used by multiple bounded contexts, it is important to have clear ownership and governance policies in place to manage changes and resolve conflicts.

The shared kernel is one of several patterns for dealing with the integration of bounded contexts in DDD, alongside others like Anti-Corruption Layer, Open Host Service, and Published Language. The choice of pattern depends on the level of integration required and the degree of autonomy each bounded context needs.

Using a shared kernel can reduce duplication and foster a more unified approach to common problems, but it also introduces coupling between bounded contexts. It is essential to manage this carefully to maintain the benefits of modularity that DDD aims to provide.