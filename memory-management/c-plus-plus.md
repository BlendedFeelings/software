---
b: https://blendedfeelings.com/software/memory-management/c-plus-plus.md
---

# Memory management in C++ 
is a critical aspect of programming, as it involves the allocation, use, and deallocation of memory in your programs. Proper memory management can help prevent memory leaks and other issues that can lead to poor performance or system crashes. Here's an overview of memory management in C++:

### Stack Memory Allocation
- The stack is used for static memory allocation, which includes local variables within functions and is managed automatically by the compiler.
- Memory is allocated when a function is called and deallocated when the function exits.
- Stack memory allocation is fast and efficient but limited in size.

### Heap Memory Allocation
- The heap is used for dynamic memory allocation, which allows you to allocate memory at runtime.
- Memory is allocated and deallocated using operators `new` and `delete` respectively for single objects, or `new[]` and `delete[]` for arrays of objects.
- Heap memory is larger than stack memory but slower to allocate and deallocate.

### `new` and `delete` Operators
- `new` is used to allocate memory on the heap for an object or an array of objects.
- `delete` is used to deallocate memory that was previously allocated with `new`.
- It is crucial to match each `new` with a corresponding `delete` to prevent memory leaks.

### Smart Pointers (C++11 and later)
- Smart pointers are template classes that ensure automatic deallocation of heap memory when no longer needed.
- `unique_ptr`: Allows exactly one owner of the underlying pointer. It can't be copied but can be moved.
- `shared_ptr`: Allows multiple owners of the same pointer; the memory is deallocated when the last `shared_ptr` goes out of scope.
- `weak_ptr`: Complements `shared_ptr` by providing a non-owning "weak" reference.

### Custom Memory Management
- Advanced users can override the `new` and `delete` operators for custom memory management.
- Placement `new` allows you to construct an object in a pre-allocated memory buffer.

### Best Practices
- Always match `new` with `delete` and `new[]` with `delete[]`.
- Use smart pointers to manage dynamic memory automatically.
- Avoid using raw pointers for memory ownership whenever possible.
- Be cautious with pointer arithmetic and always ensure pointers are valid before dereferencing them.
- Regularly check for memory leaks using tools like Valgrind or address sanitizers.

Here's an example of using `new` and `delete` in C++:

```cpp
#include <iostream>

int main() {
    // Allocate memory for an int on the heap
    int* myInt = new int(10);

    // Use the allocated memory
    std::cout << "Value of myInt: " << *myInt << std::endl;

    // Deallocate the memory
    delete myInt;

    // Allocate memory for an array of ints
    int* myArray = new int[5]{1, 2, 3, 4, 5};

    // Use the allocated array
    for (int i = 0; i < 5; ++i) {
        std::cout << "myArray[" << i << "]: " << myArray[i] << std::endl;
    }

    // Deallocate the array
    delete[] myArray;

    return 0;
}
```

## Smart pointers


### `std::unique_ptr`
`std::unique_ptr` is a smart pointer that owns and manages another object through a pointer and disposes of that object when the `unique_ptr` goes out of scope. It does not allow for the pointer to be copied, ensuring that there is only one owner of the memory resource.

Here's an example of using `std::unique_ptr`:
```cpp
#include <memory>

int main() {
    // Create a unique_ptr to an integer
    std::unique_ptr<int> uniquePtr(new int(10));

    // Use the unique_ptr
    *uniquePtr = 20;

    // No need to delete, memory is automatically released when uniquePtr goes out of scope
    return 0;
}
```

### `std::shared_ptr`
`std::shared_ptr` is a smart pointer that retains shared ownership of an object through a pointer. Multiple `shared_ptr` instances can own the same object, and the object is destroyed and its memory deallocated when the last remaining `shared_ptr` owning the object is destroyed.

Here's an example of using `std::shared_ptr`:
```cpp
#include <memory>

int main() {
    // Create a shared_ptr to an integer
    std::shared_ptr<int> sharedPtr1(new int(10));

    {
        // Create another shared_ptr that shares ownership
        std::shared_ptr<int> sharedPtr2 = sharedPtr1;

        // Both pointers now own the memory
    } // sharedPtr2 goes out of scope, but the memory is not released because sharedPtr1 still exists

    // Memory will be released when sharedPtr1 goes out of scope
    return 0;
}
```

### `std::weak_ptr`
`std::weak_ptr` is a smart pointer that holds a non-owning ("weak") reference to an object that is managed by `std::shared_ptr`. It is used to break circular references of `shared_ptr` instances.

Here's an example of using `std::weak_ptr`:
```cpp
#include <memory>

int main() {
    // Create a shared_ptr
    std::shared_ptr<int> sharedPtr(new int(10));

    // Create a weak_ptr from a shared_ptr
    std::weak_ptr<int> weakPtr(sharedPtr);

    // Use the weak_ptr to check if the object still exists and to get a shared_ptr to it
    if (auto tempSharedPtr = weakPtr.lock()) {
        // The object exists, and tempSharedPtr is a shared_ptr that owns the memory
    } else {
        // The object has been destroyed
    }

    // Memory will be released when the last shared_ptr goes out of scope
    return 0;
}
```

Smart pointers should be used instead of raw pointers whenever possible to ensure that memory is managed correctly. They are especially useful in complex programs with dynamic memory allocation, where manual memory management can lead to errors.

In the example above, we allocate memory for an integer and an array of integers, use them, and then deallocate the memory to prevent leaks. Remember that in modern C++, it is recommended to use smart pointers instead of raw pointers for better memory management.