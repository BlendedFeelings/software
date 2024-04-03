---
b: https://blendedfeelings.com/software/clean-architecture/example-user-registration.md
---

# User Registration 
end-to-end example of Clean Architecture. This example will be described in terms of the different layers and components involved, and for the sake of illustration, It uses C# as the programming language.

### Layers in Clean Architecture

1. **Entities Layer**: Contains the business objects of the application.
2. **Use Cases Layer**: Contains application-specific business rules.
3. **Interface Adapters Layer**: Converts data from the format most convenient for the use cases and entities, to the format most convenient for some external agency such as the Database or the Web.
4. **Frameworks & Drivers Layer**: Contains frameworks and tools such as the Database, the Web Framework, etc.

### Example: User Registration

#### Entities Layer

```csharp
public class User
{
    public Guid Id { get; private set; }
    public string Email { get; private set; }
    public string PasswordHash { get; private set; }

    public User(string email, string passwordHash)
    {
        Id = Guid.NewGuid();
        Email = email;
        PasswordHash = passwordHash;
    }

    // Additional methods related to the User entity can be added here
}
```

#### Use Cases Layer

```csharp
public interface IUserRepository
{
    void Add(User user);
    // Other user-related methods
}

public class RegisterUserUseCase
{
    private readonly IUserRepository _userRepository;
    private readonly IPasswordHasher _passwordHasher;

    public RegisterUserUseCase(IUserRepository userRepository, IPasswordHasher passwordHasher)
    {
        _userRepository = userRepository;
        _passwordHasher = passwordHasher;
    }

    public void Execute(string email, string password)
    {
        var passwordHash = _passwordHasher.HashPassword(password);
        var user = new User(email, passwordHash);
        _userRepository.Add(user);
    }
}
```

#### Interface Adapters Layer

```csharp
public class UserController
{
    private readonly RegisterUserUseCase _registerUserUseCase;

    public UserController(RegisterUserUseCase registerUserUseCase)
    {
        _registerUserUseCase = registerUserUseCase;
    }

    public void RegisterUser(string email, string password)
    {
        _registerUserUseCase.Execute(email, password);
        // You would typically return a result or response here.
    }
}

public class SqlUserRepository : IUserRepository
{
    // Implementation of the IUserRepository using SQL.
    public void Add(User user)
    {
        // Code to add the user to the database
    }
}

public interface IPasswordHasher
{
    string HashPassword(string password);
}

public class PasswordHasher : IPasswordHasher
{
    public string HashPassword(string password)
    {
        // Code to hash the password
        return "hashed_password";
    }
}
```

#### Frameworks & Drivers Layer

This layer would contain the actual implementations of interfaces like `IUserRepository` (e.g., `SqlUserRepository`) and any frameworks or tools you are using, such as ASP.NET for web applications, Entity Framework for ORM, etc.

#### Putting It All Together

In an actual application, you would wire up these components using dependency injection in your startup configuration. For example:

```csharp
public class Startup
{
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddTransient<IUserRepository, SqlUserRepository>();
        services.AddTransient<IPasswordHasher, PasswordHasher>();
        services.AddTransient<RegisterUserUseCase>();
        services.AddTransient<UserController>();
    }
}
```

This is a high-level example and doesn't include details like error handling, validation, or data transfer objects (DTOs), which you would typically include in a real-world application. The focus here is on the separation of concerns and the structure of the application according to Clean Architecture principles.