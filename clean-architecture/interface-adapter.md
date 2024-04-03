---
b: https://blendedfeelings.com/software/clean-architecture/interface-adapter.md
---

# Interface Adapters
in the context of clean architecture, are the layer that sits between the use cases (application business rules) and the external world, which includes the user interface (UI), external services, and data storage. This layer is responsible for adapting data between the form that is most convenient for the use cases and entities, and the form that is most convenient for external agencies such as databases, web interfaces, or third-party APIs.

### Characteristics of Interface Adapters:

1. **Data Conversion**: They convert data from the format used by the use cases and entities (often domain models) to the format required by the external layers (e.g., view models for the UI, data transfer objects for APIs, or database models for persistence).

2. **External Interactions**: Interface adapters handle interactions with external systems, such as saving data to a database, sending an email, or calling a web service.

3. **Decoupling**: They decouple the use cases and entities from external concerns, allowing the business logic to remain independent of the UI, databases, and other external agencies.

4. **Separation of Concerns**: By separating the conversion and interaction logic into adapters, the system maintains a clean separation of concerns, which simplifies maintenance and evolution.

5. **Multiple Representations**: They enable the system to interact with multiple types of clients or data stores by providing different adapters for different types of interfaces.

### Components:

The interface adapters layer typically includes the following components:

- **Controllers**: In MVC (Model-View-Controller) architectures, controllers accept input from the UI, invoke use cases, and return responses back to the UI.

- **Presenters**: In MVP (Model-View-Presenter) or MVVM (Model-View-ViewModel) architectures, presenters or view models handle the preparation of data to be displayed by the view.

- **Gateways**: These are abstractions that encapsulate the logic for interacting with external systems or services, such as messaging systems, APIs, or databases.

- **Repositories**: Repositories abstract the data access logic, providing a collection-like interface for accessing domain entities while hiding the details of data storage.

### Implementation:

Here's an example of what interface adapters might look like in C#:

```csharp
// Controller in an MVC web application
public class OrderController : Controller
{
    private readonly IPlaceOrderUseCase _placeOrderUseCase;
    private readonly OrderPresenter _presenter;

    public OrderController(IPlaceOrderUseCase placeOrderUseCase, OrderPresenter presenter)
    {
        _placeOrderUseCase = placeOrderUseCase;
        _presenter = presenter;
    }

    [HttpPost]
    public ActionResult PlaceOrder(OrderViewModel orderViewModel)
    {
        var orderData = MapViewModelToOrderData(orderViewModel);
        _placeOrderUseCase.Execute(orderData);
        var response = _presenter.GetViewModel();
        return View(response);
    }

    private OrderData MapViewModelToOrderData(OrderViewModel viewModel)
    {
        // Mapping logic from OrderViewModel to OrderData
        // ...
    }
}

// Presenter for the order use case
public class OrderPresenter
{
    private OrderResponseModel _responseModel;

    public void Present(OrderResponse orderResponse)
    {
        // Convert OrderResponse (output from the use case) to OrderResponseModel (for the UI)
        _responseModel = new OrderResponseModel
        {
            OrderId = orderResponse.OrderId,
            Success = orderResponse.Success,
            Message = orderResponse.Message
        };
    }

    public OrderResponseModel GetViewModel()
    {
        return _responseModel;
    }
}

// OrderViewModel used by the UI
public class OrderViewModel
{
    // Properties corresponding to the UI form for placing an order
    // ...
}

// OrderResponseModel used to present the result back to the UI
public class OrderResponseModel
{
    public int OrderId { get; set; }
    public bool Success { get; set; }
    public string Message { get; set; }
}
```

In this example, the `OrderController` is an interface adapter that handles incoming HTTP requests, invokes the use case, and then uses the `OrderPresenter` to prepare the response for the UI. The `OrderViewModel` and `OrderResponseModel` are specific to the UI layer and are used to transfer data between the UI and the application's core logic.

Interface adapters should be designed to bridge the gap between the inner layers (use cases and entities) and the outer layers (UI, databases, etc.) without introducing dependencies that would violate the Dependency Rule of clean architecture.