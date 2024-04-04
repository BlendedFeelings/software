---
b: https://blendedfeelings.com/software/python/variable.md
---

# Variables in Python
are used to store data values. Unlike some other programming languages, Python has no command for declaring a variable; a variable is created the moment you first assign a value to it. Variables do not need to be declared with any particular type, and can even change type after they have been set.

Here are some examples of how variables can be used in Python:

```python
# Assigning a value to a variable
x = 5
y = "Hello, World!"

# Variables can be re-assigned to different data types
x = "Now I'm a string"

# Python is case-sensitive. Variable 'a' is different from 'A'
a = 4
A = "Different variable than 'a'"

# You can also perform operations on variables
z = x + y  # This would raise an error because x is a string and y is an integer

# To fix the above error, you could convert x to an integer if it's a numeric string
x = "5"  # Now x is a numeric string
z = int(x) + y  # This will work if y is an integer

# You can also use variables in functions
def greet(name):
    print("Hello, " + name)

greet(y)  # This would print "Hello, Hello, World!"
```

Variables in Python are also dynamic in nature, which means you can reassign a variable to a different data type at any point. This is referred to as dynamic typing. Here's an example:

```python
variable = 10      # Initially an integer
variable = "Ten"   # Now it's a string
variable = 10.0    # Now it's a float
```

Variables that are declared inside a function or block are known as local variables, while variables that are declared outside of all functions or blocks are known as global variables.

### Local Variables
- Scope: Local variables are only accessible within the function or block where they are declared.
- Lifetime: Their lifetime is limited to the execution of the function. They are created when the function is called and destroyed when the function exits.
- Accessibility: They cannot be accessed from outside the function.

Example of a local variable:
```python
def my_function():
    local_var = 10  # This is a local variable
    print(local_var)

my_function()
# print(local_var)  # This would raise an error because local_var is not accessible outside the function
```

### Global Variables
- Scope: Global variables are accessible throughout the entire program, from any function or block.
- Lifetime: They are created when the program starts and destroyed when the program ends.
- Accessibility: They can be accessed and modified from any function, unless shadowed by a local variable with the same name.

Example of a global variable:
```python
global_var = 20  # This is a global variable

def my_function():
    print(global_var)

my_function()
print(global_var)  # This will print the global variable
```

#### Modifying Global Variables Inside a Function
To modify a global variable from within a function, you need to use the `global` keyword to declare that you intend to use the global variable, not a local one.

Example:
```python
global_var = 30

def my_function():
    global global_var
    global_var = 40

my_function()
print(global_var)  # This will print 40, because the global variable was modified
```

It's important to note that using global variables can make code harder to read and maintain. It's often better to pass variables as parameters to functions and return new values, rather than using global variables.

### Nested Functions Variables

The `nonlocal` keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function. Use `nonlocal` to declare that the variable is not local to the nested (enclosed) function, allowing you to modify the variable in the nearest enclosing scope that is not global.

```python
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"  # Modify the variable in the nearest enclosing scope

    inner()
    print(x)  # Output: nonlocal

outer()
```