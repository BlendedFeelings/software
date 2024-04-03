---
b: https://blendedfeelings.com/software/algorithms/sort/bucket-sort-algorithm.md
---

# Bucket Sort
is a sorting algorithm that works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm. Bucket sort is often used when the input is uniformly distributed over a range, and the range is known in advance. It has an average case complexity of O(n+k), where n is the number of elements to be sorted and k is the number of buckets. However, its worst-case complexity can be as high as O(n^2), depending on the sorting algorithm used for the individual buckets.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/BucketSort.java]
```