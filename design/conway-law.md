---
b: https://blendedfeelings.com/software/design/conway-law.md
---

# Conway's Law 
"Organizations which design systems ... are constrained to produce designs which are copies of the communication structures of these organizations."

Conway's Law is an adage named after computer programmer Melvin Conway, who introduced the idea in 1967. It states that:

In the context of software development, Conway's Law suggests that the architecture of a software system will reflect the communication structure of the organization that produces it. For instance, if a company has multiple engineering teams, each responsible for different services or components, the final software product is likely to be a composition of these separate services or components, interfacing with each other in a manner that mirrors the communication pathways between the teams.

Conway's Law has several implications for software development:

1. **Modularity**: If an organization has a siloed structure with little communication between teams, the software produced is likely to be modular with well-defined interfaces, as each team will work on their component in relative isolation.

2. **Integration Challenges**: Conversely, if communication between teams is poor, integrating the modules developed by different teams can be challenging due to mismatched interfaces or conflicting assumptions.

3. **Design and Team Structure**: To create a desired system architecture, an organization might need to consider structuring its teams in a way that promotes the kind of communication that would lead to such an architecture.

4. **Cross-Functional Teams**: Encouraging cross-functional teams can lead to more cohesive and integrated software systems, as the barriers between different areas of expertise are reduced.

5. **Reflecting Organisational Change**: As organizations evolve and change their structure, the software systems they produce may also need to change to reflect the new communication patterns.

Conway's Law has been taken into account in modern software engineering practices, like the microservices architecture, where small, autonomous teams are responsible for individual services that can be developed, deployed, and scaled independently. This approach takes advantage of Conway's Law by aligning the software architecture with the organizational structure to achieve a harmonious and effective development process.