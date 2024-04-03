---
b: https://blendedfeelings.com/software/data-structures/dynamic-array-data-structure.md
---

# Dynamic array 
is a data structure that allows you to store a collection of elements that can grow and shrink in size during the runtime of a program. Unlike a static array, which has a fixed size determined at the time of its creation, a dynamic array can resize itself automatically when elements are added or removed.

Here are some key features and operations of a dynamic array:

1. **Initialization**: A dynamic array is usually initialized with an initial capacity. This is an estimate of the number of elements it will hold.

2. **Addition of Elements**: You can add elements to a dynamic array. If the array's capacity is exceeded, it typically grows by allocating a larger block of memory, copying the existing elements to the new block, and then adding the new element.

3. **Deletion of Elements**: You can remove elements from a dynamic array. Depending on the implementation, the array might shrink when a certain threshold of unused capacity is reached.

4. **Accessing Elements**: Elements in a dynamic array can be accessed by their index, just like in a static array.

5. **Resizing**: The resizing process is usually done by creating a new array with a larger capacity and copying the elements from the old array to the new one.

6. **Amortized Complexity**: Although resizing an array is an expensive operation, dynamic arrays are designed such that the average time per operation is still efficient. This is known as amortized analysis.

Here's a simple example of how a dynamic array might be implemented in Python:

```python
class DynamicArray:
    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._array = self._make_array(self._capacity)
    
    def _make_array(self, new_capacity):
        return [None] * new_capacity
    
    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity
    
    def append(self, item):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._size] = item
        self._size += 1
    
    def __getitem__(self, index):
        if 0 <= index < self._size:
            return self._array[index]
        raise IndexError('Index out of bounds')
    
    def __len__(self):
        return self._size

# Usage
dyn_array = DynamicArray()
dyn_array.append(1)
dyn_array.append(2)
print(dyn_array[0])  # Output: 1
print(dyn_array[1])  # Output: 2
print(len(dyn_array))  # Output: 2
```

In this example, the `DynamicArray` class manages an internal array that grows by doubling its capacity whenever it runs out of space. The `append` method is used to add new elements, and the internal `_resize` method is called when necessary to allocate more space.

In other programming languages, dynamic arrays might be provided as built-in types or standard library features, such as `ArrayList` in Java, `vector` in C++, or `List` in C#.