---
b: https://blendedfeelings.com/software/design/representational-state-transfe-rest.md
---

# REST - Representational State Transfer 
is an architectural style for designing networked applications. It relies on a stateless, client-server, cacheable communications protocol -- the HTTP protocol is the most widely used. RESTful systems are characterized by how they use HTTP methods explicitly and how they make use of HTTP for all four CRUD (Create, Read, Update, Delete) operations.

Here are the key principles of REST:

1. **Client-Server Architecture**: The client and the server should be separate from each other and should be able to evolve independently.

2. **Stateless**: Each request from the client to the server must contain all the information the server needs to fulfill the request. The server should not store any state about the client session on the server side.

3. **Cacheable**: Responses must, implicitly or explicitly, define themselves as cacheable or not, to prevent clients from reusing stale or inappropriate data in response to further requests.

4. **Uniform Interface**: The interface between clients and servers is uniform, simplifying and decoupling the architecture, which enables each part to evolve independently. The four guiding principles of the uniform interface are:
   - Resource-Based: Individual resources are identified in requests using URIs as resource identifiers.
   - Manipulation of Resources Through Representations: When a client holds a representation of a resource, including any metadata attached, it has enough information to modify or delete the resource.
   - Self-descriptive Messages: Each message includes enough information to describe how to process the message.
   - Hypermedia as the Engine of Application State (HATEOAS): Clients deliver state via body contents, query-string parameters, request headers, and the requested URI (the resource name).

5. **Layered System**: A client cannot ordinarily tell whether it is connected directly to the end server, or to an intermediary along the way. Intermediary servers may improve system scalability by enabling load-balancing and by providing shared caches.

6. **Code on Demand (optional)**: Servers can temporarily extend or customize the functionality of a client by transferring executable code. This is the only optional constraint of the REST architecture.

RESTful web services typically work over HTTP and use HTTP GET, POST, PUT, DELETE, and PATCH methods to perform CRUD operations. A RESTful web service will expose a set of resources that identify the targets of the interaction with its clients. Resources are identified by URIs, which provide a global addressing space for resource and service discovery. 

RESTful services often return data in JSON or XML format, although other formats can be used, such as YAML, HTML, or plain text. The choice of representation format is based on the needs of the consumer and the type of data being delivered.