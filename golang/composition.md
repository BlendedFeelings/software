---
b: https://blendedfeelings.com/software/golang/composition.md
---

# Composition in Go 
is a way to achieve object-oriented-like behavior without using inheritance. In Go, composition is preferred over inheritance, and it's done by embedding one struct into another. This allows the containing struct to access the methods and properties of the embedded struct directly.

Here's an example of how to use composition in Go:

```go
package main

import "fmt"

// Define a struct that will be embedded
type Engine struct {
	Power int // Power in horsepower
}

// Start method for Engine
func (e Engine) Start() {
	fmt.Println("Engine is starting with power:", e.Power)
}

// Define a struct that embeds Engine
type Car struct {
	Engine // Embedding the Engine struct
	Brand string
	Model string
}

func main() {
	// Create a Car instance
	myCar := Car{
		Engine: Engine{Power: 150}, // Initialize the embedded Engine
		Brand:  "Toyota",
		Model:  "Corolla",
	}

	// Accessing the embedded struct's fields and methods
	fmt.Printf("My car is a %s %s with %d horsepower.\n", myCar.Brand, myCar.Model, myCar.Power)
	myCar.Start() // Calling Start() method from the embedded Engine
}
```

In this example, `Car` embeds `Engine`, which means that `Car` now has access to `Engine`'s fields and methods as if they were part of `Car`. You can see that we directly access the `Power` field and `Start()` method on the `myCar` instance without needing to specify the `Engine` explicitly. This is how composition works in Go, and it's a powerful way to build complex types out of simpler ones without the need for classical inheritance.