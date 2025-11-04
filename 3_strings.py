# ✅ What is a string?

# A string is a text value
# Written inside quotes " "
# Strings are immutable (cannot change characters)

name = "Hello"
print(name)

#✅ Loop through string characters
text = "this is string"
for ch in text:
    print(ch)

#✅ ASCII value (like Go byte)
ch = 'A'
print(ord(ch))   # 65

#✅ Unicode example
word = "Señor"
for ch in word:
    print(ch)

#✅ Convert bytes → string
b = [116,104,105,115]
text = bytes(b).decode()
print(text)

#✅ Useful string functions
s = "test"
print("es" in s)                # contains
print(s.count("t"))             # count
print(s.startswith("te"))       # prefix
print(s.endswith("st"))         # suffix
print(s.index("e"))             # index
print("-".join(["a","b"]))      # join
print("a"*5)                    # repeat
print("foo".replace("o","0"))   # replace
print("a-b-c".split("-"))       # split
print("TEST".lower())           # lower
print("test".upper())           # upper

#✅ Compare strings
s1 = "Hello"
s2 = "World"
print(s1 == s2)

#✅ Concatenate strings
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)
print(f"{s1} {s2}")   # formatted


Q1: What are strings in Python?

# A: Strings store text and are written in single ' ' or double " " quotes.

# Q2: Which quotes can be used for strings?

# A: 'hello' and "hello" both are valid.

# Q3: How to print a string?

# A: Using print()

# print("Hello")
# print('Hello')

# Q4: Can we use quotes inside a string?

# A: Yes, if they are different from outside quotes.

# print("It's fine")
# print('He is "Johnny"')

# Q5: How to store string in a variable?
# a = "Hello"
# print(a)

# Q6: How to write multi-line strings?

# Use triple quotes:

# a = """Hello
# World"""


# or

# a = '''Hello
# World'''

# Q7: Are strings arrays in Python?

# A: Yes, they act like arrays of characters.

# Q8: Does Python have a char type?

# A: No, a single character is also a string (length 1).

# Q9: How to access a character by index?
# a = "Hello"
# print(a[1])   # e

# Q10: How to loop through characters of a string?
# for x in "banana":
#     print(x)

# Q11: How to find length of string?

# Use len()

# a = "Hello"
# print(len(a))  # 5

# Q12: How to check if a word exists in a string?

# Use in

# txt = "Life is free"
# print("free" in txt)   # True

# Q13: How to use in with if?
# txt = "Life is free"
# if "free" in txt:
#     print("found")

# Q14: How to check if a word does NOT exist?

# Use not in

# txt = "Life is free"
# print("expensive" not in txt)

# Q15: How to use not in in if?
# if "expensive" not in txt:
#     print("Not found")
