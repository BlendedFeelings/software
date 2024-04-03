---
b: https://blendedfeelings.com/software/memory-management/golang.md
---

# Memory management in Go 
is primarily handled through the use of garbage collection, which automatically frees memory that is no longer in use. Go's runtime has a built-in garbage collector (GC) that periodically runs and reclaims memory that is not reachable by any part of the program. As a developer, you do not need to explicitly free memory as you would in languages like C or C++.

Here are some key points about memory management in Go:

1. **Garbage Collection**: The garbage collector in Go is a concurrent, tri-color mark-and-sweep collector. It works by marking objects that are still reachable, sweeping away those that aren't, and then compacting the memory to reduce fragmentation.

2. **Allocation**: Memory allocation in Go is done using the built-in `new` function for individual objects or by making slices, maps, and channels. The `make` function is used to initialize slices, maps, and channels, and it also allocates the underlying memory.

3. **Escape Analysis**: The Go compiler performs escape analysis to determine whether a variable can be allocated on the stack (which is faster and reclaimed automatically when the function returns) or if it must be allocated on the heap (which is managed by the garbage collector).

4. **Manual Memory Management**: While Go's garbage collector handles most memory management tasks, you can still influence memory usage by:
   - Using pointers to share large data structures rather than copying them.
   - Reusing objects by pooling them (e.g., using `sync.Pool`).
   - Being mindful of scope and lifetime of variables to help the garbage collector reclaim memory sooner.
   - Reducing allocations by avoiding unnecessary temporary objects.

5. **Profiling and Debugging**: Go has tools to monitor and analyze memory usage, such as `pprof`, which can help you identify memory leaks or areas of your program that are using more memory than expected.

6. **Setting GC Percentage**: You can control the aggressiveness of the garbage collector by setting the `GOGC` environment variable. The default value is 100, which means that the garbage collector will trigger a collection when the heap size doubles. Setting `GOGC` to a lower value will make the collector run more frequently, potentially reducing memory usage at the cost of CPU time.

7. **Finalizers**: Go provides the `runtime.SetFinalizer` function that allows you to associate finalizers with objects. A finalizer is a function that is called when the garbage collector is about to collect the object. However, the use of finalizers is generally discouraged because they can make memory management unpredictable and complicate the program's behavior.

In summary, Go's runtime manages memory efficiently through garbage collection, and as a developer, you typically do not need to worry about freeing memory. However, understanding how Go manages memory can help you write more efficient and performant code.