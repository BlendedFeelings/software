---
b: https://blendedfeelings.com/software/algorithms/searche/iterative-ternary-search-algorithm.md
---

# Iterative Ternary Search
is a searching algorithm used to find the position of a target value within an array. It is called "ternary" because it divides the array into three parts in each iteration. The array must be sorted in ascending order for this algorithm to work.

The algorithm begins by dividing the array into three parts by finding the two midpoints, m1 and m2, as follows:

m1 = left + (right-left)/3
m2 = right - (right-left)/3

If the target value is equal to the element at index m1 or m2, the search terminates and the index is returned. If the target value is less than the element at index m1, the search is continued on the left third of the array. If the target value is greater than the element at index m2, the search is continued on the right third of the array. Otherwise, the search is continued on the middle third of the array.

The algorithm repeats this process until the target value is found or the search space is exhausted.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/searches/IterativeTernarySearch.java]
```