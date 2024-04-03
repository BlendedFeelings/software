---
b: https://blendedfeelings.com/software/memory-management/garbage-collection/generational-collection.md
---

# Generational garbage collection 
is based on the empirical observation that most objects die young, often referred to as the "weak generational hypothesis." In other words, many objects are allocated and quickly become unreachable (die), while only a small percentage of objects live for a longer period of time.

To take advantage of this observation, memory is divided into different generations that reflect the age of objects:

- **Young Generation**: This is where new objects are allocated. It is typically small and collected frequently. Objects that survive several garbage collection cycles in the young generation are promoted to an older generation.
- **Old Generation**: This contains objects that have survived multiple collections in the young generation. Because these objects are more likely to be long-lived, the old generation is collected less frequently.
- **(Optional) Permanent Generation or Metaspace**: In some languages, like Java, there is a concept of a permanent generation (or Metaspace in newer versions of Java), which is used to store metadata such as class definitions. This area is collected separately from the young and old generations.

Here's how generational garbage collection typically works:

1. **Allocation**: New objects are allocated in the young generation, which is usually implemented as one or more areas called Eden space and Survivor spaces.

2. **Minor Collection**: When the young generation becomes full, a minor garbage collection is triggered. Live objects from the Eden space and one of the Survivor spaces are copied to the other Survivor space, compacting them in the process. Objects that are too large for the Survivor space or that have survived enough minor collections are promoted to the old generation.

3. **Major Collection (Full GC)**: Periodically, or when the old generation becomes full, a major garbage collection is performed. This involves collecting both the young and old generations. Major collections are more time-consuming and can lead to longer pause times.

4. **Promotion**: Objects that survive garbage collection in the young generation are promoted to the old generation based on certain criteria, such as age or size.

5. **Tuning**: Generational garbage collectors can often be tuned with various parameters, such as the sizes of different generations and the thresholds for promotion, to optimize performance for specific applications.

Advantages of Generational GC:
- **Efficiency**: Since most objects die young, collecting the young generation is usually fast and frees up a significant amount of memory.
- **Reduced Fragmentation**: Frequent collections in the young generation can help to reduce memory fragmentation.
- **Performance**: By focusing on collecting the young generation, where most garbage is, the garbage collector can improve overall performance and reduce pause times.

Disadvantages of Generational GC:
- **Complexity**: The algorithm is more complex than simple mark-and-sweep or reference counting.
- **Inter-generational References**: Objects in the old generation that reference objects in the young generation (cross-generational references) require special handling, typically using a card table or write barrier to track these references efficiently.
- **Tuning Required**: Different applications may require different tuning of the garbage collector to achieve optimal performance.

Generational garbage collection is widely used in modern programming languages like Java (with the HotSpot JVM), C# (.NET Framework and .NET Core), and others. It is well-suited for applications that create a lot of short-lived objects, which is common in object-oriented programming.