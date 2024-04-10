# Empty interface in Go
is specified as `interface{}`. It is an interface that has zero methods and is satisfied by any type, because any type implements at least zero methods. The empty interface is used to handle values of unknown type since it can hold values of any type, much like `void*` in C or `Object` in Java.

Here's an example of how you might define and use an empty interface in Go:

```go
package main

import "fmt"

func main() {
    var anyType interface{} // Declare a variable of empty interface type

    anyType = 5
    fmt.Println(anyType) // Outputs: 5

    anyType = "hello"
    fmt.Println(anyType) // Outputs: hello

    anyType = struct{ name string }{"Jane"}
    fmt.Println(anyType) // Outputs: {Jane}
}

// The anyType variable is used to store and print values of different types.
```

The empty interface is useful when you want a function to accept any type of argument, or when a data structure needs to store items of any type. However, to actually work with the value stored in an empty interface, you will typically need to perform a type assertion or type switch to determine its dynamic type.