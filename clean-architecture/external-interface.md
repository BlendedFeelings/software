---
b: https://blendedfeelings.com/software/clean-architecture/external-interface.md
---

# External Interfaces
in clean architecture, refer to the boundaries that define how an application interacts with external systems, services, or components. These interfaces are part of the outer layers of the architecture and are designed to communicate with the outside world while keeping the application core independent and isolated from external changes.

### Characteristics of External Interfaces:

1. **Abstraction**: External interfaces provide an abstract way for the application to interact with external agencies, such as third-party APIs, databases, file systems, or hardware devices.

2. **Separation of Concerns**: They separate the concerns of external integration from the core business logic, allowing each to evolve independently.

3. **Adaptation**: External interfaces adapt the data and protocols used by external agencies to the data structures and requirements of the application's core.

4. **Contract**: They define a contract that the external agencies must adhere to for interaction with the application. This contract includes the data formats, operations, and communication protocols.

5. **Interchangeability**: By using interfaces, the application can switch between different implementations of external services without affecting the core logic.

6. **Isolation**: They help isolate the core application from potential changes or failures in external systems, improving the overall resilience of the application.

### Implementation:

External interfaces are typically implemented using interface adapters, which include gateways, proxies, and clients that encapsulate the logic for communicating with external systems. Here's an example of how external interfaces might be implemented in C#:

```csharp
// External interface for a payment gateway
public interface IPaymentGateway
{
    PaymentResult ProcessPayment(PaymentDetails paymentDetails);
}

// Concrete implementation of the payment gateway that interacts with an external service
public class StripePaymentGateway : IPaymentGateway
{
    public PaymentResult ProcessPayment(PaymentDetails paymentDetails)
    {
        // Logic to interact with the Stripe payment API
        // ...
        return new PaymentResult
        {
            Success = true,
            TransactionId = "txn_123456789"
        };
    }
}

// Data structure for passing payment details to the payment gateway
public class PaymentDetails
{
    public string CreditCardNumber { get; set; }
    public string ExpiryDate { get; set; }
    public string Cvv { get; set; }
    public decimal Amount { get; set; }
    // Other payment-related details
}

// Data structure for the result of a payment transaction
public class PaymentResult
{
    public bool Success { get; set; }
    public string TransactionId { get; set; }
    // Other result-related details
}
```

In this example, `IPaymentGateway` is an external interface that defines how the application interacts with a payment service. `StripePaymentGateway` is a concrete implementation that interacts with the Stripe API, converting the application's payment details into the format required by Stripe and processing the payment.

External interfaces should be designed to encapsulate all the details of external communication, providing a clean and simple way for the application's core to interact with the outside world without being affected by external complexities.