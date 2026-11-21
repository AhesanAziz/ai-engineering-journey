# Python Fundamentals

A beginner-friendly introduction to Python covering output, data types, variables, comments, identifiers, user input, type conversion, literals, operators, and conditional statements.

---

## 1. Python Output

The `print()` function is used to display information on the screen.

### Basic Output

```python
print(7)
# Output: 7

print(7.7)
# Output: 7.7

print(True)
# Output: True

print("Hello", 10, 4.5, True)
# Output: Hello 10 4.5 True
```

### Using the `sep` Parameter

The `sep` parameter specifies the separator between multiple values.

```python
print("Hello", 10, 4.5, True, sep="/")
# Output: Hello/10/4.5/True
```

### Using the `end` Parameter

By default, `print()` ends with a newline (`\n`). The `end` parameter changes this behavior.

```python
print("Hello")
print("World")

# Output:
# Hello
# World
```

```python
print("Hello", end="-")
print("World")

# Output: Hello-World
```

---

## 2. Python Data Types

A data type determines the kind of value a variable can store.

### Numeric Data Types

**Integer (`int`)**

Stores whole numbers.

```python
a = 8
print(a)
print(type(a))

# Output:
# 8
# <class 'int'>
```

Python integers can store very large numbers. They are not limited to 32-bit or 64-bit integer ranges (although available memory still matters).

**Float (`float`)**

Stores decimal numbers.

```python
a = 7.5
print(a)
print(type(a))

# Output:
# 7.5
# <class 'float'>
```

Floating-point values can also represent infinity.

```python
print(1e309)
# Output: inf
```

**Complex (`complex`)**

Stores complex numbers containing real and imaginary parts.

```python
a = 5 + 6j
print(a)

# Output: (5+6j)
```

### Sequence Data Types

**String (`str`)**

Stores text.

```python
name = "Python"
print(name)

# Output: Python
```

**List (`list`)**

Stores multiple values in an ordered, mutable collection.

```python
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Output: [1, 2, 3, 4, 5]
```

**Tuple (`tuple`)**

Stores multiple values in an ordered, immutable collection.

```python
numbers = (1, 2, 3, 4, 5)
print(numbers)

# Output: (1, 2, 3, 4, 5)
```

### Set Data Type

**Set (`set`)**

Stores unique values. Sets are unordered and do not support indexing.

```python
numbers = {1, 2, 3, 4, 5}
print(numbers)

# Output: {1, 2, 3, 4, 5}
```

Duplicate values are automatically removed.

```python
numbers = {1, 2, 2, 3}
print(numbers)

# Output: {1, 2, 3}
```

Note: The order of set elements is not guaranteed.

### Dictionary Data Type

**Dictionary (`dict`)**

Stores data in key-value pairs.

```python
student = {
    "name": "Alex",
    "gender": "Male",
    "weight": 70
}

print(student)

# Output:
# {'name': 'Alex', 'gender': 'Male', 'weight': 70}
```

### Checking Data Types

The `type()` function identifies the data type of a value.

```python
print(type([1, 2, 3]))

# Output:
# <class 'list'>
```

---

## 3. Variables

A variable is a name that refers to a value stored in memory.

```python
name = "Alex"

a = 5
b = 6

print(name)
print(a + b)

# Output:
# Alex
# 11
```

### Static vs. Dynamic Typing

**Static Typing:**
- Variable types are explicitly declared or determined at compile time.
- Common in languages such as C and C++.

Example (C++):

```cpp
int a = 5;
```

**Dynamic Typing:**
- Python determines the type of a variable at runtime.
- We do not need to declare the variable's type explicitly.

Example (Python):

```python
a = 5
print(type(a))

# Output: <class 'int'>
```

### Static vs. Dynamic Binding

Binding refers to associating a variable name with an object or value.

**Dynamic Binding:**

A variable can refer to objects of different types during program execution.

```python
a = 5
print(a)

a = "Python"
print(a)

# Output:
# 5
# Python
```

**Static Binding (Simplified C++ Example):**

```cpp
int a = 5;
```

The variable's declared type remains `int`.

### Multiple Variable Declaration

**Separate Assignment:**

```python
a = 1
b = 2
c = 3

print(a, b, c)
# Output: 1 2 3
```

**Multiple Assignment:**

```python
a, b, c = 1, 2, 3

print(a, b, c)
# Output: 1 2 3
```

**Assigning the Same Value:**

```python
a = b = c = 5

print(a, b, c)
# Output: 5 5 5
```

---

## 4. Comments

Comments are used to explain code. Python ignores comments during execution.

### Single-Line Comments

Use `#` to write a comment.

```python
# This is a comment
# This is another comment

a = 4
b = 6  # Inline comment

print(a + b)

# Output: 10
```

### Multi-Line Comments

Python does not have a dedicated multi-line comment syntax.

You can use multiple `#` lines:

```python
# This is the first line.
# This is the second line.
# This is the third line.
```

Triple-quoted strings are commonly used for documentation strings (docstrings) when placed in appropriate locations, such as at the beginning of a function or module.

---

## 5. Keywords and Identifiers

### Keywords

Keywords are reserved words in Python that have special meanings.

Examples:

- `if`
- `else`
- `for`
- `while`
- `def`
- `class`
- `return`
- `True`
- `False`
- `None`
- `and`
- `or`
- `not`
- `import`

Keywords cannot be used as variable names.

### Identifiers

Identifiers are names used to identify variables, functions, classes, etc.

**Rules for Naming Identifiers:**

1. An identifier cannot start with a digit.
2. It can contain letters, digits, and underscores (`_`).
3. Special characters such as `@`, `$`, and `%` are not allowed.
4. Python keywords cannot be used as identifiers.
5. Identifiers are case-sensitive.

Examples:

```python
name = "Alex"
age = 22
_student = "John"
```

An underscore by itself is also a valid identifier.

```python
_ = "Python"
print(_)

# Output: Python
```

---

## 6. User Input

The `input()` function allows users to enter information while a program is running.

### Basic Input

```python
email = input("Enter your email: ")
print(email)
```

Example input:

```text
Enter your email: example@gmail.com
```

Example output:

```text
example@gmail.com
```

**Important:** The `input()` function always returns a string (`str`), regardless of what the user enters.

### Taking Numeric Input

If we want to perform mathematical operations, we need to convert the input into a numeric data type.

```python
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

result = first_number + second_number

print(result)
print(type(first_number))
```

Example input:

```text
Enter first number: 56
Enter second number: 67
```

Output:

```text
123
<class 'int'>
```

---

## 7. Type Conversion

Type conversion means changing a value from one data type to another.

There are two types:

### Implicit Type Conversion

Python automatically converts one data type into another when appropriate.

```python
a = 5
b = 5.6

result = a + b

print(result)
print(type(a), type(b))
print(type(result))

# Output:
# 10.6
# <class 'int'> <class 'float'>
# <class 'float'>
```

Here, Python automatically converts the integer into a float during the calculation.

### Explicit Type Conversion

The programmer manually converts a value using functions such as `int()`, `float()`, and `str()`.

**Integer to String:**

```python
a = 5
print(str(a))

# Output: 5
```

**Integer to Float:**

```python
a = 4
print(float(a))

# Output: 4.0
```

**String to Integer:**

```python
a = "25"
print(int(a))

# Output: 25
```

**String to Float:**

```python
a = "5.5"
print(float(a))

# Output: 5.5
```

### Invalid Type Conversion or Operations

Not every conversion or operation is valid.

```python
# print(4 + "4")
```

This raises a `TypeError` because Python cannot directly add an integer and a string.

Another example:

```python
# int(4 + 5j)
```

This raises a `TypeError` because a complex number cannot be directly converted to an integer.

---

## 8. Python Literals

Literals are fixed values written directly in the source code.

### Integer Literals

Python supports different number systems.

```python
a = 0b1010  # Binary
b = 100     # Decimal
c = 0o310   # Octal
d = 0x12c   # Hexadecimal

print(a, b, c, d)

# Output:
# 10 100 200 300
```

Prefixes:

- `0b` = Binary
- `0o` = Octal
- `0x` = Hexadecimal

### Float Literals

```python
float_1 = 10.5
float_2 = 1.5e2   # 1.5 × 10²
float_3 = 1.5e-3  # 1.5 × 10⁻³

print(float_1, float_2, float_3)

# Output:
# 10.5 150.0 0.0015
```

### Complex Literals

The letter `j` represents the imaginary part of a complex number.

```python
x = 3.14j

print(x)
print(x.imag)
print(x.real)

# Output:
# 3.14j
# 3.14
# 0.0
```

### String Literals

Strings can be written using single quotes, double quotes, or triple quotes.

```python
string_1 = 'This is Python'
string_2 = "This is Python"

char = "C"

multiline_string = """This is a
multi-line string."""

print(string_1)
print(string_2)
print(char)
print(multiline_string)
```

Python does not have a separate character data type. A single character is also a string.

### Unicode Strings

Python strings support Unicode characters.

```python
emoji = "\U0001F600"

print(emoji)

# Output: 😀
```

### Raw Strings

Raw strings use the `r` prefix. They treat backslashes as literal characters rather than interpreting most escape sequences.

```python
raw_string = r"Hello\nWorld"

print(raw_string)

# Output:
# Hello\nWorld
```

### Boolean Literals

Python has two Boolean values:

- `True`
- `False`

They represent logical truth values.

Interestingly, Boolean values behave like integers in arithmetic operations.

```python
a = True + 4
b = False + 10

print("a:", a)
print("b:", b)

# Output:
# a: 5
# b: 10
```

`True` behaves like `1`, and `False` behaves like `0`.

### None Literal

`None` represents the absence of a value.

```python
result = None

print(result)

# Output: None
```

It is commonly used to represent an empty or unavailable result.

---

## 9. Python Operators

Operators are symbols or keywords used to perform operations on values and variables.

### 1. Arithmetic Operators

Used for mathematical calculations.

| Operator | Meaning | Example |
| :--- | :--- | :--- |
| `+` | Addition | `5 + 2 = 7` |
| `-` | Subtraction | `5 - 2 = 3` |
| `*` | Multiplication | `5 * 2 = 10` |
| `/` | Division | `5 / 2 = 2.5` |
| `//` | Floor Division | `5 // 2 = 2` |
| `%` | Modulus (Remainder) | `5 % 2 = 1` |
| `**` | Exponentiation | `5 ** 2 = 25` |

### 2. Relational (Comparison) Operators

Used to compare two values. They return either `True` or `False`.

| Operator | Meaning |
| :--- | :--- |
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Example:

```python
a = 10
b = 5

print(a > b)
print(a == b)
print(a != b)

# Output:
# True
# False
# True
```

### 3. Logical Operators

Used to combine or reverse Boolean conditions.

| Operator | Meaning |
| :--- | :--- |
| `and` | True if both conditions are true |
| `or` | True if at least one condition is true |
| `not` | Reverses the Boolean result |

Example:

```python
a = 10

print(a > 5 and a < 20)
print(a < 5 or a == 10)
print(not(a > 5))

# Output:
# True
# True
# False
```

### 4. Bitwise Operators

Bitwise operators work on the binary representation of integers.

| Operator | Meaning |
| :--- | :--- |
| `&` | Bitwise AND |
| `\|` | Bitwise OR |
| `^` | Bitwise XOR |
| `~` | Bitwise NOT |
| `<<` | Left Shift |
| `>>` | Right Shift |

Example:

```python
a = 5  # Binary: 0101
b = 3  # Binary: 0011

print(a & b)
print(a | b)
print(a ^ b)
print(a << 1)
print(a >> 1)

# Output:
# 1
# 7
# 6
# 10
# 2
```

### 5. Assignment Operators

Used to assign values to variables and update existing values.

| Operator | Example | Equivalent |
| :--- | :--- | :--- |
| `=` | `a = 5` | Assign 5 |
| `+=` | `a += 2` | `a = a + 2` |
| `-=` | `a -= 2` | `a = a - 2` |
| `*=` | `a *= 2` | `a = a * 2` |
| `/=` | `a /= 2` | `a = a / 2` |
| `//=` | `a //= 2` | `a = a // 2` |
| `%=` | `a %= 2` | `a = a % 2` |
| `**=` | `a **= 2` | `a = a ** 2` |

Example:

```python
a = 10
a += 5

print(a)

# Output: 15
```

### 6. Membership Operators

Used to check whether a value exists inside a sequence or collection.

| Operator | Meaning |
| :--- | :--- |
| `in` | Checks whether a value exists |
| `not in` | Checks whether a value does not exist |

Example:

```python
name = "Python"

print("P" in name)
print("z" not in name)

# Output:
# True
# True
```

---

## 10. If-Else Statements

Conditional statements allow a program to make decisions based on conditions.

### Basic If Statement

Executes a block of code only when the condition is true.

```python
age = 20

if age >= 18:
    print("You are an adult.")

# Output:
# You are an adult.
```

### If-Else Statement

Executes one block when the condition is true and another when it is false.

```python
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Output:
# You are a minor.
```

### If-Elif-Else Statement

Used when multiple conditions need to be checked.

```python
marks = 75

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")

# Output:
# Grade B
```

Python uses indentation to define blocks of code. Proper indentation is mandatory.

---

## Quick Revision

| Topic | Main Concept |
| :--- | :--- |
| Output | `print()` |
| Data Types | `int`, `float`, `str`, `list`, `tuple`, `set`, `dict`, etc. |
| Variables | Names that refer to values |
| Comments | `#` |
| Keywords | Reserved words |
| Identifiers | Names of variables, functions, and classes |
| User Input | `input()` |
| Type Conversion | `int()`, `float()`, `str()` |
| Literals | Fixed values in source code |
| Operators | Perform operations |
| If-Else | Conditional execution |

## Important Beginner Reminders

1. Python is dynamically typed.
2. `input()` always returns a string.
3. Lists are mutable; tuples are immutable.
4. Sets store unique values and do not support indexing.
5. Dictionaries store key-value pairs.
6. Python uses indentation instead of curly braces to define code blocks.
7. `==` compares values, whereas `=` assigns values.
8. `True` and `False` are Boolean values.
9. `None` represents the absence of a value.
10. Python is case-sensitive.

---

*End of Python Fundamentals Notes.*