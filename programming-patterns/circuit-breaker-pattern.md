---
b: https://blendedfeelings.com/software/programming-patterns/circuit-breaker-pattern.md
---

# Circuit Breaker Pattern 
is used to handle failures in distributed systems, such as microservices. It is used to prevent cascading failures and to provide a fallback mechanism when a service or a component fails. 
It works by wrapping a potentially failing operation with a circuit breaker object.The circuit breaker object monitors the operation and opens the circuit if the operation fails repeatedly. When the circuit is open, the circuit breaker returns a fallback value or throws an exception, without calling the operation. When the circuit is closed, the circuit breaker calls the operation normally.

Here's how the Circuit Breaker pattern works in the context of software:

**Closed State**: Initially, the circuit breaker is in the "Closed" state, allowing requests to pass through to the service or resource. Each successful request resets the failure count.

**Failure Detection**: If a request fails, the circuit breaker increments a failure counter. If the number of failures crosses a predefined threshold within a certain period, the circuit breaker transitions to the "Open" state.

**Open State**: In this state, the circuit breaker prevents any requests from being made to the service, usually by throwing an exception or returning an error. This gives the failing service time to recover. The circuit breaker remains in this state for a predefined "timeout" period.

**Half-Open State**: After the timeout period expires, the circuit breaker enters the "Half-Open" state. Here, it allows a limited number of test requests to pass through. If these requests are successful, it indicates that the service is back to normal, and the circuit breaker transitions back to the "Closed" state. If these requests fail, the circuit breaker returns to the "Open" state, and the timeout period begins again.

**Reset**: If the test requests in the "Half-Open" state are successful, the circuit breaker resets, moving back to the "Closed" state, and the system resumes normal operation.

The Circuit Breaker pattern is beneficial because it:

Prevents an application from repeatedly trying to execute an operation that's likely to fail.
Gives external services time to recover from faults.
Protects the system from cascading failures.
Can provide fallback mechanisms to maintain functionality even when a part of the system is down.

```java
// Circuit Breaker class
class CircuitBreaker {
    private int failureThreshold;
    private int resetTimeout;
    private int consecutiveFailures;
    private long lastFailureTime;
    private boolean isOpen;

    CircuitBreaker(int failureThreshold, int resetTimeout) {
        this.failureThreshold = failureThreshold;
        this.resetTimeout = resetTimeout;
        this.consecutiveFailures = 0;
        this.lastFailureTime = 0;
        this.isOpen = false;
    }

    void execute(Runnable command) {
        if (isOpen) {
            long now = System.currentTimeMillis();
            if (now - lastFailureTime > resetTimeout) {
                isOpen = false;
            } else {
                throw new RuntimeException("Circuit breaker is open");
            }
        }

        try {
            command.run();
            consecutiveFailures = 0;
        } catch (Exception e) {
            consecutiveFailures++;
            lastFailureTime = System.currentTimeMillis();
            if (consecutiveFailures >= failureThreshold) {
                isOpen = true;
            }
            throw e;
        }
    }
}

// Usage
CircuitBreaker circuitBreaker = new CircuitBreaker(3, 5000);
try {
    circuitBreaker.execute(() -> {
        // Call external service
    });
} catch (Exception e) {
    // Handle exception
}
```