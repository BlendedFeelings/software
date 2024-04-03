---
b: https://blendedfeelings.com/software/design/rate-limiting-pattern.md
---

# Rate Limiting pattern 
in software architecture is a technique used to control the amount of traffic that an application or a system can handle. It is designed to prevent overuse of resources by limiting how many requests a user, service, or IP address can make in a given amount of time. This pattern is particularly useful in preventing abuse, ensuring fair usage, and maintaining the quality of service during high traffic.

Here are key aspects of the Rate Limiting pattern:

1. **Thresholds**: Define the maximum number of requests that can be made within a certain time window (e.g., 100 requests per minute).

2. **Time Windows**: Establish the duration for which the rate limit applies (e.g., per minute, per hour, per day).

3. **Identification**: Determine how to identify the entities that are being limited (e.g., by IP address, API key, user account).

4. **Tracking**: Implement a mechanism to track the number of requests made by each entity within the time window.

5. **Enforcement**: Once an entity reaches its limit, enforce the limit by blocking additional requests, queuing them, or slowing down the response rate.

6. **Response**: Provide feedback to the sender of the request when a limit has been reached, often through HTTP status codes like `429 Too Many Requests`.

7. **Configuration**: Allow the rate limits to be configurable so that they can be adjusted based on the application's needs and the usage patterns.

8. **Scalability**: Ensure that the rate limiting mechanism can scale with the application, and consider distributed rate limiting strategies for distributed systems.

9. **Graceful Degradation**: Design the system so that it fails gracefully when limits are reached, rather than causing a service outage.

10. **Exemptions and Priorities**: Allow for exemptions (whitelisting) or different rate limits based on priority levels or subscription tiers.

Implementing rate limiting can be done in several ways:

- **Client-Side Rate Limiting**: Clients are responsible for tracking and respecting the rate limits. This is less common and relies on client cooperation.

- **Server-Side Rate Limiting**: The server tracks the number of requests and enforces the limits. This is the most common and reliable method.

- **Fixed Window Counting**: A simple approach where the count resets after a fixed time window. This can allow bursts of traffic at the window boundaries.

- **Sliding Window Log**: A more complex approach that records the timestamp of each request and ensures a smooth limit over time.

- **Token Bucket**: Allows for a burst of traffic up to a maximum "bucket size" and then refills the tokens at a steady rate.

- **Leaky Bucket**: Requests are processed at a steady rate, and excess requests are either queued or dropped if the bucket is full.

Rate limiting is often implemented using middleware in web frameworks, standalone rate limiting services, or as part of API gateways and load balancers. It's important to balance the rate limits to protect the system while providing a good user experience.