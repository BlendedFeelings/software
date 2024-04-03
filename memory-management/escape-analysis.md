---
b: https://blendedfeelings.com/software/memory-management/escape-analysis.md
---

# Escape analysis 
is an optimization technique used by compilers and runtime environments to determine the scope and lifetime of objects in a program. It analyses how objects are used to decide whether they can be allocated on the stack instead of the heap, potentially leading to significant performance improvements. The key idea is to detect if an object's reference "escapes" the method or scope in which it was created.

Here's how escape analysis generally works:

1. **Analysis**: The compiler or runtime environment examines the code to track the flow of object references. It looks for points in the code where an object reference is passed outside its current scope, such as returning the reference from a method, storing it in a global variable, or passing it to another method that may store it globally.

2. **Stack Allocation**: If the analysis determines that an object does not escape the method in which it was created, the object can be allocated on the stack. Stack allocation is typically faster than heap allocation and does not require garbage collection.

3. **Heap Allocation**: If the object reference does escape, then the object must be allocated on the heap to ensure that it remains accessible after the method returns.

4. **Optimization**: The compiler applies the results of the escape analysis to optimize memory usage by converting heap allocations to stack allocations where possible.

Advantages of escape analysis include:

- **Performance**: Stack allocation is faster than heap allocation. It also avoids the overhead associated with garbage collection since stack-allocated objects are automatically reclaimed when the stack frame is popped.
- **Reduced Garbage Collector Pressure**: Fewer objects on the heap mean less work for the garbage collector, which can improve overall system performance.
- **Improved Cache Locality**: Objects allocated on the stack are more likely to benefit from cache locality, as they are accessed in a last-in-first-out (LIFO) order, which is friendly to the CPU cache.

However, escape analysis is a complex process and may not always be able to detect all the cases where an object does not escape. The effectiveness of escape analysis can depend on the sophistication of the compiler's or runtime's implementation.

Escape analysis is most commonly used in managed runtime environments like the Java Virtual Machine (JVM) and .NET Common Language Runtime (CLR), which have sophisticated garbage collectors and runtime optimizers. It can also be used in ahead-of-time compiled languages like C++ to inform certain optimizations, although it's less common due to the manual memory management model typically used in such languages.