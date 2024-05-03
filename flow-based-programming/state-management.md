---
b: https://blendedfeelings.com/software/flow-based-programming/state-management.md
---

# State In Flow-Based Programming (FBP)
is managed locally within autonomous components that maintain their own state, communicate via immutable data packets, and avoid shared state to ensure data flow is predictable and side-effect-free.

1. **Component State**: Each component in an FBP application can maintain its own internal state. This state is encapsulated within the component and can be modified as IPs flow through the component. The state is typically local to the component and persists across the processing of multiple IPs.

2. **Immutable Data**: IPs are usually treated as immutable data structures. Once an IP is created and sent to the next component, it should not be altered. If a component needs to modify the data, it will typically create a new IP with the updated data and send it downstream. This immutability helps to avoid side effects and makes the data flow more predictable.

3. **No Shared State**: FBP discourages shared state between components. Instead, components communicate by sending and receiving IPs. This reduces the complexity associated with concurrent access to shared resources and helps to maintain clear boundaries between components.

4. **Stateful Components**: Some components are specifically designed to manage state. These stateful components can accumulate, store, and distribute state information as needed. For example, a component might aggregate data from multiple IPs before sending a result downstream.

5. **External State Management**: In some cases, FBP applications may interact with external systems for state management, such as databases or key-value stores. These systems can be used to persist state information that needs to be shared or maintained beyond the lifecycle of the application.

6. **Feedback Loops**: FBP networks can have feedback loops where the output of a component is fed back into it as input. This can be used to maintain state over time, such as in iterative algorithms or state machines.

7. **Concurrency and Isolation**: Since components run independently and concurrently, state management becomes easier as each component's state is isolated from others. This isolation helps prevent race conditions and makes the system more robust.

In summary, state in FBP is managed locally within components, with the flow of immutable IPs carrying data through the network. Stateful components and external systems can be used for more complex state management needs, and the design of FBP inherently promotes safe and isolated state handling due to its emphasis on component independence and data immutability.