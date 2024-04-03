---
b: https://blendedfeelings.com/software/algorithms/sort/stooge-sort-algorithm.md
---

# StoogeSort
is a recursive sorting algorithm that sorts an array by dividing it into three parts and recursively sorting the first two parts, then the last two parts, and finally the first two parts again. The algorithm works by comparing the first and last elements of the array, and if the first element is greater than the last element, it swaps them. Then, if there are three or more elements in the array, it recursively sorts the first two-thirds of the array, then the last two-thirds of the array, and finally the first two-thirds of the array again. The algorithm repeats this process until the array is sorted.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/StoogeSort.java]
```