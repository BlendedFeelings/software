---
b: https://blendedfeelings.com/software/clean-architecture/independent-of-ui.md
---

# Independent of UI 
in clean architecture asserts that the user interface (UI) is just one of many possible ways to interact with the application, and it should be possible to change it without affecting the core business logic. This principle has several key benefits:

1. **Flexibility**: By decoupling the UI from the core logic, you can change the UI without needing to change the business rules or data models. This flexibility allows you to support multiple interfaces (web, mobile, desktop, CLI, etc.) using the same application core.

2. **Maintainability**: When the UI is independent, the application becomes easier to maintain because UI changes are often more frequent due to user feedback, design updates, or platform-specific requirements. The separation ensures that these frequent changes do not ripple through the entire codebase.

3. **Testability**: It's easier to test business logic when it's not mixed with UI code. Business logic can be tested using automated tests without the need for complex UI automation frameworks.

4. **Reusability**: The core application logic can be reused across different UIs. For example, the same business rules could be applied to both a web application and a mobile app without duplication of code.

5. **Simplified Development**: Different teams can work on the UI and the core application logic simultaneously without stepping on each other's toes. This can lead to faster development cycles and less coordination overhead.

To achieve UI independence, clean architecture typically involves the following layers:

- **Entities**: These are the high-level business objects of the application.
- **Use Cases**: These encapsulate the application-specific business rules and are independent of the UI.
- **Interface Adapters**: This layer contains controllers, presenters, and gateways that translate data between the use cases and the UI or external systems.
- **UI**: The outermost layer where the user interface resides. It could be any type of interface, such as a web page, a mobile app, or a command-line interface.

By following the Dependency Rule, which states that source code dependencies can only point inwards, the UI layer depends on the interface adapters, which in turn depend on the use cases and entities. This ensures that the UI can be easily changed or replaced without affecting the inner layers.

In practice, this separation is often achieved by using patterns like Model-View-Controller (MVC), Model-View-Presenter (MVP), or Model-View-ViewModel (MVVM), where the model (business logic and data) is kept separate from the view (UI) and the controller/presenter/viewmodel acts as an intermediary.