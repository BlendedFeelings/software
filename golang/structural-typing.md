---
b: https://blendedfeelings.com/software/golang/structural-typing.md
---

# Structural typing 
is a way of determining type compatibility based on the structure of the types involved, rather than their explicit declarations or inheritance relationships. In contrast to nominal typing, where types must be explicitly declared to be compatible (usually through inheritance), structural typing allows for type compatibility if two types have the same structure, even if they have different names or no declared relationship at all.

In Go (also known as Golang), structural typing manifests through interfaces. An interface in Go specifies a method set, which is simply a collection of method signatures. A type is said to implement an interface if it has methods with the same signatures as all the methods in the interface's method set.

Here's an example to illustrate structural typing in Go:

```go
package main

import "fmt"

// Define an interface with a method set
type Talker interface {
    Talk() string
}

// Define a type that implements the method set of the interface
type Dog struct{}

func (d Dog) Talk() string {
    return "Woof!"
}

// Define another type that also implements the method set of the interface
type Robot struct{}

func (r Robot) Talk() string {
    return "Beep boop"
}

// A function that takes a Talker interface
func Speak(t Talker) {
    fmt.Println(t.Talk())
}

func main() {
    d := Dog{}
    r := Robot{}

    // Both Dog and Robot implement Talker, so they can be passed to Speak
    Speak(d) // Outputs: Woof!
    Speak(r) // Outputs: Beep boop
}
```

In this example, both `Dog` and `Robot` types implement the `Talker` interface because they both have a `Talk` method with the same signature as the one defined in the `Talker` interface. They do this without explicitly stating that they implement the interface (which is a characteristic of structural typing).

The `Speak` function accepts any type that satisfies the `Talker` interface. When it's called with an instance of `Dog` or `Robot`, the Go runtime checks whether the provided value has all the methods required by the `Talker` interface. Since both `Dog` and `Robot` have the `Talk` method, they are both valid arguments to the `Speak` function.

This approach provides a flexible and decoupled way of designing systems, as you can create new types that satisfy existing interfaces without modifying the interfaces or other types that use them. It also encourages the design of small, focused interfaces, which is a common Go idiom encapsulated in the phrase "accept interfaces, return structs."