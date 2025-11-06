# Q1. What is a stack?
# A stack is a linear data structure that follows the Last In First Out (LIFO) principle.

# Q2. What does LIFO mean?
# The last element added to the stack is the first one removed.

# Q3. Example of stack in real life?
# A stack of pancakes — you add and remove from the top.

# ⚙️ Stack Operations

# Q4. What is Push operation?
# Adds an element to the top of the stack.

# Q5. What is Pop operation?
# Removes and returns the top element.

# Q6. What is Peek operation?
# Returns the top element without removing it.

# Q7. What is isEmpty operation?
# Checks if the stack is empty.

# Q8. What is Size operation?
# Returns the number of elements in the stack.

# 💻 Stack Implementation

# Q9. How can we implement a stack in Python?
# Using lists or linked lists.

# Q10. Why use lists for stack?

# Simple and easy to use

# Memory efficient

# Q11. Why not use arrays for stack?
# Because arrays have fixed size.

# Q12. Why use linked list for stack?
# Because it allows dynamic size (can grow/shrink anytime).

# Q13. Why not use linked list for stack?
# It needs extra memory for storing node addresses.

# 🔧 Python List Stack Example
 stack = []
 stack.append('A')  
 stack.append('B')
 stack.pop()        
 stack[-1]          

# 🧱 Stack using Class Example (short)
 class Stack:
   def __init__(self):
     self.stack = []
   def push(self, e): self.stack.append(e)
   def pop(self): return self.stack.pop() if self.stack else "Empty"
   def peek(self): return self.stack[-1] if self.stack else "Empty"

# 🔗 Stack using Linked List

# Q14. What is a linked list stack?
# A stack made using nodes, each storing data and a pointer to the next node.

# Q15. Advantage of linked list stack?
# Can grow dynamically.

# Q16. Disadvantage of linked list stack?
# Takes extra memory and is more complex.

# 🌍 Real-World Uses of Stack

# Q17. Where are stacks used?
# Undo/Redo in editors
# Browser history
# Function calls
# Expression evaluation
# Backtracking (like maze solving)

# 🧠 Explanation:

# push() → adds element on top

# pop() → removes top element and returns it

# isEmpty() → checks if stack is empty

# top() → shows top element without removing

# Like Go, here also we encapsulate (group) all methods under one class
