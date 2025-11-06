# 🧠 What is a Queue?

# 👉 A Queue is a linear data structure that follows the rule:
# FIFO – First In, First Out

# That means —

# The first element added will be the first one removed.

# 🎯 Real-life example:
# Think of people standing in a line at a movie ticket counter —

# The first person in line is served first.

# New people join at the end of the line.

# 🧩 Basic Queue Operations
# Operation	               Meaning	                                        Example
# Enqueue	                   Add element to end of queue	                  Add new person to line
# Dequeue	                  Remove element from front	                    First person gets ticket & leaves
# Peek	                 Show the front element	See who’s                    first in line
# isEmpty	                 Check if queue is empty	                        Is anyone waiting?
# Size	                 Count how many are in queue	                 How many people in line?

# 🧮 Queue using Python List

# In Python, lists can easily act as queues.
queue = []

# Enqueue (add elements)
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue:", queue)

# Peek (see front element)
print("Peek:", queue[0])

# Dequeue (remove first element)
print("Dequeue:", queue.pop(0))
print("Queue after Dequeue:", queue)

# isEmpty
print("isEmpty:", not bool(queue))

# Size
print("Size:", len(queue))


# ⚠️ Note:

# Removing the first element (pop(0)) is slow for big queues,
# because Python shifts all elements one step left after removal.

# 🧱 Queue using a Class (Better Way)
# This is more organized and easy to expand later.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage
myQueue = Queue()
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue:", myQueue.queue)
print("Peek:", myQueue.peek())
print("Dequeue:", myQueue.dequeue())
print("Queue after Dequeue:", myQueue.queue)
print("isEmpty:", myQueue.isEmpty())
print("Size:", myQueue.size())


# 🔗 Queue using Linked List (Advanced but Efficient)

# Linked lists make queue operations faster because
# we don’t need to shift elements in memory.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        self.length -= 1
        return temp.data

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()

# Example usage
myQueue = Queue()
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue:", end="")
myQueue.printQueue()
print("Peek:", myQueue.peek())
print("Dequeue:", myQueue.dequeue())
print("Queue after Dequeue:", end="")
myQueue.printQueue()
print("isEmpty:", myQueue.isEmpty())
print("Size:", myQueue.size())


# ⚖️ Comparison: List vs Linked List Queue
# | Feature             | Using List                    | Using Linked List               |
# | ------------------- | ----------------------------- | ------------------------------- |
# | **Speed**           | Slow when removing from front | Fast (no shifting needed)       |
# | **Memory Use**      | Less                          | More (each node stores pointer) |
# | **Size**            | Fixed if using arrays         | Grows dynamically               |
# | **Code Complexity** | Simple                        | More complex                    |


# 💡 Real-Life Applications of Queues
# | Application                    | Description                                         |
# | ------------------------------ | --------------------------------------------------- |
# | **Task Scheduling**            | OS uses queues to manage processes.                 |
# | **Printer Jobs**               | First document sent to printer prints first.        |
# | **Customer Service Systems**   | First call received is handled first.               |
# | **Breadth-First Search (BFS)** | Queue helps explore nodes level by level in graphs. |
# | **Message Queues**             | Used in distributed systems for task processing.    |
