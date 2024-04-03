---
b: https://blendedfeelings.com/software/design/deployment-stamps-pattern.md
---

# Deployment Stamps pattern 
is a software architecture pattern that is used to manage and scale deployments in cloud environments. It is particularly useful in scenarios where a single application needs to be deployed in multiple isolated instances, often referred to as "stamps". Each stamp represents a deployment of the application with its own dedicated set of resources, such as databases, storage, and compute instances.

Key aspects of the Deployment Stamps pattern include:

1. **Isolation**: Each stamp is isolated from the others, meaning that issues in one stamp (like performance problems or security breaches) do not affect the others.

2. **Scalability**: The pattern allows for horizontal scalability because new stamps can be added as needed to handle increased load or to serve different geographical regions.

3. **Consistency**: All stamps are based on the same deployment configuration, ensuring consistency across different instances of the application.

4. **Manageability**: Although each stamp is isolated, they can be managed in a consistent way using common tools and processes.

5. **Customization**: While the stamps are typically identical in setup, they can be customized as needed for specific requirements, such as compliance with local regulations.

6. **Fault Tolerance**: By spreading the application across multiple stamps, the overall system can tolerate faults in individual stamps without a total system failure.

The Deployment Stamps pattern is often used in conjunction with other cloud design patterns, such as the Sharding pattern for distributing data across different stamps, or the Circuit Breaker pattern to prevent failures in one stamp from cascading to others.

This pattern is particularly relevant for SaaS (Software as a Service) providers that need to deploy their application for a large number of tenants (customers), where each tenant might require their own isolated environment.

An example of the Deployment Stamps pattern in action could be a company that provides a web-based CRM system. The company could create a separate stamp for each major customer, ensuring that each customer's data and usage does not impact any other customer. Each stamp would have its own web servers, database servers, and storage, and could be located in different data centers or cloud regions to meet data residency requirements.

In summary, the Deployment Stamps pattern is a strategic approach to deploying cloud-based applications that need to be replicated across multiple isolated environments, providing scalability, manageability, and fault tolerance.