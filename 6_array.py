# 🧠 What is an Array in Python?
# An array is a data structure that stores multiple values of the same type in one variable.

# Example: storing marks of 5 students.

# Python supports arrays in two ways:

# Type	Module/Structure	Used For
# Built-in list	list	General-purpose (can store mixed types)
# Array module	array	Store same data type only (int/float) — like C/Java arrays

# ✅ Difference Between List & Array
# Feature        	List            	     Array (array module)
# Stores         	Mixed data types      	Same data type
# Speed	          Slower in numerics	     Faster
# Used in        	General python	         Numeric operations
# Import needed   	No	                   Yes (import array)

# ✅ Using Arrays (array module)
# ✨ Import
# import array

# ✨ Create an integer array
  import array as arr
  a = arr.array('i', [1, 2, 3, 4, 5])
  print(a)

# Code	Meaning
# 'i'	integer array
# 'f'	float array
# 📍 Array Operations

# ✅ Access Elements (indexing)
 print(a[0])   # 1
 print(a[3])   # 4

# ✅ Update Value
 a[1] = 10
 print(a)

# ✅ Append Values
 a.append(6)
 print(a)

# ✅ Insert Value
 a.insert(2, 15)  # at index 2
 print(a)

# ✅ Remove Value
 a.remove(10)
 print(a)

# ✅ Pop Element
 a.pop()  # last element

# ✅ Length
 print(len(a))

# 🔁 Loop Through Array
 for x in a:
     print(x)

# ❌ If we try to insert wrong type
 a.append("hello")   # ERROR

# ✅ 2-D Array (list of lists)
 matrix = [
     [1, 2],
     [3, 4]
 ]

 print(matrix[0][1])  # 2

# 🧮 Array vs NumPy Array (Important)

# Feature           	Python array           	NumPy array
# Speed	                Slow	                Very fast
# Memory	              More	                   Less
# Operations	          Limited               	Many
# Suitable for       	Small data	            Machine learning, data science

# NumPy Example:
 import numpy as np
 a = np.array([1, 2, 3, 4, 5])
 print(a)

# 🧑‍🏫 When to use what?
# Use Case   :                              	Use:
# General                                   purpose	List
# Same type + performance need	           array module
# Data science / ML	                        NumPy array

# 💡 Interview Quick Notes
# Question	Answer
# What is an array?-	A collection of similar data elements.
# Array module name?-	array
# List vs array?	-List stores mixed values, array stores same type only
# Default array type?	-No default, we specify type code like 'i', 'f'

# 🎯 Cheat Code Table — Python Array Type Codes
# Code	Meaning
# 'i'	integer
# 'f'	float
# 'b'	signed char
# 'd'	double
