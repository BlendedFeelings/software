# Slicing in Go 
is a common operation that allows you to create a new slice from an existing array, slice, or string. Slicing is done by specifying a half-open range with two indices separated by a colon. The first index indicates the start of the slice, and the second index indicates the end of the slice (non-inclusive). If you omit the start index, it defaults to 0; if you omit the end index, it defaults to the length of the array, slice, or string.

Here's an example of how to create a slice from an array:

```go
package main

import "fmt"

func main() {
    // Define an array
    numbers := [5]int{0, 1, 2, 3, 4}

    // Create a slice from the array
    slice := numbers[1:4] // This will include elements at index 1, 2, and 3

    fmt.Println(slice) // Output: [1 2 3]
}
```

You can also create a slice with a missing start or end index:

```go
sliceStart := numbers[:3] // This will include elements at index 0, 1, and 2
sliceEnd := numbers[2:]   // This will include elements at index 2, 3, and 4
```

Slicing can also be applied to strings to obtain substrings:

```go
message := "Hello, World!"
substring := message[7:12] // This will get "World"

fmt.Println(substring) // Output: World
```

Remember that slices in Go are references to the underlying array. Therefore, modifying the elements of a slice will also modify the corresponding elements in the original array. If you want to create a slice that does not modify the original array, you can use the `copy` function to create a new independent slice.

Here's an example of using `copy`:

```go
original := []int{1, 2, 3, 4, 5}
sliced := original[1:4] // Create a slice that includes elements 2, 3, and 4

// Create a new slice with the same length as 'sliced'
copied := make([]int, len(sliced))

// Copy the elements from 'sliced' to 'copied'
copy(copied, sliced)

// Now 'copied' is an independent slice
```

When you use `copy`, the elements are copied over to the new slice, and any modifications to this new slice will not affect the original array or slice.