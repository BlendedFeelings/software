---
b: https://blendedfeelings.com/software/design/compensating-transaction-pattern.md
---

# Compensating Transaction pattern 
is a software architecture pattern used to ensure system consistency when conducting operations that span multiple services or data sources, which may not support distributed transactions. This pattern is particularly useful in microservices architectures where each service manages its own data and transactions.

Here's an overview of how the Compensating Transaction pattern works:

1. **Local Transactions**: Each service performs its part of the overall process in a local transaction. If the service can successfully complete its part of the process, it records this fact along with any necessary information to undo the action if needed later.

2. **Compensation Logic**: Each service includes compensation logic, which is the code necessary to undo the effects of a previous operation. This logic is crucial because it allows the system to revert to its original state if the overall process cannot be completed successfully.

3. **Saga**: A saga is a sequence of local transactions where each transaction updates data within a single service. If a local transaction fails, the saga executes compensating transactions for all previously completed local transactions to roll back the changes.

4. **Coordinator**: A coordinator (or orchestration service) is often used to manage the saga, especially in complex scenarios. It initiates each local transaction, monitors their success or failure, and triggers compensating transactions as needed.

5. **Eventual Consistency**: The system may not be consistent at all times during the process, but it should eventually reach a consistent state, either by completing all local transactions successfully or by executing all necessary compensating transactions.

Here's an example scenario illustrating the Compensating Transaction pattern:

- A user wants to book a holiday package that includes a flight, a hotel, and a car rental.
- The booking service starts a saga to handle this multi-step transaction.
- It first reserves a flight (local transaction in the flight service).
- Then it books a hotel room (local transaction in the hotel service).
- Finally, it attempts to reserve a car (local transaction in the car rental service).
- If the car reservation fails, the booking service triggers compensating transactions:
  - It cancels the hotel booking (compensation in the hotel service).
  - It releases the flight reservation (compensation in the flight service).
- The system is now back to its original state, and the user is informed that the holiday package could not be booked.

The Compensating Transaction pattern provides a way to maintain data consistency without relying on distributed transactions, which can be complex and less performant. However, it requires careful design and implementation of compensation logic and may introduce complexity in terms of state management and coordination.