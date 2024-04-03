---
b: https://blendedfeelings.com/software/programming-patterns/throttling-pattern.md
---

# Throttling
is used to limit the rate at which requests are made to a system or API. It is used to prevent excessive requests from overwhelming the system and causing performance issues or downtime.

Examples
**Request-based throttling**: This limits the number of requests that can be made within a certain time period.
**Connection-based throttling**: This limits the number of connections that can be made to a system within a certain time period from a single IP address.

```java
class MyClass
{
    int maxRequests = 10
    int timeIntervalInSeconds = 60
    int requestCount = 0
    int lastRequestTime = CurrentTime()

    void MakeRequest()
    {
        // Check if the maximum number of requests has been reached
        if (requestCount >= maxRequests)
        {
            // Calculate the time remaining until the next request can be made
            timeSinceLastRequest = CurrentTime() - lastRequestTime
            timeToWait = timeIntervalInSeconds - timeSinceLastRequest
            wait(timeToWait) // Wait until the next request can be made

            // Reset the request counter and update the timestamp
            requestCount = 0
            lastRequestTime = CurrentTime()
        }

        // Make the request
        Request()

        requestCount += 1
        lastRequestTime = CurrentTime()
    }
}
```