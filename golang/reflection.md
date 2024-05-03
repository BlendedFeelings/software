---
b: https://blendedfeelings.com/software/golang/reflection.md
---

# Reflection in Go 
is a powerful feature that allows you to inspect and manipulate objects at runtime. It is provided by the `reflect` package, which enables you to work with types and values in a dynamic manner. Reflection can be used for a variety of tasks, such as type checking, iterating through the fields of structs, calling functions dynamically, and much more.

Here's a basic example of reflection in Go:

```go
package main

import (
	"fmt"
	"reflect"
)

func main() {
	var x float64 = 3.4
	fmt.Println("type:", reflect.TypeOf(x)) // Prints the type of x

	v := reflect.ValueOf(x)
	fmt.Println("value:", v)               // Prints the value of x
	fmt.Println("type:", v.Type())         // Prints the type of the value held by v
	fmt.Println("kind:", v.Kind())         // Prints the kind of the value held by v, which is a specific type
	fmt.Println("float value:", v.Float()) // Accesses the float value of v

	// Reflection can also be used to modify values if they are settable
	p := reflect.ValueOf(&x) // Note: we pass a pointer to x
	v = p.Elem()
	if v.CanSet() {
		v.SetFloat(7.1)
		fmt.Println("x after modification:", x)
	}
}
```

In this example, we use the `reflect.TypeOf` function to get the type information of the variable `x`. We also use `reflect.ValueOf` to get a `reflect.Value`, which is a wrapper around the actual value, allowing us to introspect and manipulate it.

The `Value` type has many methods to work with the underlying data, such as `Type`, `Kind`, `Float`, and `CanSet`. The `CanSet` method checks if the value is addressable and can be changed. To modify a value, you must pass a pointer to it to `reflect.ValueOf`, and then call `Elem` to get the value that the pointer points to.

Reflection should be used carefully, as it can make code harder to understand and maintain. It also tends to be slower than direct access because of the additional runtime checks and the dynamic nature of the operations involved.