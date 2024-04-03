---
b: https://blendedfeelings.com/software/design/cache-aside-pattern.md
---

# Cache-Aside pattern 
also known as Lazy-Loading, is a caching pattern in software architecture that delays the loading of data into the cache until the moment the data is actually needed. This pattern is commonly used to improve the performance and scalability of applications by reducing the demand on the underlying data store and decreasing latency for the end-users.

Here's how the Cache-Aside pattern generally works:

1. **Check Cache First**: When an application needs to read data, it first checks the cache to see if the data is present.
2. **Load on Miss**: If the data is not found in the cache (a cache miss), the application then loads the data from the data store.
3. **Add to Cache**: After retrieving the data from the data store, the application stores the data in the cache so that subsequent reads for the same data can be served directly from the cache.
4. **Return Data**: The application returns the retrieved data to the client or the part of the application that requested it.
5. **Write Through**: When data is updated or created, the application writes directly to the data store. Optionally, it can also update the cache with the new data to keep it in sync.
6. **Expiration and Eviction**: The cache has an eviction policy that determines when data should be removed. Data can be evicted based on time-to-live (TTL), least recently used (LRU), or other policies. This helps to ensure that the cache does not grow indefinitely and that stale data is not served to the application.

### Benefits of Cache-Aside Pattern:

- **Efficiency**: Reduces the number of reads from the slower, persistent data store and serves data from the faster cache.
- **Scalability**: Helps the application scale by offloading the demand from the data store to the cache.
- **Freshness**: Ensures that the cache contains only the data that is needed, potentially reducing the amount of stale or unused data.

### Drawbacks of Cache-Aside Pattern:

- **Complexity**: Adds complexity to the application code, as the application must manage the cache logic.
- **Cache Coherence**: Requires careful management to ensure that the cache remains consistent with the data store.
- **Latency on Miss**: The first read for a particular piece of data will be slower because it involves both a cache miss and a data store read.

### When to Use:

- When the application has a read-heavy workload and data is read more often than it is updated.
- When the data set is large, but only a subset is frequently accessed.
- When the cost of cache misses is not prohibitive, and the benefit of having frequently accessed data in the cache outweighs it.

### When Not to Use:

- When the application has a write-heavy workload, and data is frequently updated or invalidated.
- When data consistency is of utmost importance, and the complexity of managing cache coherence is not justified.

The Cache-Aside pattern is widely used in distributed systems and can be implemented using various caching technologies like Redis, Memcached, or even in-memory caches within an application.