---
b: https://blendedfeelings.com/software/golang/make-new.md
---

# Make and New functions 
are built-in functions that are used to allocate and initialize memory for built-in data types. The `new` function allocates zeroed memory for any type and returns a pointer to it, while `make` is used to allocate and initialize slices, maps, and channels, returning an initialized value of the type, not a pointer.

### `new` Function
The `new` function allocates memory for a variable of a given type and returns a pointer to it. The allocated memory is zeroed, which means that each bit is set to 0. For numeric types, this means the value is initialized to 0, for booleans it's `false`, for strings it's the empty string `""`, and for pointers, it's `nil`.

Here is the syntax for the `new` function:

```go
pointer := new(Type)
```

Example of using `new`:

```go
ptr := new(int) // ptr is a pointer to an int that is initialized to 0
```

### `make` Function
The `make` function is used to allocate and initialize memory for only three types: slices, maps, and channels. Unlike `new`, `make` returns an initialized (non-zeroed) value of the type, not a pointer.

Here is the syntax for the `make` function:

```go
value := make(Type, size)
```

For slices and channels, you can also specify the capacity:

```go
slice := make([]Type, length, capacity)
channel := make(chan Type, buffer_size)
```

Example of using `make`:

```go
slice := make([]int, 10) // slice of 10 ints, all initialized to 0
m := make(map[string]int) // map of strings to ints
ch := make(chan int) // unbuffered channel of ints
```

### Differences
- `new` returns a pointer to a zeroed variable of the specified type.
- `make` returns an initialized (but not zeroed) value of the type (only for slices, maps, and channels).
- `new` can be used with any type, while `make` is limited to slices, maps, and channels.

Use `new` when you need a pointer to a new zeroed value of a type. Use `make` when you need to create a slice, map, or channel and you want it to be initialized and ready for use.