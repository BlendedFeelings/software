---
b: https://blendedfeelings.com/software/concurrent-programming/versioning-and-timestamps.md
---

# Versioning and timestamps 
are techniques used in the design of concurrent data structures to manage consistency and detect conflicts. These methods are particularly useful in lock-free and wait-free data structures where multiple threads may access and modify shared data without using locks to coordinate their actions. Here's how they work:

### Versioning

In versioning, each data item in the structure is associated with a version number (or counter). The version number is incremented whenever the data item is updated. Here's a simplified example of how versioning might be used in a lock-free data structure:

1. A thread reads the version number and the data.
2. It computes the new value based on the read data.
3. It attempts to update the data using an atomic compare-and-swap (CAS) operation that checks if the version number is unchanged since it was last read.
4. If the CAS succeeds, the update is applied, and the version number is incremented.
5. If the CAS fails (because another thread has updated the data), the thread retries from step 1.

By checking the version number before updating, the thread can ensure that no other thread has modified the data in the meantime, thus maintaining consistency.

### Timestamps

Timestamps serve a similar purpose to version numbers but use a global notion of time (or logical time) to order operations. Each operation is tagged with a timestamp, and the system ensures that operations are applied in timestamp order. Here's a high-level view of how timestamps might be used:

1. A thread obtains a unique timestamp for its operation (often from a global counter or clock).
2. It reads the current state of the data along with the timestamp of the last update.
3. It computes the new value based on the read data.
4. It attempts to apply the new value using an atomic operation, ensuring that the timestamp of the last update has not changed.
5. If successful, the data is updated with the new value and the new timestamp.
6. If unsuccessful, the thread retries, possibly obtaining a new timestamp.

Timestamps can be particularly useful in multi-version concurrency control (MVCC) systems, where each write operation creates a new version of the data item tagged with a timestamp. Readers can then access the version of the data that was current at the time their read operation started, providing a consistent view of the data without preventing concurrent writes.

### Considerations

- **Performance:** Both versioning and timestamps can incur overhead due to the need to manage additional metadata and handle retries in the case of conflicts.
- **Memory Overhead:** Each data item needs to store a version number or timestamp, which can increase memory usage.
- **Scalability:** These techniques can help improve scalability by reducing the need for locks, but they also require careful design to avoid excessive retries and contention.
- **Complexity:** Implementing these techniques correctly can be complex and requires a deep understanding of concurrency control.

In practice, versioning and timestamps are often combined with other lock-free techniques, such as backoff strategies, to create robust and efficient concurrent data structures. They are particularly well-suited for environments with high read-to-write ratios, as they allow reads to proceed without blocking while still ensuring that writes occur in a consistent order.