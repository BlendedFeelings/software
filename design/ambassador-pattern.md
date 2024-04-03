---
b: https://blendedfeelings.com/software/design/ambassador-pattern.md
---

# Ambassador pattern 
is a structural pattern used in software architecture where a helper service, known as an ambassador, acts as an intermediary between a client application and another service (often remote). This pattern is particularly useful when dealing with cross-cutting concerns such as logging, monitoring, network resilience, and security.

Here's an overview of the Ambassador pattern and its components:

1. **Client Application**: The primary application that needs to consume services provided by a remote service.

2. **Ambassador Service**: A proxy that acts on behalf of the client application. It is responsible for sending requests to the remote service and can also handle additional tasks such as:
   - **Retries**: Automatically retrying a request if the initial attempt fails.
   - **Circuit Breaking**: Preventing the application from making requests to a failing service to avoid cascading failures.
   - **Load Balancing**: Distributing requests across multiple instances of a service.
   - **Logging**: Recording details about requests and responses for debugging and monitoring purposes.
   - **Security**: Adding authentication and encryption to requests.

3. **Remote Service**: The service that the client application wants to use. The remote service is unaware of the ambassador and behaves as if it is being accessed directly by the client.

The Ambassador pattern is particularly useful in microservices architectures and distributed systems where network-based communication is prevalent. It helps to decouple the client application from the complexity of interacting with external services, making the application's codebase simpler and more focused on its core functionality.

One of the most common implementations of the Ambassador pattern is the use of sidecar containers in container orchestration platforms like Kubernetes. A sidecar container runs alongside the main application container in the same pod, acting as an ambassador by handling cross-cutting concerns.

For example, Envoy Proxy is a high-performance distributed proxy designed for single services and applications, as well as a communication bus and “universal data plane” designed for large microservice “service mesh” architectures. It can be used as an ambassador to provide dynamic service discovery, load balancing, TLS termination, HTTP/2 and gRPC proxies, circuit breakers, health checks, staged rollouts, and more.