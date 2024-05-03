---
b: https://blendedfeelings.com/software/design/domain-categories.md
---

# Domain (categories)
is divided into subdomains, each representing a different area of interest within the overall system. These subdomains are categorized into three main types: Core, Generic, and Supporting. Understanding these subdomains is crucial for organizing the complexity of large systems and focusing development efforts where they are most valuable.

### Core Domain

The Core Domain is the central part of the system that provides the unique business capabilities that give the company a competitive advantage. It is the primary reason for the system's existence and usually where the most significant business value lies. In DDD, the Core Domain should receive the most attention in terms of resources, effort, and quality. It's where the most complex domain modeling takes place, and it often requires custom development and deep domain knowledge.

### Generic Subdomain

A Generic Subdomain is a part of the system that does not provide any unique business value but is necessary for the system to function. These are typically common functionalities that can be found across different systems, such as authentication, authorization, logging, or communication with external services. Generic subdomains can often be addressed with off-the-shelf solutions or standard patterns, as they do not require deep domain knowledge or custom development.

### Supporting Subdomain

Supporting Subdomains are areas of the system that provide necessary supporting features to the Core Domain but are not central to the business strategy. They complement the Core Domain by providing additional functionality that enhances the overall user experience or system performance. While they are important, they do not warrant the same level of investment as the Core Domain. Supporting subdomains can sometimes be outsourced or handled with less focus on custom development.

It's important to note that the categorization of subdomains can change over time as the business evolves. What may be considered a Supporting Subdomain at one point could become a Core Domain if it grows in strategic importance.

In DDD, the design and architecture of the system are influenced by the classification of these subdomains. Each subdomain can have its own bounded context, which is a clear boundary within which a particular domain model is defined and applicable. This helps to manage complexity by allowing different subdomains to evolve independently, reducing tight coupling, and enabling teams to focus on specific areas without being overwhelmed by the entire domain.