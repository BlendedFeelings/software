# `GOMAXPROCS` in Go
is an environment variable that determines the maximum number of operating system threads that can execute user-level Go code simultaneously. It effectively sets the maximum number of CPU cores that the Go runtime will use for parallel execution of Go goroutines.

The default value of `GOMAXPROCS` is the number of CPU cores available on the machine. However, you can change this value to control the level of parallelism for Go programs. This can be useful for optimizing performance, particularly in environments with many CPU cores or when you want to limit the resource usage of a Go application.

You can set `GOMAXPROCS` in two ways:

1. **Environment Variable**: You can set the `GOMAXPROCS` environment variable before running a Go program. For example, in a Unix-like shell:

   ```sh
   export GOMAXPROCS=4
   ./my_go_program
   ```

   This sets the `GOMAXPROCS` to 4, instructing the Go runtime to use up to 4 OS threads for executing goroutines.

2. **Runtime Package**: You can also set `GOMAXPROCS` programmatically within a Go program by using the `runtime` package:

   ```go
   package main

   import (
   	"fmt"
   	"runtime"
   )

   func main() {
   	// Set GOMAXPROCS to 4.
   	runtime.GOMAXPROCS(4)

   	// Your program code here
   }
   ```

   The `runtime.GOMAXPROCS()` function sets the maximum number of CPUs that can be executing simultaneously and returns the previous setting. If the argument to `runtime.GOMAXPROCS()` is less than 1, it does not change the current setting.

It's important to note that setting `GOMAXPROCS` does not guarantee that your program will always use that many OS threads. The actual number of threads used at any given time is determined by the Go scheduler, which may use fewer threads if there aren't enough runnable goroutines to require more. Adjusting `GOMAXPROCS` can be a tool for performance tuning, but it's often best to let the Go runtime manage concurrency with its default settings unless you have a specific reason to change it.