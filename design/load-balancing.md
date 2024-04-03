---
b: https://blendedfeelings.com/software/design/load-balancing.md
---

# Load balancing 
refers to the process of distributing workloads across multiple computing resources, such as servers, network links, or CPUs. The goal of load balancing is to optimize resource use, maximize throughput, minimize response time, and avoid overloading any single resource. It is a crucial aspect of high-availability, scalability, and reliability in distributed systems.

Here are several key concepts and methods associated with load balancing in software:

1. **Types of Load Balancers:**
   - **Hardware Load Balancers:** Physical devices that manage network traffic to servers.
   - **Software Load Balancers:** Applications that run on standard hardware and perform similar functions to hardware load balancers.
   - **Cloud-Based Load Balancers:** Services provided by cloud platforms (like AWS, Azure, Google Cloud) that distribute traffic across cloud resources.

2. **Load Balancing Algorithms:**
   - **Round Robin:** Distributes each incoming request sequentially to the next server in a pool.
   - **Least Connections:** Directs traffic to the server with the fewest active connections.
   - **IP Hash:** Determines which server to use based on the hash of the client's IP address.
   - **Weighted Algorithms:** Servers are assigned weights based on their capacity, and traffic is distributed accordingly.

3. **Session Persistence:**
   Sometimes also referred to as "sticky sessions," this ensures that a user's session is maintained with the same server for the duration of their visit.

4. **Health Checks:**
   Regular checks on servers to ensure they are available and capable of handling requests. If a server fails a health check, it can be temporarily removed from the pool.

5. **Redundancy:**
   Having multiple load balancers can provide redundancy, ensuring that if one fails, another can take over.

6. **Scalability:**
   Load balancers can help systems scale horizontally by adding more servers to the pool as demand increases.

7. **Global Server Load Balancing (GSLB):**
   Distributes traffic across servers in different geographical locations to improve response times and provide disaster recovery.

8. **SSL Termination:**
   Load balancers can also handle the decryption of SSL/TLS traffic, offloading this CPU-intensive task from the web servers.

9. **Content-Based Routing:**
   Directs requests to different servers based on the content being requested or other properties of the incoming request.

10. **Network-Level Balancing:**
    Load balancing can also occur at the network level using protocols like DNS or at the transport layer with TCP/UDP.

Load balancing can be implemented in various layers of the OSI model and is not limited to just the application layer. It is an essential component of modern IT infrastructure, particularly in environments that require high availability and the ability to handle large volumes of traffic.