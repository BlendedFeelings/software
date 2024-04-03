---
b: https://blendedfeelings.com/software/algorithms/searche/square-root-binary-search-algorithm.md
---

# SquareRootBinarySearch 
is an algorithm used to find the square root of a given number using binary search. It works by repeatedly dividing the range of possible square roots in half until the desired level of accuracy is achieved. The algorithm is based on the observation that the square root of a number is always between 1 and the number itself, so the search can be limited to this range.

The basic idea of the SquareRootBinarySearch algorithm is to start with a range [low, high], where low=1 and high=n (the number whose square root is to be found). Then, the algorithm repeatedly divides this range in half until the desired level of accuracy is achieved. At each step, the algorithm checks whether the middle point of the range is the square root of the number. If it is, the algorithm returns this value. Otherwise, the algorithm updates the range to either the left or right half of the current range, depending on whether the middle point is less than or greater than the square root of the number. The process continues until the desired level of accuracy is achieved.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/searches/SquareRootBinarySearch.java]
```