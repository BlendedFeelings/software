---
b: https://blendedfeelings.com/software/programming-patterns/repository-pattern.md
---

# Repository Pattern
is a design pattern that mediates between the domain and data mapping layers of an application. It's a way to encapsulate the logic required to access data sources, providing a more abstract interface for accessing data. The pattern aims to separate the logic that retrieves data from business logic, which allows for more modular code and makes it easier to maintain and test.

Here’s how the Repository Pattern works:

1. **Abstraction**: The repository acts as an intermediary between the domain model (business logic) and data mapping layers, hiding the details of the data access code from the business logic.

2. **Decoupling**: By decoupling the business logic from data access code, the application becomes more robust. Changes to the data access logic do not affect the business logic, and vice versa.

3. **Testability**: With repositories acting as in-memory collections, it becomes easier to unit test the domain models without setting up an actual database.

4. **Centralization**: All the data access logic is centralized in repositories rather than being spread across multiple domain objects. This promotes code reuse and maintainability.

5. **Flexibility**: The pattern allows you to easily switch between different data sources or strategies because the business logic depends on abstractions (interfaces) rather than concrete implementations.

```java
public interface UserRepository {
    User findById(long id);
    List<User> findAll();
    void save(User user);
    void delete(User user);
}

class UserRepositoryImpl implements UserRepository {
    List<User> users = new ArrayList<>();

    User findById(long id) {
        return users
            .filter(user -> user.getId() == id)
            .first();
    }

    List<User> findAll() {
        return users;
    }

    void save(User user) {
        users.add(user);
    }

    void delete(User user) {
        users.remove(user);
    }
}

public class UserService {
    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public User findUserById(long id) {
        return userRepository.findById(id);
    }

    public List<User> findAllUsers() {
        return userRepository.findAll();
    }

    public void saveUser(User user) {
        userRepository.save(user);
    }

    public void deleteUser(User user) {
        userRepository.delete(user);
    }
}

```