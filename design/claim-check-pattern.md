---
b: https://blendedfeelings.com/software/design/claim-check-pattern.md
---

# Claim-Check pattern 
is a messaging pattern used in software architecture to efficiently handle large data sets or large binary objects when integrating different systems or components. This pattern is particularly useful when dealing with message-oriented middleware, where passing large messages over the network can be expensive and slow.

**How the Claim-Check Pattern Works:**

1. **Initial Request**: A client sends a message (the claim) to a service, which includes a reference to the data rather than the data itself. This reference is typically a unique identifier or key.

2. **Data Storage**: The large data payload is stored in a persistent storage system (like a database, file system, or blob storage). The storage location is associated with the unique identifier provided in the initial message.

3. **Claim Ticket**: The service processes the initial message and returns a claim ticket to the client. This ticket contains the unique identifier that can be used to retrieve the data at a later time.

4. **Data Processing**: When the data is needed for processing, the recipient service uses the claim ticket to retrieve the data from the persistent storage. The service can then perform the necessary operations on the retrieved data.

5. **Data Retrieval**: After processing, if the client needs access to the processed data, it can use the claim ticket to retrieve the data from the storage.

**Advantages of the Claim-Check Pattern:**

- **Performance**: By avoiding the transfer of large data sets over the network, the pattern can significantly improve the performance of the messaging system.
- **Scalability**: It allows for better scalability since the messaging system is not clogged with large payloads, and services can retrieve data as needed.
- **Reliability**: The pattern can increase reliability since the data is stored persistently, reducing the risk of data loss during transmission.
- **Flexibility**: It provides a flexible approach to data processing, as different services can process the same data independently using the claim ticket.

**Use Cases for the Claim-Check Pattern:**

- **Large File Processing**: When files are too large to be processed in memory or sent over the network in a single message.
- **Data Enrichment**: When a message needs to be enriched with additional data that is too large to include in the original message.
- **Asynchronous Processing**: When processing can be deferred, and there is no need to send all the data with the initial request.

**Considerations:**

- **Data Consistency**: Ensure that the data associated with the claim ticket remains consistent and available throughout the processing lifecycle.
- **Security**: The claim ticket and the data storage must be secured to prevent unauthorized access.
- **Storage Costs**: Depending on the storage solution, there might be costs associated with storing large amounts of data.
- **Complexity**: Introducing the Claim-Check pattern adds complexity to the system, so it should be used only when the benefits outweigh the added complexity.

In summary, the Claim-Check pattern is a useful architectural pattern for handling large data payloads in distributed systems, particularly when using message-oriented middleware. It helps to improve performance, scalability, and reliability, but it also introduces additional complexity and requires careful consideration of data consistency and security.