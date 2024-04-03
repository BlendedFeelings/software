---
b: https://blendedfeelings.com/software/memory-management/garbage-collection/tri-color-mark-and-sweep.md
---

# Tri-color mark-and-sweep garbage collector 
is a variation of the mark-and-sweep algorithm used in garbage collection for automatic memory management in programming languages. It is designed to be an incremental garbage collector, meaning it can collect garbage in small steps, interleaved with the program's execution, rather than stopping the entire program to perform garbage collection.

The "tri-color" terminology refers to the use of three colors to mark objects during the garbage collection process:

1. **White**: Objects that are potentially garbage (i.e., they have not been visited yet).
2. **Gray**: Objects that have been discovered to be reachable (i.e., they are not garbage) but whose references have not been fully explored.
3. **Black**: Objects that have been confirmed to be reachable and all of their references have been explored.

The tri-color mark-and-sweep collector operates in two phases:

### Mark Phase
In the mark phase, the collector identifies all the objects that are reachable from the root set (a set of objects known to be reachable, such as global variables and active stack frames). It does this by initially marking all objects as white, then visiting each object in the root set, marking them as gray, and placing them in a gray set. The collector then repeatedly takes a gray object, marks it black, and then marks all objects it references as gray (adding them to the gray set if they are not already black). This process continues until there are no more gray objects, meaning all reachable objects have been marked black.

### Sweep Phase
In the sweep phase, the collector scans through the memory, looking for white objects. Since all reachable objects have been marked black, any remaining white objects are not reachable and can be considered garbage. These white objects are then reclaimed, freeing up memory for future allocations.

The advantage of the tri-color algorithm is that it can be performed incrementally. The collector can pause after processing one or more objects and allow the program to resume execution. This helps to avoid long pauses that can occur in non-incremental garbage collectors.

To maintain correctness when the collector is incremental, the algorithm must handle the case where the program modifies references during the collection process. This is typically done using write barriers, which ensure that any changes to references during the mark phase do not violate the invariants of the tri-color marking. Specifically, if a black object is modified to reference a white object, the white object must be marked gray to ensure it is not incorrectly collected as garbage.

The tri-color mark-and-sweep collector is used in various programming language runtimes and can be quite effective in managing memory in systems where responsiveness and minimizing pause times are important.