---
b: https://blendedfeelings.com/software/low-level/optimization/avoiding-unnecessary-memory-accesses.md
---

# Avoiding unnecessary memory accesses 
is a key optimization strategy that can greatly improve the performance of a program. Memory access is relatively expensive in terms of CPU cycles, especially if the data is not found in the cache and has to be fetched from the main memory. By minimizing memory accesses, you can reduce the program's execution time and improve its overall efficiency.

Here are some techniques to avoid unnecessary memory accesses:

1. **Reuse Computed Values**: Store the results of computations in local variables if they will be used multiple times, rather than recalculating them each time they are needed.

2. **Minimize Use of Temporary Variables**: Temporary variables can lead to additional memory writes and reads. Whenever possible, compute values directly where they are needed, or use in-place algorithms to reduce the need for temporaries.

3. **Use Registers Wisely**: Make use of the CPU's registers for frequently accessed variables. Compilers often handle this automatically, but in performance-critical code, you might need to give the compiler hints (e.g., using the `register` keyword in C) or use inline assembly to ensure that variables are kept in registers.

4. **Loop Invariants**: Move calculations that do not change within a loop outside of the loop. This prevents the same calculation from being performed in each iteration.

5. **Strength Reduction**: Replace expensive operations with cheaper ones, especially inside loops. For example, replace multiplication with addition when possible.

6. **Structure Packing**: Pack data structures to eliminate unused space (padding) and reduce the overall memory footprint, which can lead to fewer cache lines being used.

7. **Lazy Evaluation**: Delay the computation of a value until it is actually needed, which can sometimes prevent the computation altogether if the value ends up not being used.

8. **Eliminate Redundant Loads and Stores**: Ensure that your code does not repeatedly load or store the same value to memory when it could be kept in a register.

9. **Batch Updates**: If multiple updates to a data structure are required, batch them together to minimize the number of times the structure is accessed.

10. **Prefetching**: If you know you will need certain data soon but don't need it immediately, you can prefetch it into the cache to avoid a stall later on.

Here's an example that demonstrates some of these principles:

```c
// Original code
for (int i = 0; i < n; ++i) {
    result[i] = (a[i] * b[i]) + (c[i] * d[i]);
}

// Optimized code
int temp1, temp2;
for (int i = 0; i < n; ++i) {
    temp1 = a[i] * b[i]; // Compute once and reuse
    temp2 = c[i] * d[i]; // Compute once and reuse
    result[i] = temp1 + temp2;
}
```

In the optimized code, the products `a[i] * b[i]` and `c[i] * d[i]` are computed once and stored in temporary variables `temp1` and `temp2`, which can potentially be held in registers. This avoids the need to recompute these values if they are used elsewhere in the code.

Remember that modern compilers are quite good at optimizing code, so many of these optimizations may be automatically applied when compiling with optimization flags. However, understanding these principles can help you write more efficient code from the start and guide you when manual optimization is necessary. Always profile your code to ensure that the optimizations you apply have the desired effect.