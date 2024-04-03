---
b: https://blendedfeelings.com/software/design/valet-key-pattern.md
---

# Valet Key pattern 
is a cloud design pattern that is used to delegate access to a service with restricted permissions, much like giving a valet the key to your car with the understanding that they can only drive it and not access the trunk or glove compartment. In cloud storage systems, this pattern is particularly useful for providing clients with a token or key that grants them direct access to a specific resource or service for a limited time or under certain conditions, without exposing more sensitive data or operations.

Here's how the Valet Key pattern works in the context of cloud services:

1. **Client Request:** A client application requests access to a resource, such as a file in cloud storage.

2. **Service Authorization:** The service authenticates the client and authorizes the request. It then generates a token or key with specific permissions that allow the client to perform the requested operation directly with the storage service.

3. **Valet Key Issuance:** The service provides the client with this token or key, which is the "valet key."

4. **Direct Access:** The client uses the valet key to directly interact with the storage service. This could involve uploading, downloading, or modifying the resource as allowed by the permissions of the valet key.

5. **Expiration:** The valet key is typically time-limited or usage-limited, meaning it will expire after a certain period or after being used a certain number of times.

The advantages of the Valet Key pattern include:

- **Reduced Load on the Service:** By allowing clients to interact directly with storage, the service does not have to act as a proxy for data transfer, thus reducing its load.
- **Improved Performance:** Direct access can lead to better performance and lower latency since data does not have to be routed through an intermediate service.
- **Fine-Grained Access Control:** The service can issue valet keys with very specific permissions, thus adhering to the principle of least privilege.
- **Scalability:** Since the client interacts directly with storage, this pattern can help the service to scale better.

In cloud platforms like Microsoft Azure, this pattern is implemented using Shared Access Signatures (SAS), which provide secure delegated access to resources in the storage account. In Amazon Web Services (AWS), a similar capability can be achieved using pre-signed URLs with Amazon S3.

The Valet Key pattern is particularly useful when dealing with large data transfers or when providing temporary access to resources without compromising security or overloading the main service with data transfer tasks.