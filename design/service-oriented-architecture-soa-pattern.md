---
b: https://blendedfeelings.com/software/design/service-oriented-architecture-soa-pattern.md
---

# Service-Oriented Architecture (SOA) 
is a software design approach where services are provided to the other components by application components, through a communication protocol over a network. The basic principles of SOA are to allow easy cooperation of a large number of computers that are connected over a network.

Here are some key characteristics of SOA:

1. **Loose Coupling**: Services are designed with the intention that they can be used without a deep knowledge of the services themselves. They should not be tightly integrated with the consuming application, allowing for flexibility and ease of integration.

2. **Interoperability**: SOA promotes the use of standards that ensure services can operate across different platforms and languages, which is essential for the systems distributed over different networks.

3. **Reusability**: Services are designed to be reused in different scenarios and applications, which can lead to significant reductions in development time and cost.

4. **Discoverability**: Services can be discovered using a registry that allows consumers to find them and understand what they do without knowing their technical details.

5. **Abstraction**: Services hide the logic they encapsulate from the outside world. The internal workings of a service are not exposed to the consumers, which means that the service provider can change the service implementation without affecting the consumers.

6. **Standardized Service Contract**: Services adhere to a communications agreement, as defined collectively by one or more service-description documents.

7. **Autonomy**: Services have control over the logic they encapsulate, from a design-time and run-time perspective.

8. **Statelessness**: Services are stateless as much as possible, but may maintain state in certain situations. Being stateless means that the service does not remember anything between executions.

9. **Scalability**: SOA can be scaled out by adding more services to the pool that fulfill the same service contract.

10. **Composition**: Services can be composed to form new services. This is often done using business process orchestration.

SOA can be implemented using various technologies, including Web Services (SOAP, REST), messaging systems (JMS, AMQP), and more. It is important to note that SOA is a design philosophy, not a specific technology or standard, and it can be implemented in many different ways depending on the needs of the organization.