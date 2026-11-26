
# ==========================================
# PYTHON PRACTICE: LOOPS, PATTERNS AND STRINGS
# ==========================================

# Each problem is written as a separate function.
# To run a problem, call its function at the bottom
# of this file.


# ==========================================
# PROBLEM 1: Reverse Number Pattern
# ==========================================

def problem_1():
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


# ==========================================
# PROBLEM 2: Increasing and Decreasing Star Pattern
# ==========================================

def problem_2():
    # Increasing pattern
    for i in range(1, 6):
        for j in range(i):
            print("*", end=" ")
        print()

    # Decreasing pattern
    for i in range(4, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()


# ==========================================
# PROBLEM 3: Pyramid Star Pattern
# ==========================================

def problem_3():
    for i in range(1, 10, 2):
        spaces = (9 - i) // 2

        print("  " * spaces + "* " * i)


# ==========================================
# PROBLEM 4: Reverse Number Pattern
# ==========================================

def problem_4():
    for i in range(1, 6):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


# ==========================================
# PROBLEM 5: Sum of the Series
# 1 + x^2/2 + x^3/3 + ... + x^n/n
# ==========================================

def problem_5():
    x = float(input("Enter the value of x: "))
    n = int(input("Enter the number of terms: "))

    total = 1

    for i in range(2, n + 1):
        total += (x ** i) / i

    print("Sum of the series:", total)


# ==========================================
# PROBLEM 6: Natural Logarithm Series
# ln(1+x) = x - x^2/2 + x^3/3 - x^4/4 + ...
# Calculate the first 7 terms.
# ==========================================

def problem_6():
    x = float(input("Enter the value of x: "))

    total = 0

    for i in range(1, 8):
        term = (x ** i) / i

        if i % 2 == 0:
            total -= term
        else:
            total += term

    print("Approximate value of ln(1+x):", total)


# ==========================================
# PROBLEM 7: Sum of Repeated 2s
# Example: 2 + 22 + 222 + 2222 + ...
# ==========================================

def problem_7():
    n = int(input("Enter the number of terms: "))

    term = 0
    total = 0

    for i in range(n):
        term = term * 10 + 2
        total += term

        if i > 0:
            print("+", end="")

        print(term, end="")

    print()
    print("Sum of above series is:", total)


# ==========================================
# PROBLEM 8: Unique Combinations of 1, 2, 3 and 4
# ==========================================

def problem_8():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                for l in range(1, 5):

                    if i != j and i != k and i != l:
                        if j != k and j != l and k != l:
                            print(i, j, k, l)


# ==========================================
# PROBLEM 9: Decimal to Binary Conversion
# ==========================================

def problem_9():
    num = int(input("Enter a decimal number: "))

    if num == 0:
        print("Binary equivalent: 0")
        return

    original_num = num
    binary = ""

    if num < 0:
        num = -num

    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

    if original_num < 0:
        binary = "-" + binary

    print("Binary equivalent:", binary)


# ==========================================
# PROBLEM 10: LCM and HCF of Two Numbers
# ==========================================

def problem_10():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    a = abs(num1)
    b = abs(num2)

    # Finding HCF using the Euclidean algorithm
    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    hcf = a

    # Finding LCM
    if num1 == 0 or num2 == 0:
        lcm = 0
    else:
        lcm = abs(num1 * num2) // hcf

    print("HCF:", hcf)
    print("LCM:", lcm)


# ==========================================
# PROBLEM 11: Create Short Form from Initial Characters
# Example: Data science mentorship program -> DSMP
# ==========================================

def problem_11():
    sentence = input("Enter a sentence: ")

    words = sentence.split()
    short_form = ""

    for word in words:
        short_form += word[0].upper()

    print("Short form:", short_form)


# ==========================================
# PROBLEM 12: Append Second String in the Middle
# Example: campusx + data -> camdatapusx
# ==========================================

def problem_12():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    middle = len(str1) // 2

    result = str1[:middle] + str2 + str1[middle:]

    print("Result:", result)


# ==========================================
# PROBLEM 13: Arrange Lowercase Letters First
# Example: PyNaTive -> yaivePNT
# ==========================================

def problem_13():
    str1 = input("Enter a string: ")

    lowercase = ""
    uppercase = ""

    for char in str1:
        if char.islower():
            lowercase += char
        else:
            uppercase += char

    result = lowercase + uppercase

    print("Result:", result)


# ==========================================
# PROBLEM 14: Sum and Average of Digits in a String
# Example: hel123O4every093
# ==========================================

def problem_14():
    text = input("Enter an alphanumeric string: ")

    total = 0
    count = 0

    for char in text:
        if char.isdigit():
            total += int(char)
            count += 1

    if count == 0:
        print("No digits found.")
    else:
        average = total / count

        print("Sum:", total)
        print("Avg:", average)


# ==========================================
# PROBLEM 15: Remove All Characters Except Integers
# Example: I am 25 years and 10 months old -> 2510
# ==========================================

def problem_15():
    str1 = input("Enter a string: ")

    result = ""

    for char in str1:
        if char.isdigit():
            result += char

    print("Result:", result)


# ==========================================
# PROBLEM 16: Check Whether a String is Symmetrical
# Example: khokho
# ==========================================

def problem_16():
    text = input("Enter a string: ")

    middle = len(text) // 2

    if len(text) % 2 == 0:
        first_half = text[:middle]
        second_half = text[middle:]
    else:
        first_half = text[:middle]
        second_half = text[middle + 1:]

    if first_half == second_half:
        print("The entered string is symmetrical.")
    else:
        print("The entered string is not symmetrical.")


# ==========================================
# PROBLEM 17: Reverse Words in a Given String
# Example: geeks quiz practice code
# Output: code practice quiz geeks
# ==========================================

def problem_17():
    sentence = input("Enter a sentence: ")

    words = sentence.split()

    reversed_sentence = " ".join(words[::-1])

    print("Result:", reversed_sentence)


# ==========================================
# PROBLEM 18: Find Uncommon Words from Two Strings
# ==========================================

def problem_18():
    A = input("Enter the first sentence: ")
    B = input("Enter the second sentence: ")

    words_A = A.split()
    words_B = B.split()

    uncommon_words = []

    for word in words_A:
        if words_A.count(word) == 1 and words_B.count(word) == 0:
            uncommon_words.append(word)

    for word in words_B:
        if words_B.count(word) == 1 and words_A.count(word) == 0:
            uncommon_words.append(word)

    print("Uncommon words:", uncommon_words)


# ==========================================
# PROBLEM 19: Find Word Location in a String
# Do not use index() or find().
# ==========================================

def problem_19():
    sentence = input("Enter a sentence: ")
    target = input("Enter the word to search for: ")

    words = sentence.split()

    location = -1

    for i in range(len(words)):
        if words[i] == target:
            location = i + 1
            break

    if location != -1:
        print("Location of the word is", location)
    else:
        print("Word not found.")


# ==========================================
# PROBLEM 20: Remove Duplicate Characters from a String
# ==========================================

def problem_20():
    text = input("Enter a string: ")

    result = ""

    for char in text:
        if char not in result:
            result += char

    print("String after removing duplicates:", result)


# ==========================================
# RUN A PROBLEM
# ==========================================

# Uncomment ONE function call at a time to run that problem.

# problem_1()
# problem_2()
# problem_3()
# problem_4()
# problem_5()
# problem_6()
# problem_7()
# problem_8()
# problem_9()
# problem_10()
# problem_11()
# problem_12()
# problem_13()
# problem_14()
# problem_15()
# problem_16()
# problem_17()
# problem_18()
# problem_19()
# problem_20()
