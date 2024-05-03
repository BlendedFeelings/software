---
b: https://blendedfeelings.com/software/golang/functional-options.md
---

# Functional options 
is a pattern in Go (Golang) that allows you to create clean and flexible APIs for configuring objects without the need for a complex constructor or an explosion of constructors when the number of configuration parameters grows. The pattern was popularized by Dave Cheney and is widely used in Go codebases.

Here's how the functional options pattern works:

1. Define a struct that you want to configure.
2. Define an option type, which is a function that takes a pointer to your struct and returns an error (the error can be omitted if not needed).
3. Create option functions that implement the option type, each setting one or more configuration values on the struct.
4. Create a constructor function for your struct that accepts a variadic number of option functions and applies them to a new instance of your struct.

Here's an example of how to implement the functional options pattern in Go:

```go
package main

import "fmt"

// Config is the struct we want to configure.
type Config struct {
    Timeout int
    MaxConns int
    TLS bool
}

// Option is the type for configuration options.
type Option func(*Config) error

// WithTimeout sets the timeout in the Config.
func WithTimeout(timeout int) Option {
    return func(c *Config) error {
        c.Timeout = timeout
        return nil
    }
}

// WithMaxConns sets the maximum number of connections in the Config.
func WithMaxConns(maxConns int) Option {
    return func(c *Config) error {
        c.MaxConns = maxConns
        return nil
    }
}

// WithTLS enables TLS in the Config.
func WithTLS(tls bool) Option {
    return func(c *Config) error {
        c.TLS = tls
        return nil
    }
}

// NewConfig creates a new Config with the provided options.
func NewConfig(opts ...Option) (*Config, error) {
    config := &Config{
        Timeout: 10, // default timeout
        MaxConns: 100, // default max connections
        TLS: false, // default TLS setting
    }

    for _, opt := range opts {
        err := opt(config)
        if err != nil {
            return nil, err
        }
    }

    return config, nil
}

func main() {
    // Create a Config with custom timeout and max connections.
    config, err := NewConfig(
        WithTimeout(30),
        WithMaxConns(50),
    )
    if err != nil {
        fmt.Println("Error creating config:", err)
        return
    }

    fmt.Printf("Config: %+v\n", config)
}
```

In this example, the `NewConfig` function takes a variable number of `Option` functions. Each option function is applied to the `Config` struct to set the desired configuration. The functional options pattern provides a clean and flexible way to configure objects and is particularly useful when you have a large number of potential configuration parameters.