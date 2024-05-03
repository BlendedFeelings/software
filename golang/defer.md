---
b: https://blendedfeelings.com/software/golang/defer.md
---

# Defer in Go 
delays the execution of a function until a later time or event, like you might find in some asynchronous programming models. However, Go does have a `defer` statement that is used to ensure that a function call is performed later in the program's execution, usually for purposes of cleanup. `defer` is commonly used to ensure that resources are released in a timely manner, such as closing files or network connections.

When a `defer` statement is encountered, the function call specified is not executed immediately. Instead, it is placed onto a stack and executed when the surrounding function returns, either because it reached the end of its body, or because it encountered a return statement, or an error occurred. The deferred calls are executed in last-in-first-out order.

Here is an example of how `defer` is used in Go:

```go
package main

import (
	"fmt"
	"os"
)

func main() {
	// Open a file for reading
	file, err := os.Open("example.txt")
	if err != nil {
		panic(err)
	}

	// Defer the closing of the file until the surrounding function (main) returns
	defer file.Close()

	// Do something with the file
	// ...

	// When the main function returns, file.Close() will be called automatically
	fmt.Println("File will be closed automatically when the main function exits.")
}
```

In this example, the `defer file.Close()` statement ensures that the file is closed when the `main` function exits, regardless of whether it exits normally or due to an error. This helps to prevent resource leaks.

Remember that deferred function calls are executed even if a runtime panic occurs, which is useful for recovering from panics and for cleaning up resources gracefully.