---
b: https://blendedfeelings.com/software/algorithms/sort/slow-sort-algorithm.md
---

# SlowSort
is a recursive sorting algorithm that is intentionally designed to be inefficient. It was created as a joke algorithm by Andrei Broder in 1985 to demonstrate that not all algorithms are created equal. 

The algorithm works by recursively dividing the input array into two halves, then swapping the elements in the two halves if they are out of order. This process is repeated until the array is sorted. However, the algorithm is intentionally designed to take a long time to sort even small arrays, making it impractical for real-world use.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/SlowSort.java]
```