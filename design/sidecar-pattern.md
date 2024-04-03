---
b: https://blendedfeelings.com/software/design/sidecar-pattern.md
---

# Sidecar pattern 
is a design pattern used in software architecture, particularly in the context of microservices. It is a structural pattern that involves deploying an additional component (the "sidecar") alongside a primary application or service. This sidecar is tightly coupled with the main application and provides supporting features for the application, such as monitoring, logging, configuration, networking services, and more.

Here are some key aspects of the sidecar pattern:

1. **Isolation of Responsibilities**: The sidecar manages certain aspects of the application, such as inter-service communications, security, or telemetry, without the application needing to be aware of these details. This allows developers to focus on the business logic of the primary service.

2. **Consistency**: By using a sidecar, you can apply the same set of functionalities across multiple services in a consistent manner. For example, if you have a logging sidecar, it can be used with various services to provide uniform logging capabilities.

3. **Ease of Updates**: Since the sidecar is a separate component, it can be updated independently of the application. This means you can update, for example, security protocols or communication features without touching the application code.

4. **Language-agnostic**: The sidecar can be implemented in any programming language, regardless of the language used for the main application. This is particularly useful in a polyglot environment where different services are written in different languages.

5. **Scalability**: Sidecars can be scaled independently from the application. If a particular aspect of the sidecar's functionality needs to be scaled up (like rate limiting or request caching), it can be done without scaling the entire application.

6. **Network Abstraction**: In many cases, sidecars abstract away the network communication, so services can communicate with each other without having to deal with the complexities of network protocols, service discovery, or retries.

A common example of the sidecar pattern is the use of Envoy proxy in the service mesh architecture, like Istio, where Envoy acts as a sidecar to each service instance, handling inbound and outbound traffic for the services.

To visualize the sidecar pattern, imagine a containerized environment where each container runs a single application or service. Alongside each application container, you have a sidecar container that handles certain cross-cutting concerns. They share the same lifecycle, meaning they are created and retired together.

The sidecar pattern is a powerful tool in the microservices ecosystem, providing a modular and scalable way to add functionality to applications without increasing complexity within the application code itself.