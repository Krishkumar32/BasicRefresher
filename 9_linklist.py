# Q1. What is a Linked List?

# 👉 A linked list is a data structure made up of nodes.
# Each node has two parts:

# Data (value)
# Pointer (link) to the next node

#Example:
    [10 | next] → [20 | next] → [30 | next] → None

# Q2. How is a Linked List different from an Array?

# | Feature                         | **Array** | **Linked List**   |
# | ------------------------------- | --------- | ----------------- |
# | Fixed size                      | Yes       | No                |
# | Continuous memory               | Yes       | No                |
# | Can access any element directly | Yes       | No                |
# | Easy to insert/delete           | No        | Yes               |
# | Uses extra memory for links     | No        | Yes               |
# | Built-in structure in languages | Yes       | No (we create it) |

# In short:
# Arrays are faster to access elements.
# Linked lists are flexible to grow or shrink.

# Q3. Why use a Linked List instead of an Array?

# ✅ Use Linked List when:
# You don’t know the size of the data in advance.
# You need to insert or delete elements often.
# ❌ Don’t use Linked List when:
# You need to access elements quickly using index numbers.

# Q4. What are the types of Linked Lists?

# Singly Linked List → Each node points to the next node only.
# Example: 1 → 2 → 3 → None

# Doubly Linked List → Each node points to both previous and next node.
# Example: None ← 1 ↔ 2 ↔ 3 → None

# Circular Linked List → The last node points back to the first node.
# Example: 1 → 2 → 3 → (back to 1)

# Q5. What are the basic operations of a Linked List?

# ✅ Main operations:

# Traversal → Go through all nodes one by one.

# Insertion → Add a new node.

# Deletion → Remove a node.

# Searching → Find a particular value.

# Sorting → Arrange nodes in order.

# Q6. What is Traversal in Linked List?

# ➡ Traversal means moving from the head node to the last node, visiting each node.

# Example (Python):
    
    def traverse(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Q7. How to find the smallest value in a Linked List?

# ➡ Traverse the list and keep checking for the lowest value.

# Example:

def find_min(head):
    min_val = head.data
    current = head.next
    while current:
        if current.data < min_val:
            min_val = current.data
        current = current.next
    return min_val

# Q8. How to delete a node in a Linked List?

# ➡ First connect the previous node to the next node of the one you want to delete.

# Steps:

# Find the node before the one to delete.

# Change its next link to skip the deleted node.

# Example:

def delete_node(head, node_to_delete):
    if head == node_to_delete:
        return head.next  # deleting head node

    current = head
    while current.next and current.next != node_to_delete:
        current = current.next

    if current.next:
        current.next = current.next.next

    return head

# Q9. How to insert a node in a Linked List?

# ➡ Create a new node and connect it properly between nodes.

# Example:

def insert_at_position(head, new_node, position):
    if position == 1:
        new_node.next = head
        return new_node

    current = head
    for _ in range(position - 2):
        current = current.next

    new_node.next = current.next
    current.next = new_node
    return head

# Q10. What is the time complexity of Linked List operations?

# | Operation                      | **Time Complexity** |
# | ------------------------------ | ------------------- |
# | Traversal                      | O(n)                |
# | Search                         | O(n)                |
# | Insertion (at beginning)       | O(1)                |
# | Deletion (known node)          | O(1)                |
# | Insertion/Deletion (at middle) | O(n)                |
# | Random Access                  | ❌ Not possible      |

# Q11. Why can’t we do binary search on linked lists?

# ➡ Because binary search needs direct access to the middle element (like arr[mid]),
# but in a linked list, we can only go one node at a time.

# Q12. Advantages of Linked List

# ✅ Flexible size
# ✅ Easy to insert/delete nodes
# ✅ Efficient memory usage for dynamic data

# Q13. Disadvantages of Linked List

# ❌ Uses extra memory for pointers
# ❌ No direct access (must traverse)
# ❌ More complex to program than arrays



# simple code for linklist:
class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

current =node1
while current is not None :
    print(current.data,end="->")
    current = current.next
    
print("None")


#code for travesing:
class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


head = node1
current =head
while current is not None :
    print(current.data,end="->")
    current = current.next
    
print("None")







#insertion in linklist in beginning:
class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
    #creating new nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
 #adding a new node at the beginning
head = node1
new_node = Node(70)
new_node.next = head
head =new_node
 #printing data
current =head
while current is not None :
    print(current.data,end="->")
    current = current.next
    
print("None")





#insertion in linklist in end :
class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
    #creating new nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
 #adding a new node at the end
new_node =Node(60)
head =node1
current = head
while current.next is not None:
    current = current.next
current.next = new_node
 #printing data
current =head
while current is not None :
    print(current.data,end="->")
    current = current.next
    
print("None")




#insertion in linklist at specific position :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# creating new nodes
node1 = Node(10)   
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# linking nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# adding a new node after 20
new_node = Node(25)

current = node1
while current is not None:
    if current.data == 20:
        new_node.next = current.next
        current.next = new_node
        break
    current = current.next

# printing the data
head = node1
current = head
while current is not None:
    print(current.data, end="->")
    current = current.next
print("None")











# deletion of linklist :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# creating new nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# linking the nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# define head of the list
head = node1

# delete the first node (move head to the next node)
if head is not None:
    head = head.next   # head now starts from 20

# print the linked list after deletion
current = head
while current is not None:
    print(current.data, end="->")
    current = current.next
print("None")




# delete the last node :
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# creating new nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# linking the nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# set head
head = node1

# delete the last node
current = head
while current.next.next is not None:
    current = current.next
current.next = None   # remove the last node (50)

# print the updated list
current = head
while current is not None:
    print(current.data, end="->")
    current = current.next
print("None")




# delete the particular data:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# creating new nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# linking the nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# head of the linked list
head = node1

# delete node with data = 30
current = head
while current.next is not None:
    if current.next.data == 30:
        current.next = current.next.next
        break
    current = current.next

# print the linked list
current = head
while current is not None:
    print(current.data, end="->")
    current = current.next
print("None")






