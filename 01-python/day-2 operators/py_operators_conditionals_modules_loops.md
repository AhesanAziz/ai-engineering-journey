# Python Basics: Operators, Conditionals, Modules & Loops

A structured reference guide covering fundamental Python concepts, complete with executable code examples.

---

## 1. Operators in Python

- **Arithmetic Operators**
- **Relational Operators**
- **Logical Operators**
- **Bitwise Operators**
- **Assignment Operators**
- **Membership Operators**

```python
# Arithmetic Operators
print(5 + 6)   # Addition: 11
print(5 - 6)   # Subtraction: -1
print(5 * 6)   # Multiplication: 30
print(5 / 2)   # Division (float): 2.5
print(5 // 2)  # Floor Division: 2
print(5 % 2)   # Modulus (remainder): 1
print(5 ** 2)  # Exponentiation: 25

# Relational Operators
print(4 > 5)   # False
print(4 < 5)   # True
print(4 >= 4)  # True
print(4 <= 4)  # True
print(4 == 4)  # True
print(4 != 4)  # False

# Logical Operators
print(1 and 0) # 0
print(1 or 0)  # 1
print(not 1)   # False

# Bitwise Operators
print(2 & 3)   # Bitwise AND: 2
print(2 | 3)   # Bitwise OR: 3
print(2 ^ 3)   # Bitwise XOR: 1
print(~3)      # Bitwise NOT: -4
print(4 >> 2)  # Right Shift: 1
print(5 << 2)  # Left Shift: 20

# Assignment Operators
a = 2
a %= 2         # Equivalent to: a = a % 2
print(a)       # 0

# Membership Operators
print('D' not in 'Delhi')      # False
print(1 in [2, 3, 4, 5, 6])    # False
```

### Practice Program: Sum of a 3-Digit Number
```python
# Find the sum of digits of a 3-digit number entered by the user
number = int(input('Enter a 3-digit number: '))

# Extract last digit (e.g., 345 % 10 -> 5)
digit_1 = number % 10
number = number // 10

# Extract middle digit (e.g., 34 % 10 -> 4)
digit_2 = number % 10
number = number // 10

# Extract first digit (e.g., 3 % 10 -> 3)
digit_3 = number % 10

print("Sum of digits:", digit_1 + digit_2 + digit_3)
```

---

## 2. Conditional Statements (`if-elif-else`)

### Example 1: User Login Simulation
```python
# Dummy credentials for demonstration
VALID_EMAIL = 'user@example.com'
VALID_PASSWORD = 'password123'

email = input('Enter email: ')
password = input('Enter password: ')

if email == VALID_EMAIL and password == VALID_PASSWORD:
    print('Welcome!')
elif email == VALID_EMAIL and password != VALID_PASSWORD:
    print('Incorrect password.')
    password = input('Enter password again: ')
    if password == VALID_PASSWORD:
        print('Welcome, finally!')
    else:
        print('Access denied. Too many failed attempts.')
else:
    print('Invalid credentials.')
```

### Example 2: Find the Minimum of 3 Numbers
```python
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

if a < b and a < c:
    print('Smallest is:', a)
elif b < c:
    print('Smallest is:', b)
else:
    print('Smallest is:', c)
```

### Example 3: Menu-Driven ATM Interface
```python
menu = input("""
Hi! How can I help you?
1. Enter 1 for PIN change
2. Enter 2 for balance check
3. Enter 3 for withdrawal
4. Enter 4 for exit
Choice: """)

if menu == '1':
    print('Proceeding to PIN change...')
elif menu == '2':
    print('Checking account balance...')
elif menu == '3':
    print('Proceeding to withdrawal...')
else:
    print('Exiting. Thank you!')
```

---

## 3. Built-in Modules in Python

- `math`
- `keyword`
- `random`
- `datetime`

```python
import math
import keyword
import random
import datetime

# Math module
print("Square root of 196:", math.sqrt(196))

# Keyword module
print("Python Keywords:", keyword.kwlist)

# Random module
print("Random integer (1-100):", random.randint(1, 100))

# Datetime module
print("Current Date & Time:", datetime.datetime.now())

# Note: You can run help('modules') in an interactive shell to view all installed modules.
```

---

## 4. Loops in Python

### `while` Loops

#### Multiplication Table
```python
number = int(input('Enter a number for multiplication table: '))
i = 1

while i < 11:
    print(f"{number} * {i} = {number * i}")
    i += 1
```

#### `while` Loop with `else`
```python
x = 1
while x < 3:
    print(x)
    x += 1
else:
    print('Limit crossed')
```

#### Number Guessing Game
```python
import random

jackpot = random.randint(1, 100)
guess = int(input('Guess a number between 1 and 100: '))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print('Wrong! Guess higher.')
    else:
        print('Wrong! Guess lower.')

    guess = int(input('Guess again: '))
    counter += 1
else:
    print('Correct guess!')
    print('Total attempts:', counter)
```

### `for` Loops

#### Basic Iteration
```python
for i in [1, 2, 3, 4, 5]:
    print(i)
```

#### Population Growth/Decay Calculation
*Problem: The current population of a town is 10,000, increasing at a rate of 10% per year. Find the population at the end of each of the previous 10 years.*

```python
curr_pop = 10000

for year in range(10, 0, -1):
    print(f"Year {year}: {curr_pop:.2f}")
    curr_pop = curr_pop - 0.1 * curr_pop
```

---

## 5. Practice Exercises (To-Do)

- **Sequence Sum:** Calculate $1/1! + 2/2! + 3/3! + \dots + n/n!$
- **Nested Loops:** Generate unique combinations of `1, 2, 3, 4`
- **Pattern 1:**
  ```text
  *
  **
  ***
  ```
- **Pattern 2:**
  ```text
  1
  121
  12321
  1234321
  ```
- **Loop Control Statements:** Practice implementing `break` (e.g., prime number checker), `continue`, and `pass`.