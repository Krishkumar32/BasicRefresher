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
