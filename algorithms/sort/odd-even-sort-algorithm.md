---
b: https://blendedfeelings.com/software/algorithms/sort/odd-even-sort-algorithm.md
---

# Odd-even Sort
is a simple sorting algorithm that sorts the elements by comparing and swapping them in pairs. It works by repeatedly iterating through the array, comparing adjacent elements in pairs, and swapping them if they are in the wrong order. The algorithm sorts the even-indexed elements and odd-indexed elements separately in two phases, and it repeats these phases until the array is completely sorted. The time complexity of this algorithm is O(n^2), which makes it inefficient for large arrays.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/OddEvenSort.java]
```