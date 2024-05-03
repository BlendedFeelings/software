---
b: https://blendedfeelings.com/software/design/registrator-pattern.md
---

# Registrator pattern 
is a design pattern used in service-oriented architectures, especially in microservices, to automate the registration and deregistration of services with a service discovery system. In a dynamic environment, where service instances can be frequently created and destroyed (e.g., in a cloud environment with auto-scaling), manually keeping the service registry up to date can be error-prone and cumbersome. The Registrator pattern addresses this issue by providing an automated way to manage service instance information in the service registry.

Here's how the Registrator pattern typically works:

1. **Service Instance Starts**: When a new instance of a service starts, it may broadcast its existence, or a separate Registrator component detects the new instance. This can be done through various mechanisms, such as listening to events from the container orchestrator (like Kubernetes or Docker Swarm) or by the service instance sending a heartbeat to the Registrator.

2. **Registration**: The Registrator component automatically registers the new service instance with the service discovery system. This registration includes metadata about the service, such as its IP address, port number, version, and any other relevant information that clients might need to connect to it.

3. **Service Discovery**: Clients use the service discovery system to retrieve the list of available service instances and their metadata. Clients can then use this information to communicate with the services.

4. **Service Instance Stops**: When a service instance is stopped or fails, the Registrator component detects this event and automatically deregisters the instance from the service discovery system. This ensures that clients do not attempt to connect to unavailable service instances.

5. **Health Checking**: Optionally, the Registrator or the service discovery system can perform health checks on the service instances to ensure they are operational. Unhealthy instances can be deregistered or marked as such in the service registry.

Benefits of the Registrator Pattern:

- **Automation**: Service registration and deregistration are automated, reducing the need for manual intervention and the potential for human error.
- **Resilience**: The system can quickly adapt to changes in the service landscape, such as instances being added or removed, which enhances overall resilience.
- **Simplicity**: Clients can discover services without needing to know the details of where and how many instances are running.

Challenges of the Registrator Pattern:

- **Complexity**: Introducing a Registrator component can add complexity to the deployment and operation of the service infrastructure.
- **Consistency**: Ensuring that the service registry is always consistent with the actual state of the system can be challenging, especially in the face of network partitions or other failures.
- **Latency**: There may be a delay between when a service instance starts or stops and when it is registered or deregistered, which could lead to clients trying to access unavailable services.

An example of a tool that implements the Registrator pattern is the open-source project "Registrator" by Glider Labs, which automatically registers and deregisters Docker services with a service discovery tool like Consul or etcd. In Kubernetes, the pattern is inherently supported by the platform, with services being automatically registered with the internal DNS system when they are created.