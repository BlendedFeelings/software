---
b: https://blendedfeelings.com/software/design/model-view-controller-mvc-pattern.md
---

# Model-View-Controller (MVC) 
is a software architectural pattern commonly used for developing user interfaces that divides an application into three interconnected components. This is done to separate internal representations of information from the ways information is presented to and accepted from the user. The three components are:

1. **Model**: The central component of the pattern. It is the application's dynamic data structure, independent of the user interface. It directly manages the data, logic, and rules of the application.

2. **View**: Any representation of information such as a chart, diagram or table. Multiple views of the same information are possible, such as a bar chart for management and a tabular view for accountants.

3. **Controller**: Accepts input and converts it to commands for the model or view. It acts as an intermediary between the Model and the View, and is responsible for taking the input from the user, processing it (which may involve asking the Model to change its state), and then updating the View accordingly.

The flow of control in an MVC application is as follows:

1. The user interacts with the View, such as clicking a button or entering data into a form.
2. The Controller receives the input from the View, often as a result of user actions, and translates that input into a form that can be used by the Model or View.
3. If the input involves changing the state of the application, the Controller will interact with the Model, possibly updating it.
4. The Model notifies the View of any changes to its state (usually through a notification mechanism).
5. The View updates the user interface based on the changes to the Model.

This separation of concerns allows for modular development; different developers can work on the Model, View, and Controller independently. It also makes the application easier to test and maintain. The MVC pattern is widely used in web applications, with many frameworks such as Ruby on Rails, Django (Python), and ASP.NET MVC providing a structured way to implement MVC.