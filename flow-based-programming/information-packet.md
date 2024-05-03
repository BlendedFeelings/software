---
b: https://blendedfeelings.com/software/flow-based-programming/information-packet.md
---

# Information packet (IP) 
is a discrete, immutable data entity that is transmitted between decoupled components within a network, facilitating asynchronous and concurrent data processing.

1. **Data Encapsulation**: An IP encapsulates a piece of data or a data structure. This can be anything from a simple integer or string to a complex object or file.

2. **Immutability**: IPs are typically immutable; once created, their content does not change. This makes the system more predictable and prevents side effects.

3. **Ownership**: At any given time, an IP is "owned" by only one component. This means that when a component sends an IP to another, it relinquishes control over that IP. The receiving component takes ownership and is responsible for eventually disposing of it.

4. **Asynchronous Communication**: Components communicate by sending and receiving IPs asynchronously. This allows for concurrent execution and can improve the scalability and performance of an application.

5. **Ports**: Each component has defined input and output ports. IPs are sent and received through these ports. The connections between components' ports define the application's network topology.

6. **Queues**: Ports often have queues to hold IPs until the component is ready to process them. This allows for the decoupling of component execution speeds.

7. **Types**: IPs can be typed, meaning that a port can be designed to accept only certain kinds of data. This helps in preventing errors and enforcing data integrity within the network.

8. **Lifecycle**: An IP has a lifecycle that typically includes creation, transportation, processing, and disposal. Proper management of this lifecycle is crucial to prevent memory leaks and ensure that all resources are released appropriately.

9. **Back-pressure**: Some FBP systems implement back-pressure mechanisms to control the flow of IPs and prevent components from being overwhelmed by incoming data.

10. **Debugging and Monitoring**: Since IPs are discrete data elements that flow through the network, it is possible to monitor and log their movement for debugging and analysis purposes.

FBP is particularly well-suited for problems that can be naturally modeled as networks of processes or for systems that require high levels of concurrency and modularity. The paradigm is used in various domains, from audio and video processing to financial systems and complex event processing.