# 🔹 What is a Function?

# A function is a block of code that runs when we call it.
# We use functions to reuse code and avoid repetition.

# ⭐ Example
def greet():
    print("Hello, welcome!")

# Call function:
greet()

# 🔹 Why Functions?
# Without function :                  	With function:
# Code repeats again & again          	Reusable
# Hard to maintain	                    Easy to manage
# Long code	                             Short & clean code

# 🔹 Types of Functions
# Type:                                 	Meaning:
# Built-in	                             Already available (print, len, input)
# User defined                         	 We create them
# Functions with parameters	             Take inputs
# Functions with return                	 Give output

# ✅ Creating & Calling a Function
def hello():
    print("Hello World")

hello()

# ✅ Function with Parameters (Arguments)
# 🔸 Single argument
def greet(name):
    print("Hello", name)

greet("Krishna")

# 🔸 Multiple arguments
def add(a, b):
    print(a + b)

add(10, 20)

# ✅ Return Value

# If you want function to give back a value, use return.

def add(a, b):
    return a + b

result = add(5, 3)
print(result)   # 8


print = show output
return = send back a value

# ✅ Function Without Arguments
def show():
    print("No input here")

show()

# ✅ Function With Multiple Return Values
def calc(a, b):
    return a + b, a - b

x, y = calc(10, 5)
print(x, y)

# ✅ Default Parameter

# If parameter value is not given, default will be used.

def greet(name="Guest"):
    print("Hello", name)

greet()        # Hello Guest
greet("Rahul") # Hello Rahul

# ✅ Keyword Arguments

# Specify value by parameter name

def student(name, age):
    print(name, age)

student(age=21, name="Ravi")

# ✅ Variable Length Arguments
# 🔸 *args → multiple values (tuple)
def total(*numbers):
    print(sum(numbers))

total(10, 20, 30)

# 🔸 **kwargs → key-value (dictionary)
def info(**data):
    print(data)

info(name="Krishna", age=22)

# ✅ Local vs Global Variables
# Local variable (inside function)
def test():
    x = 10
    print(x)

test()

#Global variable (outside)
x = 50

def show():
    print(x)

show()

#Modify global inside function
x = 100

def change():
    global x
    x = 200

change()
print(x) # 200

# ✅ Anonymous Function (Lambda)

# Short function for simple tasks

add = lambda a, b: a + b
print(add(2, 3))

# 🎯 Important Interview Points

# Function = reusable code block
# Defined  - using def
# return - sends value back
# *args = many values
# **kwargs = key-value pairs
# Local variable -  lives inside function
# Global variable - accessible everywhere
# Lambda = one-line function

# 📝 Quick Revision

# Topic:                            	Meaning:
# def	                                define function
# return                            	give output
# parameter                         	input name
# argument                          	input value
# *args                              	many values
# **kwargs	                          many key-value
# global	                            modify outside variable
