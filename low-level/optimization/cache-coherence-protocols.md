---
b: https://blendedfeelings.com/software/low-level/optimization/cache-coherence-protocols.md
---

# Cache coherence protocols 
are mechanisms used in multi-processor systems to ensure that multiple caches maintain a consistent view of shared memory. When multiple processors or cores with their own caches are used, it's possible for the same memory location to be cached in several caches simultaneously. If one processor modifies the data in its cache, the other processors must be made aware of this change to ensure they don't work with stale data.

The main goal of cache coherence protocols is to provide a consistent and up-to-date view of memory across all processors. To maintain coherence, these protocols typically provide answers to the following questions:

1. **When is a write by one processor visible to another processor?**
2. **What happens on a read or write to a shared memory location?**

Here are the most common cache coherence protocols:

### MESI Protocol (Illinois Protocol)
The MESI protocol is a widely-used cache coherence protocol that defines four states for each cache line:

- **M (Modified)**: The cache line is present only in the current cache and has been modified from the value in main memory. The cache is responsible for writing the data back to the main memory.
- **E (Exclusive)**: The cache line is present only in the current cache and matches the main memory. It can be safely written to without informing other caches.
- **S (Shared)**: The cache line may be stored in multiple caches and matches the main memory. It cannot be written to without informing other caches.
- **I (Invalid)**: The cache line is invalid or not present in the current cache.

### MOESI Protocol
The MOESI protocol adds a fifth state to the MESI protocol:

- **O (Owned)**: The cache line is present in one or more caches and might be modified in at least one cache. The owning cache is responsible for providing the data to other caches and updating the main memory.

### MSI Protocol
The MSI protocol is a simpler protocol with only three states:

- **M (Modified)**: Same as in MESI.
- **S (Shared)**: Same as in MESI.
- **I (Invalid)**: Same as in MESI.

### MESIF Protocol
The MESIF protocol is an extension of MESI used by Intel processors. It adds a fifth state:

- **F (Forward)**: Indicates that the cache line is shared and that the cache holding this line will respond to requests from other caches.

### Dragon Protocol
The Dragon protocol is another coherence protocol that is based on a write-update strategy instead of write-invalidate, which means that when a processor writes to a cache line, the new value is broadcasted to other caches that have a copy of that line.

### Berkeley Protocol
The Berkeley protocol, also known as the Firefly protocol, uses a write-once strategy, which means the first write to a shared line by any cache causes the line to become unshared.

### Write-Invalidate vs. Write-Update
Cache coherence protocols generally use one of two strategies to handle writes:

- **Write-Invalidate**: When a processor writes to a cache line, other copies of that line in different caches are marked as invalid. This is used by the MESI protocol.
- **Write-Update**: When a processor writes to a cache line, the new value is sent to all other caches that have a copy of that line. This can increase bus traffic but ensures that all caches have the most up-to-date value.

Implementing cache coherence protocols is complex and requires careful design to balance performance, complexity, and power consumption. The choice of protocol can significantly affect the performance of a multi-processor system, especially for workloads with a high degree of shared data access.