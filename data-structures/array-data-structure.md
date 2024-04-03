---
b: https://blendedfeelings.com/software/data-structures/array-data-structure.md
---

# Arrays 
are a fundamental data structure used in programming to store collections of elements. They are one of the simplest and most widely used data structures. Here are some key points about arrays:

1. **Fixed Size**: An array has a fixed size, meaning the number of elements it can hold is defined when the array is created. This size cannot be changed during the lifetime of the array.

2. **Homogeneous Elements**: Arrays typically store elements of the same data type. This means that all elements in an array are of the same type (e.g., all integers, all floats, or all strings).

3. **Contiguous Memory Allocation**: In memory, an array is allocated as a contiguous block. This means that all elements of the array are stored in adjacent memory locations, which allows for efficient access and manipulation of elements.

4. **Index-Based Access**: Each element in an array can be accessed by its index. Indexing usually starts from 0, so the first element is at index 0, the second at index 1, and so on. This allows for quick access to any element, as the memory address of any element can be calculated using the base address of the array and the element's index.

5. **Efficiency**: Accessing an element by its index is a constant-time operation, denoted as O(1), meaning it takes the same amount of time regardless of the array's size. However, operations like inserting or deleting elements (especially in the middle of the array) can be costly because they may require shifting elements to maintain the array's contiguous nature.

6. **Use Cases**: Arrays are used when you need to store a known number of elements and perform operations like iterating through the elements, accessing elements by their position, or performing computations on the elements.

Here is an example of how an array might be declared in C#:

```csharp
int[] numbers = new int[5]; // An array of 5 integers
```

And here's how you might access and set values in the array:

```csharp
numbers[0] = 10; // Set the first element to 10
int firstNumber = numbers[0]; // Access the first element
```

Arrays are a building block for more complex data structures and algorithms and are supported in some form by nearly all programming languages.