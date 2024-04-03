---
b: https://blendedfeelings.com/software/algorithms/sort/bitonic-sort-algorithm.md
---

# Bitonic Sort 
is a parallel comparison-based sorting algorithm that is used to sort a sequence of numbers. It is a divide-and-conquer algorithm that sorts the input sequence in two phases. In the first phase, the input sequence is divided into smaller sequences, and each of these sequences is sorted in ascending order. In the second phase, the sorted sequences are merged together to produce a final sorted sequence.

The algorithm works by comparing pairs of elements that are a certain distance apart in the sequence, and swapping them if they are in the wrong order. This distance between elements is gradually reduced until the entire sequence is sorted.

Bitonic sort is particularly useful for parallel processing, as the sorting of each subsequence can be done independently of the others. This makes it a popular choice for sorting large datasets in parallel computing environments.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/BitonicSort.java]
```