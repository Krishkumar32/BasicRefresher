# 📌 What is a Variable?

# A variable is a name that stores a value in memory.

# Think of a box with a label:

# Label = variable name

# Inside box = value

# Example:

name = "Krishna"
age = 24


# Here,

# name stores "Krishna"

# age stores 24

# 📌 Why do we use Variables?

# We use variables to:

# ✔ store data
# ✔ reuse data
# ✔ process values

# Without variables, you must type the value again and again.

# 📌 How to Create a Variable in Python?

# Just write name = value

x = 10
city = "Bangalore"


# Python automatically detects type, no need to declare type.

# ✅ Variable Naming Rules
# Rule	Example
# Start with letter or _	name, _value
# Cannot start with number ❌	1name ❌
# No special characters	name$ ❌
# No space	my name ❌
# Case sensitive	age ≠ Age
# Meaningful name	studentName ✅

# ✅ Data Types Stored in Variables
# Data Type	Example
int (numbers)	age = 20
float (decimal)	price = 99.5
string (text)	name = "Krishna"
bool (True/False)	isStudent = True
complex	c = 2+3j

# ✅ Check Data Type
x = 10
print(type(x))

# ✅ Change/Update Variable
x = 5
x = 10   # value updated

# ✅ Multiple Variables
Assign multiple values:
a, b, c = 1, 2, 3

# Same value to multiple variables:
x = y = z = 10

# ✅ Input Variable

# User enters value at runtime:

name = input("Enter name: ")

# ✅ Constant in Python

# Python does not have real constants, but we use capital letters:

PI = 3.14
MAX_STUDENTS = 100

# ✅ Keywords Cannot be Variables

# Words reserved by Python cannot be used as variable names:

# Examples: if, for, class, True, False, etc.

# Check keywords:

import keyword
print(keyword.kwlist)

# 📌 Dynamic Typing

# Python is dynamically typed
# → Type decided during program execution

# Example:

x = 10      # int
x = "Hello" # now string

# ✅ Memory Concept

# When you create a variable, Python makes space in memory to store value.

# Example:

x = 5


Memory:
x → 5

# 📚 Short Q & A for Interview

# Question	Answer

# What is variable? -	A container to store data
# Does Python need type declaration? -	No, it is dynamically typed
# How to check type? - type(variable)
# What is constant? -	Value that should not change, written in CAPITALS
# Can variables be updated? -	Yes
# Example of invalid variable	 - 1name, data$
