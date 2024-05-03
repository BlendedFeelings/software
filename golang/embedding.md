---
b: https://blendedfeelings.com/software/golang/embedding.md
---

# Embedding in Go (Golang) 
is a concept where one struct type can include another type without using inheritance. This allows for a sort of composition where methods of the embedded type become part of the outer type. Embedding can be done with both struct types and interface types.

Here's an example of embedding with structs:

```go
package main

import (
	"fmt"
)

type Engine struct {
	Power int // Horsepower of the engine
}

// Start is a method of Engine
func (e Engine) Start() {
	fmt.Println("Engine has started with power:", e.Power)
}

// Stop is a method of Engine
func (e Engine) Stop() {
	fmt.Println("Engine has stopped.")
}

// Car embeds Engine
type Car struct {
	Engine // Embedding Engine struct
	Model  string
}

func main() {
	car := Car{
		Engine: Engine{Power: 150},
		Model:  "Ford Mustang",
	}

	// You can call methods of the embedded Engine directly on Car
	car.Start()
	car.Stop()

	// Accessing fields of the embedded Engine
	fmt.Println("Car model:", car.Model, "with power:", car.Power)
}
```

In this example, `Car` embeds `Engine`. This means that `Car` now has access to the methods of `Engine` (`Start` and `Stop`) and can call them as if they were defined on `Car` itself. Additionally, the fields of `Engine` can be accessed directly through `Car`.

Here's an example of embedding with interfaces:

```go
package main

import (
	"fmt"
)

// Writer is an interface with one method
type Writer interface {
	Write([]byte) (int, error)
}

// ConsoleWriter implements the Writer interface
type ConsoleWriter struct{}

// Write is the method implementation of Writer for ConsoleWriter
func (cw ConsoleWriter) Write(data []byte) (int, error) {
	n, err := fmt.Println(string(data))
	return n, err
}

// Logger embeds the Writer interface
type Logger struct {
	Writer // Embedding Writer interface
}

func main() {
	log := Logger{
		Writer: ConsoleWriter{},
	}

	// We can call the Write method directly on Logger
	log.Write([]byte("Hello, World!"))
}
```

In this example, `Logger` embeds the `Writer` interface. This means that any type that satisfies the `Writer` interface can be assigned to `Logger.Writer`, and the `Write` method can be called on `Logger` as if it were its own method.

Embedding is a powerful feature in Go that promotes composition over inheritance, allowing for flexible and maintainable code design.