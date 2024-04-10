---
b: https://blendedfeelings.com/software/data-store/session-consistency.md
---

# Session consistency 
is a consistency model that ensures a system maintains a consistent state within the context of a single user's session. It is a guarantee that a user will receive a consistent view of the data for the duration of their session, even in a distributed system where data may be replicated across multiple nodes.

Under session consistency, once a user has performed a write operation, any subsequent read operations within the same session should reflect that write. This means that the user can see their own changes immediately, but it does not necessarily guarantee that other users will see those changes right away.

Session consistency is particularly useful in scenarios where a user is interacting with a system in a sequence of operations that depend on each other. For example, if a user is editing a document in a cloud-based editor, session consistency ensures that each change they make is visible in subsequent reads during that editing session.

Here are some key points about session consistency:

1. **User-centric**: The consistency guarantee is specific to the session of a user or process, not the entire system.

2. **Scope**: It typically applies to a sequence of operations performed by a single user or process, ensuring that the operations are consistent within that scope.

3. **Implementation**: It can be implemented using various techniques, such as client-side tracking of operations, sticky sessions that route a user's requests to the same server, or ensuring that read operations fetch data from the same replica where the recent write occurred.

4. **Tunable consistency**: Session consistency allows for different consistency levels within the same system. While one user's session may require strong consistency, other operations outside of that session might use weaker consistency models for better performance.

5. **Latency and Performance**: By focusing on consistency within a session rather than across the entire system, session consistency can reduce the latency and performance overhead associated with maintaining strict consistency across all operations.

Session consistency is one of several models designed to provide a balance between the strong guarantees of strict consistency and the performance benefits of eventual consistency. It allows developers to design systems that provide a good user experience by ensuring that users see a consistent view of their own interactions with the system, while still allowing for some degree of eventual consistency in the background.