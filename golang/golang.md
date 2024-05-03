---
b: https://blendedfeelings.com/software/golang/golang.md
---

# Go
often referred to as Golang due to its domain name (golang.org), is an open-source programming language created by Google. It was designed by Robert Griesemer, Rob Pike, and Ken Thompson and officially released in 2009. Go is statically typed, compiled, and syntactically similar to C, but with memory safety, garbage collection, structural typing, and CSP-style concurrency.

Here are some key features of Go:

1. **Simplicity and Readability**: Go has a clean syntax with minimalistic features. This makes it easy to read and write.

2. **Concurrency Support**: Go has built-in support for concurrency with goroutines and channels. Goroutines are functions that can run concurrently, and channels are used to communicate between them.

3. **Fast Compilation**: Go compiles quickly to machine code yet has the convenience of garbage collection and the power of run-time reflection.

4. **Standard Library**: Go has a rich standard library that covers a wide range of areas, including HTTP server/client implementation, JSON encoding/decoding, and more.

5. **Tooling**: Go comes with a suite of tools for formatting code (`gofmt`), managing dependencies (`go mod`), running tests (`go test`), and more.

6. **Static Typing and Efficiency**: Go is statically typed, which helps catch errors at compile time. It is also efficient in terms of both execution speed and memory usage.

7. **Cross-Platform**: Go can be used to develop applications for various platforms, including Windows, macOS, Linux, and others.

Here's a simple "Hello, World!" program in Go:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

To run a Go program, you typically write the code in a file with a `.go` extension, and then use the `go run` command to compile and run it, or `go build` to compile it into an executable.

Go is widely used for backend development, cloud services, and other systems-level programming tasks where performance and concurrency are important. It has been adopted by many companies and has a growing ecosystem and community.