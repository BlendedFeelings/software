---
b: https://blendedfeelings.com/software/design/client-side-loadbalancer-pattern.md
---

# Client-side load balancer pattern 
is a design pattern used in distributed systems where the client is responsible for distributing the load between a set of server instances. This pattern is often used in microservices architectures where multiple instances of a service are running and the client needs to decide which instance to send a request to.

Here's how the pattern generally works:

1. **Service Discovery**: The client retrieves a list of available service instances from a service registry, which keeps track of all the instances of the services in the system.

2. **Load Balancing Strategy**: The client uses a load balancing strategy to select which service instance to use for each request. Common strategies include:
   - **Round Robin**: Requests are distributed sequentially among the service instances.
   - **Random**: A service instance is chosen at random for each request.
   - **Least Connections**: The instance with the fewest active connections is chosen.
   - **Weighted**: Instances are chosen based on assigned weights, which could be based on each instance's capacity or response time.

3. **Making the Request**: The client makes the request to the selected service instance. If the instance is available and can handle the request, it processes it and returns a response.

4. **Handling Failures**: If the selected service instance fails to handle the request (e.g., due to a crash or network issue), the client-side load balancer can retry the request with another instance.

5. **Feedback Loop**: Optionally, the load balancer can use feedback from the service instances (such as average response times or error rates) to make more informed load balancing decisions in the future.

Benefits of the Client-Side Load Balancer Pattern:

- **Reduced Latency**: Since the client can select the closest or fastest service instance, it can reduce overall latency.
- **Scalability**: The pattern allows for easy scaling of services by simply adding more instances.
- **Flexibility**: Different load balancing strategies can be implemented and changed according to the needs of the system.
- **Resilience**: The system can continue to function even if some service instances become unavailable.

Challenges of the Client-Side Load Balancer Pattern:

- **Complexity**: Implementing a client-side load balancer can add complexity to the client application.
- **Consistency**: Keeping the service registry up to date and ensuring all clients have a consistent view of service instances can be challenging.
- **Resource Usage**: The client must have the resources (e.g., CPU, memory) to perform load balancing operations.

Popular tools and libraries that implement client-side load balancing include Netflix's Ribbon (now in maintenance mode) and Spring Cloud LoadBalancer in the Java ecosystem. Other languages and frameworks have similar libraries or service meshes (like Istio or Linkerd) that can take on the role of load balancing.