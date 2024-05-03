---
b: https://blendedfeelings.com/software/golang/table-driven-tests.md
---

# Table-driven tests in Go 
are a common pattern for writing tests where you define a series of test cases in a table (usually a slice of structs) and then iterate over them in a loop. Each entry in the table represents a test case with its own set of inputs and expected outputs.

Here's a step-by-step guide on how to write table-driven tests in Go:

1. **Import the testing package**: You need to import Go's `testing` package to write tests.

2. **Define your test cases**: Create a slice of structs, where each struct represents a test case with fields for inputs and the expected result.

3. **Write the test function**: Write a test function that iterates over the slice of test cases, calling the function you want to test with each set of inputs and comparing the result to the expected outcome.

4. **Run the test**: Use the `go test` command to run your test function.

Here is an example of a table-driven test in Go:

```go
package yourpackage

import "testing"

// Function you want to test
func Add(a, b int) int {
    return a + b
}

// Define a struct for your test cases
type addTest struct {
    name     string
    a        int
    b        int
    expected int
}

// Write the table-driven test function
func TestAdd(t *testing.T) {
    // Define your test cases
    tests := []addTest{
        {"add positives", 1, 2, 3},
        {"add negatives", -1, -2, -3},
        {"add mixed", -1, 1, 0},
    }

    // Iterate over the test cases
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            // Call the function with the test case inputs
            result := Add(tt.a, tt.b)

            // Check if the result is as expected
            if result != tt.expected {
                t.Errorf("Add(%d, %d) = %d; want %d", tt.a, tt.b, result, tt.expected)
            }
        })
    }
}
```

In this example, we're testing a simple `Add` function with three test cases: adding two positive numbers, two negative numbers, and a positive and a negative number. Each test case is named, which helps identify which cases pass or fail when running the tests.

To run your tests, navigate to the directory containing your test file in the terminal and execute `go test`. This will run all tests in the current directory. If you want to run a specific test, you can use `go test -run TestAdd`, where `TestAdd` is the name of the test function.