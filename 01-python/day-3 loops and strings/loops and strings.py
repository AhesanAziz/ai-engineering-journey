
# ============================================================
# PYTHON FUNDAMENTALS
# Topics: Loops, Nested Loops, Loop Control Statements & Strings
# ============================================================


# ============================================================
# 1. LOOPS - PRACTICE PROGRAMS
# ============================================================

# ------------------------------------------------------------
# Program 1: Population Growth
#
# Problem:
# Current population = 10000
# Population increases by 10% every year.
# Find the population at the end of each of the last 10 years.
#
# Formula:
# New Population = Old Population * 1.1
#
# To calculate previous population:
# Previous Population = Current Population / 1.1
# ------------------------------------------------------------

def population_growth():
    current_population = 10000

    for year in range(10, 0, -1):
        population = current_population / (1.1 ** year)
        print(f"{year} years ago: {population:.2f}")


# ------------------------------------------------------------
# Program 2: Sequence Sum
#
# Problem:
# Calculate the sum of:
# 1/1! + 2/2! + 3/3! + ... + n/n!
#
# Factorial:
# 4! = 4 * 3 * 2 * 1 = 24
# ------------------------------------------------------------

def sequence_sum():
    n = int(input("Enter n: "))

    result = 0
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i
        result = result + i / fact

    print(result)


# ============================================================
# 2. NESTED LOOPS
# ============================================================

# A nested loop means placing one loop inside another loop.
# The inner loop executes completely for every iteration
# of the outer loop.


# Example 1: Printing all pairs

for i in range(1, 5):
    for j in range(1, 5):
        print(i, j)


# Example 2: Printing unique pairs
# Avoids repeating pairs in reverse order.

for i in range(1, 5):
    for j in range(i + 1, 5):
        print(i, j)


# ============================================================
# 3. PATTERN PRINTING USING NESTED LOOPS
# ============================================================

# ------------------------------------------------------------
# Pattern 1: Increasing Star Pattern
#
# *
# **
# ***
# ****
# ------------------------------------------------------------

def star_pattern():
    rows = int(input("Enter number of rows: "))

    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()


# ------------------------------------------------------------
# Pattern 2: Palindromic Number Pattern
#
# 1
# 121
# 12321
# 1234321
# ------------------------------------------------------------

def number_pattern():
    rows = int(input("Enter number of rows: "))

    for i in range(1, rows + 1):

        # Increasing sequence
        for j in range(1, i + 1):
            print(j, end="")

        # Decreasing sequence
        for k in range(i - 1, 0, -1):
            print(k, end="")

        print()


# ============================================================
# 4. LOOP CONTROL STATEMENTS
# ============================================================

# Three important loop control statements:
#
# 1. break
# 2. continue
# 3. pass


# ------------------------------------------------------------
# 4.1 BREAK
#
# The break statement immediately terminates the loop.
# ------------------------------------------------------------

for i in range(1, 10):
    if i == 5:
        break

    print(i)

# Output:
# 1
# 2
# 3
# 4


# ------------------------------------------------------------
# 4.2 CONTINUE
#
# The continue statement skips the current iteration
# and moves to the next iteration.
# ------------------------------------------------------------

for i in range(1, 10):
    if i == 5:
        continue

    print(i)

# Output:
# 1 2 3 4 6 7 8 9


# ------------------------------------------------------------
# 4.3 PASS
#
# The pass statement does nothing.
# It is used as a placeholder when a statement is required.
# ------------------------------------------------------------

for i in range(1, 10):
    pass


# ------------------------------------------------------------
# 4.4 FOR-ELSE STATEMENT
#
# The else block executes when the loop finishes normally
# without encountering a break statement.
#
# Example: Finding prime numbers in a given range.
# ------------------------------------------------------------

def prime_numbers():
    lower = int(input("Enter lower range: "))
    upper = int(input("Enter upper range: "))

    for i in range(lower, upper + 1):

        if i < 2:
            continue

        for j in range(2, i):

            if i % j == 0:
                break

        else:
            print(i)

# Note:
# The else belongs to the inner for loop.
# If the inner loop finishes without break, the number is prime.


# ============================================================
# 5. STRINGS IN PYTHON
# ============================================================

# A string is a sequence of characters.
# In Python, strings are sequences of Unicode characters.
#
# Topics:
# 1. Creating strings
# 2. Accessing strings
# 3. String slicing
# 4. Editing and deleting strings
# 5. String operations
# 6. String functions
# 7. Practical string programs


# ------------------------------------------------------------
# 5.1 CREATING STRINGS
# ------------------------------------------------------------

s = 'hello'

s = "hello"

# Multiline strings
s = '''hello'''

s = """hello"""

# Using str()
s = str("hello")

print(s)

# Quotation marks inside strings
s = "It's raining outside"
print(s)


# ============================================================
# 6. ACCESSING SUBSTRINGS FROM A STRING
# ============================================================

# ------------------------------------------------------------
# 6.1 POSITIVE INDEXING
#
# Positive indexing starts from 0 and moves left to right.
# ------------------------------------------------------------

s = "hello world"

print(s[0])  # h
print(s[1])  # e
print(s[4])  # o

# Accessing an invalid index causes IndexError.
# print(s[41])


# ------------------------------------------------------------
# 6.2 NEGATIVE INDEXING
#
# Negative indexing starts from -1 and moves right to left.
# ------------------------------------------------------------

s = "hello world"

print(s[-1])  # d
print(s[-2])  # l
print(s[-3])  # r


# ------------------------------------------------------------
# 6.3 STRING SLICING
#
# Syntax:
# string[start:stop:step]
#
# start = Starting index (included)
# stop  = Ending index (excluded)
# step  = Number of positions to move
# ------------------------------------------------------------

s = "hello world"

print(s[0:5])       # hello
print(s[6:11])      # world
print(s[0:11:2])    # hlowrd
print(s[6:0:-2])    # wol
print(s[::-1])      # dlrow olleh
print(s[-1:-6:-1])  # dlrow

# Important:
# The ending index is excluded.
# A positive step moves left to right.
# A negative step moves right to left.
# [::-1] reverses a string.


# ============================================================
# 7. EDITING AND DELETING STRINGS
# ============================================================

# Python strings are IMMUTABLE.
#
# Immutability means that individual characters of an
# existing string cannot be modified.


# Example: This produces a TypeError.
#
# s = "hello world"
# s[0] = "H"


# Correct approach: Create a new string.

s = "hello world"
s = "H" + s[1:]

print(s)  # Hello world


# ------------------------------------------------------------
# Deleting a string variable
# ------------------------------------------------------------

s = "hello world"

del s

# print(s)
# This produces NameError because the variable is deleted.


# Individual characters cannot be deleted using del.
# Strings are immutable.


# ============================================================
# 8. OPERATIONS ON STRINGS
# ============================================================

# Five types of operations:
#
# 1. Arithmetic operations
# 2. Relational operations
# 3. Logical operations
# 4. Loops on strings
# 5. Membership operations


# ------------------------------------------------------------
# 8.1 ARITHMETIC OPERATIONS
# ------------------------------------------------------------

# Concatenation (+)
print("delhi" + " " + "mumbai")

# Repetition (*)
print("delhi" * 5)

# Another example
print("*" * 50)


# ------------------------------------------------------------
# 8.2 RELATIONAL OPERATIONS
#
# Strings are compared lexicographically using Unicode values.
# String comparisons are case-sensitive.
# ------------------------------------------------------------

print("delhi" == "delhi")  # True
print("delhi" != "delhi")  # False

print("mumbai" > "pune")   # False
print("Pune" > "pune")     # False


# ------------------------------------------------------------
# 8.3 LOGICAL OPERATIONS
#
# Operators:
# and
# or
# not
#
# Python's and/or operators return operands,
# not necessarily Boolean values.
# ------------------------------------------------------------

# AND:
# Returns the first falsy operand.
# If all operands are truthy, returns the last operand.

print("hello" and "world")  # world
print("" and "world")       # ""

# OR:
# Returns the first truthy operand.
# If all operands are falsy, returns the last operand.

print("hello" or "world")  # hello
print("" or "world")       # world

# NOT:
# Returns the opposite Boolean value of truthiness.

print(not "hello")  # False
print(not "")       # True


# ------------------------------------------------------------
# 8.4 LOOPS ON STRINGS
# ------------------------------------------------------------

for i in "hello":
    print(i)

# Another example

for i in "delhi":
    print("pune")


# ------------------------------------------------------------
# 8.5 MEMBERSHIP OPERATIONS
#
# in and not in check whether a character or substring
# exists inside a string.
# ------------------------------------------------------------

print("D" in "delhi")       # False
print("d" in "delhi")       # True
print("del" in "delhi")     # True
print("abc" not in "delhi") # True


# ============================================================
# 9. COMMON STRING FUNCTIONS
# ============================================================

# ------------------------------------------------------------
# len()
# Returns the number of characters in a string.
# Spaces are also counted.
# ------------------------------------------------------------

print(len("hello world"))


# ------------------------------------------------------------
# max()
# Returns the character with the highest Unicode value.
# ------------------------------------------------------------

print(max("hello world"))


# ------------------------------------------------------------
# min()
# Returns the character with the lowest Unicode value.
# ------------------------------------------------------------

print(min("hello world"))


# ------------------------------------------------------------
# sorted()
# Returns a sorted list of characters.
# It does not return a string.
# ------------------------------------------------------------

print(sorted("hello world"))
print(sorted("hello world", reverse=True))


# ============================================================
# 10. CAPITALIZE, TITLE, UPPER, LOWER AND SWAPCASE
# ============================================================

s = "hello world"

# capitalize(): First character uppercase, remaining lowercase.
print(s.capitalize())

# title(): First character of each word uppercase.
print(s.title())

# upper(): Converts all characters to uppercase.
print(s.upper())

# lower(): Converts all characters to lowercase.
print("Hello World".lower())

# swapcase(): Converts uppercase to lowercase and vice versa.
print("HeLlO WoRlD".swapcase())

# Important:
# Strings are immutable.
# These methods return new strings and do not modify
# the original string.


# ============================================================
# 11. COUNT, FIND AND INDEX
# ============================================================

s = "my name is nitish"

# count(): Counts occurrences of a substring.
print(s.count("i"))  # 3

# find(): Returns the position of the first occurrence.
# Returns -1 if the substring is not found.
print(s.find("x"))   # -1

# index(): Returns the position of the first occurrence.
# Raises ValueError if the substring is not found.
# print(s.index("x"))


# Difference:
#
# find()  -> Returns -1 if not found.
# index() -> Raises ValueError if not found.


# ============================================================
# 12. ENDSWITH() AND STARTSWITH()
# ============================================================

s = "my name is nitish"

# endswith(): Checks whether a string ends with a substring.
print(s.endswith("nitish"))  # True
print(s.endswith("sho"))     # False

# startswith(): Checks whether a string starts with a substring.
print(s.startswith("my"))    # True
print(s.startswith("1my"))   # False


# ============================================================
# 13. FORMAT()
# ============================================================

name = "nitish"
gender = "male"

# Inserts values into placeholders.

print("Hi my name is {1} and I am a {0}".format(gender, name))

# {0} = First argument
# {1} = Second argument


# Named placeholders

print("My name is {name} and I am {gender}".format(
    name=name,
    gender=gender
))


# ============================================================
# 14. ISALNUM(), ISALPHA(), ISDIGIT() AND ISIDENTIFIER()
# ============================================================

# isalnum():
# True if all characters are letters or numbers.
print("nitish1234".isalnum())   # True
print("nitish1234%".isalnum())  # False

# isalpha():
# True if all characters are alphabetic.
print("nitish".isalpha())      # True
print("nitish123".isalpha())   # False

# isdigit():
# True if all characters are digits.
print("12345".isdigit())       # True
print("123abc".isdigit())      # False

# isidentifier():
# Checks whether a string is a valid Python identifier.
print("first_name".isidentifier())  # True
print("first-name".isidentifier())  # False
print("123name".isidentifier())     # False


# ============================================================
# 15. SPLIT() AND JOIN()
# ============================================================

# split():
# Splits a string into a list of substrings.
# By default, separates using whitespace.

s = "hi my name is nitish"

print(s.split())

# Specifying a separator

s = "apple,banana,mango"
print(s.split(","))


# join():
# Joins elements of an iterable into a single string.

words = ["hi", "my", "name", "is", "nitish"]

print(" ".join(words))

# Another example

print("-".join(["2026", "11", "26"]))


# ============================================================
# 16. REPLACE()
# ============================================================

# replace():
# Replaces one substring with another.

s = "hi my name is nitish"

print(s.replace("nitish", "campusx"))

# If the old substring does not exist,
# the original string is returned unchanged.


# ============================================================
# 17. STRIP()
# ============================================================

# strip(): Removes whitespace from both sides.
# lstrip(): Removes whitespace from the left.
# rstrip(): Removes whitespace from the right.

s = "    nitish    "

print(s.strip())
print(s.lstrip())
print(s.rstrip())

# These methods do not remove spaces from the middle.


# ============================================================
# 18. PRACTICAL STRING PROGRAMMING PROBLEMS
# ============================================================


# ------------------------------------------------------------
# Problem 1: Find the length of a string without using len().
# ------------------------------------------------------------

def string_length():

    s = input("Enter the string: ")

    counter = 0

    for i in s:
        counter += 1

    print("Length of string is", counter)


# ------------------------------------------------------------
# Problem 2: Extract username from an email.
#
# Example:
# Input:  nitish24singh@gmail.com
# Output: nitish24singh
# ------------------------------------------------------------

def extract_username():

    s = input("Enter the email: ")

    pos = s.index("@")

    print(s[0:pos])


# ------------------------------------------------------------
# Problem 3: Count the frequency of a particular character.
#
# Example:
# String: hello how are you
# Search: h
# ------------------------------------------------------------

def character_frequency():

    s = input("Enter the string: ")
    term = input("What would you like to search for? ")

    counter = 0

    for i in s:
        if i == term:
            counter += 1

    print("Frequency:", counter)

# Note: This program assumes term is a single character.


# ------------------------------------------------------------
# Problem 4: Remove a particular character from a string.
# ------------------------------------------------------------

def remove_character():

    s = input("Enter the string: ")
    term = input("What would you like to remove? ")

    result = ""

    for i in s:
        if i != term:
            result = result + i

    print(result)


# ------------------------------------------------------------
# Problem 5: Check whether a string is a palindrome.
#
# Examples:
# abba
# malayalam
# madam
# ------------------------------------------------------------

def palindrome_check():

    s = input("Enter the string: ")

    flag = True

    for i in range(0, len(s) // 2):

        if s[i] != s[len(s) - i - 1]:

            flag = False
            print("Not a Palindrome")
            break

    if flag:
        print("Palindrome")


# Alternative approach using slicing:

def palindrome_check_alternative():

    s = input("Enter the string: ")

    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")


# ------------------------------------------------------------
# Problem 6: Count the number of words without using split().
#
# The in_word variable checks whether we are currently
# inside a word.
# Multiple consecutive spaces are handled correctly.
# ------------------------------------------------------------

def word_count():

    s = input("Enter the string: ")

    counter = 0
    in_word = False

    for i in s:

        if i != " ":

            if not in_word:
                counter += 1

            in_word = True

        else:
            in_word = False

    print("Number of words:", counter)


# ------------------------------------------------------------
# Problem 7: Convert a string to title case without using title().
# ------------------------------------------------------------

def convert_to_title_case():

    s = input("Enter the string: ")

    L = []

    for i in s.split():

        L.append(i[0].upper() + i[1:].lower())

    print(" ".join(L))


# ------------------------------------------------------------
# Problem 8: Convert an integer to a string without using str().
#
# Handles:
# - Positive numbers
# - Negative numbers
# - Zero
# ------------------------------------------------------------

def integer_to_string():

    number = int(input("Enter the number: "))

    digits = "0123456789"
    result = ""

    if number == 0:

        result = "0"

    else:

        if number < 0:
            number = -number
            sign = "-"

        else:
            sign = ""

        while number != 0:

            result = digits[number % 10] + result

            number = number // 10

        result = sign + result

    print(result)
    print(type(result))


# ============================================================
# 19. QUICK REVISION
# ============================================================

# LOOPS
#
# for       -> Iterates over a sequence.
# while     -> Repeats while a condition is True.
# break     -> Terminates a loop.
# continue  -> Skips the current iteration.
# pass      -> Does nothing; acts as a placeholder.
#
# Nested loops -> Loops inside other loops.
# For-else     -> Else executes if loop finishes without break.


# STRINGS
#
# Strings are immutable.
# Indexing starts from 0.
# Negative indexing starts from -1.
# Slicing uses [start:stop:step].
# The stop index is excluded.
# [::-1] reverses a string.


# COMMON STRING FUNCTIONS
#
# len()       -> Returns string length.
# max()       -> Returns maximum character.
# min()       -> Returns minimum character.
# sorted()    -> Returns a sorted list.
# count()     -> Counts occurrences.
# find()      -> Finds substring; returns -1 if missing.
# index()     -> Finds substring; raises ValueError if missing.
# split()     -> Splits a string into a list.
# join()      -> Joins iterable elements into a string.
# replace()   -> Replaces a substring.
# strip()     -> Removes leading and trailing whitespace.
# upper()     -> Converts to uppercase.
# lower()     -> Converts to lowercase.
# title()     -> Converts to title case.
# capitalize()-> Capitalizes the first character.
# swapcase()  -> Reverses character capitalization.
# isalpha()   -> Checks alphabetic characters.
# isdigit()   -> Checks digit characters.
# isalnum()   -> Checks alphanumeric characters.
# isidentifier() -> Checks valid Python identifiers.


# ============================================================
# END OF PYTHON FUNDAMENTALS: LOOPS AND STRINGS
# ============================================================


# ============================================================
# HOW TO RUN THE PRACTICE PROGRAMS
# ============================================================
#
# All practical programs are defined as functions.
# To practise a particular program, call its function below.
#
# Example:
#
# population_growth()
# sequence_sum()
# star_pattern()
# number_pattern()
# prime_numbers()
# string_length()
# extract_username()
# character_frequency()
# remove_character()
# palindrome_check()
# word_count()
# convert_to_title_case()
# integer_to_string()
#
# Uncomment only the function you want to practise.
# ============================================================

