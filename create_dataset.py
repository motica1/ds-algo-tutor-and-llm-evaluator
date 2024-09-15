from langsmith import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = Client()
dataset_name = "week1_prj_evaluation_data_structure_algo_tutor"

inputs = [
    "Explain DFS and BFS with examples. Make sure to detail the differences between the two and then share some real life applications that use these.",
    "Teach me iterative programming with examples and make me practise it.",
    "If i want to get the shortest travel plan between two countries, which algorithm should i use?",
    "what are stacks and queues?",
    "Tell me all the sorting algorithms",
    "Explain the Dijkstra's algorithm",
    "What is the difference between a stack and a queue?",
    "What is exactly a linked list?",
    "How do you implement a binary search tree?",
    "What is a hash table?"
]

outputs = [
    """Sure! Let's break down Depth-First Search (DFS) and Breadth-First Search (BFS) with examples, highlight their differences, and discuss some real-life applications.

### Depth-First Search (DFS)

**Definition:** DFS is a traversal algorithm that starts at a specified node and explores as far as possible along each branch before backtracking. It uses a stack data structure (or recursion) to keep track of the nodes to be visited next.

**Example:**
Imagine you have a tree structure like this:

```
      A
     / \
    B   C
   / \   \
  D   E   F
```

If we perform DFS starting from node A, the traversal order could be:
1. Visit A
2. Go to B
3. Go to D (no more children, backtrack to B)
4. Go to E (no more children, backtrack to B, then to A)
5. Go to C
6. Go to F (no more children)

The order of traversal would be: **A, B, D, E, C, F**.

### Breadth-First Search (BFS)

**Definition:** BFS is a traversal algorithm that starts at a specified node and explores all the neighboring nodes at the current level before moving on to the next level. It uses a queue data structure to keep track of the nodes to be visited next.

**Example:**
Using the same tree structure:

```
      A
     / \
    B   C
   / \   \
  D   E   F
```

If we perform BFS starting from node A, the traversal order would be:
1. Visit A
2. Visit B and C (next level)
3. Visit D and E (next level from B)
4. Visit F (next level from C)

The order of traversal would be: **A, B, C, D, E, F**.

### Key Differences Between DFS and BFS

| Feature          | Depth-First Search (DFS)       | Breadth-First Search (BFS)       |
|------------------|---------------------------------|----------------------------------|
| **Data Structure**| Uses a stack (or recursion)     | Uses a queue                     |
| **Traversal Order**| Explores as far down a branch as possible before backtracking | Explores all neighbors at the current level before going deeper |
| **Memory Usage** | Can be more memory
"""
,
    """"
    Absolutely! Iterative programming is a fundamental concept where you repeat a set of instructions until a certain condition is met. This is often done using loops, such as `for` loops and `while` loops.

### Let's Start with an Example: Factorial Calculation

The factorial of a number \( n \) (denoted as \( n! \)) is the product of all positive integers less than or equal to \( n \). For example:
- \( 5! = 5 \times 4 \times 3 \times 2 \times 1 = 120 \)

#### Iterative Approach to Calculate Factorial

Here's how you can calculate the factorial of a number iteratively:

1. **Initialize a variable to hold the result (let's call it `result`) and set it to 1.**
2. **Use a loop to multiply `result` by each number from 1 to `n`.**
3. **Return `result` after the loop ends.**

Here's the code in JavaScript:

```javascript
function factorialIterative(n) {
    let result = 1; // Step 1: Initialize result
    for (let i = 1; i <= n; i++) { // Step 2: Loop from 1 to n
        result *= i; // Multiply result by i
    }
    return result; // Step 3: Return the result
}

console.log(factorialIterative(5)); // Output: 120
```

### Now It's Your Turn to Practice!

**Task:** Write a function to calculate the sum of all numbers from 1 to \( n \) iteratively.

#### Steps to Follow:
1. **Create a function named `sumIterative`.**
2. **Initialize a variable to hold the sum (let's call it `sum`) and set it to 0.**
3. **Use a loop to add each number from 1 to `n` to `sum`.**
4. **Return `sum` after the loop ends.**

Give it a try! Write the code and share it with me. If you get stuck, let me know where you need help!
    """
,
 """" To find the shortest travel plan between two countries, you would typically use **Dijkstra's algorithm** if the graph representing the countries and their connections (like roads or flight paths) has non-negative edge weights (costs). 

Dijkstra's algorithm is efficient for finding the shortest path in a graph where the edges have weights that represent the cost of traveling between nodes (in this case, countries). 

If your graph has negative edge weights (which can happen if there are discounts or penalties associated with certain routes), you would want to use the **Bellman-Ford algorithm**, as it can handle negative weights.

Would you like to dive deeper into how Dijkstra's algorithm works or see an example?
    """
,
 """"Stacks and queues are both linear data structures that store collections of elements, but they differ in how elements are added and removed.

### Stacks:
- **Definition**: A stack is a collection of elements that follows the Last In, First Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed.
- **Operations**:
  - **Push**: Add an element to the top of the stack. (O(1))
  - **Pop**: Remove and return the top element of the stack. (O(1))
  - **Peek**: Return the top element without removing it. (O(1))
- **Use Cases**: Stacks are often used in scenarios like function call management (call stack), undo mechanisms in applications, and parsing expressions.

**Example**:
Imagine a stack of plates. You can only take the top plate off (pop) or add a new plate on top (push).

### Queues:
- **Definition**: A queue is a collection of elements that follows the First In, First Out (FIFO) principle. This means that the first element added to the queue is the first one to be removed.
- **Operations**:
  - **Enqueue**: Add an element to the end of the queue. (O(1))
  - **Dequeue**: Remove and return the front element of the queue. (O(1))
  - **Peek**: Return the front element without removing it. (O(1))
- **Use Cases**: Queues are commonly used in scenarios like task scheduling, managing requests in a server, and breadth-first search in graphs.

**Example**:
Think of a line at a ticket counter. The first person in line is the first to be served (dequeue), and new people join the end of the line (enqueue).

Would you like to see more details or examples about stacks and queues?
    """
,
 """"Sure! Here’s a list of common sorting algorithms along with a brief description of each:

### 1. **Bubble Sort**
- **Description**: A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until no swaps are needed.
- **Time Complexity**: O(n^2)

### 2. **Selection Sort**
- **Description**: This algorithm repeatedly finds the minimum element from the unsorted portion of the array and moves it to the beginning. It divides the array into a sorted and an unsorted part.
- **Time Complexity**: O(n^2)

### 3. **Insertion Sort**
- **Description**: This algorithm builds the final sorted array one item at a time. It takes each element from the unsorted part and finds the appropriate position in the sorted part.
- **Time Complexity**: O(n^2)

### 4. **Merge Sort**
- **Description**: A divide-and-conquer algorithm that splits the array into halves, sorts each half recursively, and then merges the sorted halves back together.
- **Time Complexity**: O(n log n)

### 5. **Quick Sort**
- **Description**: Another divide-and-conquer algorithm that selects a 'pivot' element, partitions the array into elements less than and greater than the pivot, and recursively sorts the partitions.
- **Time Complexity**: O(n log n) on average, O(n^2) in the worst case.

### 6. **Heap Sort**
- **Description**: This algorithm uses a binary heap data structure to sort elements. It first builds a max heap from the array, then repeatedly extracts the maximum element and rebuilds the heap.
- **Time Complexity**: O(n log n)

### 7. **Counting Sort**
- **Description**: A non-comparison-based sorting algorithm that counts the occurrences of each unique element and uses this information to place each element in its correct position.
- **Time Complexity**: O(n + k), where k is the range of the input.

### 8. **Radix Sort**
- **Description**: A non-comparison-based sorting algorithm that sorts numbers by processing individual digits. It uses counting sort as a subroutine to sort the numbers based on each digit.
- **Time Complexity**: O(nk), where k is the number of digits in the largest number
    """
,
 """"Dijkstra's algorithm is a popular algorithm used to find the shortest path from a starting node (or vertex) to all other nodes in a weighted graph with non-negative edge weights. It is widely used in various applications, such as routing and navigation systems.

### How Dijkstra's Algorithm Works:

1. **Initialization**:
   - Start by assigning a tentative distance value to every node. Set the initial node's distance to 0 and all other nodes' distances to infinity (∞).
   - Create a priority queue (or a min-heap) to keep track of nodes to explore, starting with the initial node.

2. **Exploration**:
   - While there are nodes to explore in the priority queue:
     - Remove the node with the smallest tentative distance (let's call this node `current`).
     - For each neighbor of the `current` node:
       - Calculate the distance from the start node to this neighbor through the `current` node.
       - If this calculated distance is less than the previously recorded distance for this neighbor, update the neighbor's distance and set its predecessor to the `current` node.
       - Add the neighbor to the priority queue if it is not already there or update its position if its distance has changed.

3. **Repeat**:
   - Repeat the exploration process until all nodes have been processed or the priority queue is empty.

4. **Result**:
   - Once the algorithm completes, you will have the shortest distance from the starting node to all other nodes in the graph. You can also reconstruct the shortest path to any node by following the predecessor pointers.

### Example:

Consider a graph with nodes A, B, C, and D, and the following weighted edges:
- A to B (weight 1)
- A to C (weight 4)
- B to C (weight 2)
- B to D (weight 5)
- C to D (weight 1)

**Steps**:
1. Initialize distances: A=0, B=∞, C=∞, D=∞.
2. Start with A, update neighbors:
   - B: distance = 1 (A to B)
   - C: distance = 4 (A to C)
3. Next, explore B (smallest distance):
   - C: distance = 3 (A to B to C, which is 1 + 2)
   - D: distance = 6 (A to B
    """
,
 """"The main difference between a stack and a queue lies in how they manage the order of elements when adding and removing them. Here’s a concise comparison:

### Stack:
- **Order of Operations**: Last In, First Out (LIFO)
  - The last element added to the stack is the first one to be removed.
- **Key Operations**:
  - **Push**: Add an element to the top of the stack.
  - **Pop**: Remove and return the top element of the stack.
  - **Peek**: Return the top element without removing it.
- **Use Cases**: 
  - Function call management (call stack), undo mechanisms in applications, parsing expressions.

**Example**: Think of a stack of plates. You can only take the top plate off (pop) or add a new plate on top (push).

### Queue:
- **Order of Operations**: First In, First Out (FIFO)
  - The first element added to the queue is the first one to be removed.
- **Key Operations**:
  - **Enqueue**: Add an element to the end of the queue.
  - **Dequeue**: Remove and return the front element of the queue.
  - **Peek**: Return the front element without removing it.
- **Use Cases**: 
  - Task scheduling, managing requests in a server, breadth-first search in graphs.

**Example**: Think of a line at a ticket counter. The first person in line is the first to be served (dequeue), and new people join the end of the line (enqueue).

### Summary:
- **Stack**: LIFO structure, where the last element added is the first to be removed.
- **Queue**: FIFO structure, where the first element added is the first to be removed.

Would you like to know more about how to implement stacks and queues in code?
    """
,
 """"A **linked list** is a linear data structure that consists of a sequence of elements, called **nodes**, where each node contains two main components:

1. **Data**: The value or information that the node holds.
2. **Pointer (or Reference)**: A reference to the next node in the sequence. This allows the nodes to be linked together.

### Characteristics of Linked Lists:
- **Dynamic Size**: Unlike arrays, linked lists can grow and shrink in size dynamically as elements are added or removed. This makes them more flexible in terms of memory usage.
- **Non-contiguous Memory**: The nodes in a linked list are not stored in contiguous memory locations. Each node can be located anywhere in memory, and they are connected via pointers.

### Types of Linked Lists:
1. **Singly Linked List**:
   - Each node contains a pointer to the next node in the sequence.
   - Traversal is only possible in one direction (from the head to the tail).

   **Structure**:
   ```
   [Data | Next] -> [Data | Next] -> [Data | Next] -> null
   ```

2. **Doubly Linked List**:
   - Each node contains two pointers: one to the next node and one to the previous node.
   - This allows traversal in both directions (forward and backward).

   **Structure**:
   ```
   null <- [Prev | Data | Next] <-> [Prev | Data | Next] <-> [Prev | Data | Next] -> null
   ```

3. **Circular Linked List**:
   - The last node points back to the first node, forming a circle.
   - Can be singly or doubly linked.

   **Structure** (Singly Circular):
   ```
   [Data | Next] -> [Data | Next] -> [Data | Next] --+
      ^                                               |
      +-----------------------------------------------+
   ```

### Advantages of Linked Lists:
- **Dynamic Size**: They can easily grow or shrink as needed.
- **Efficient Insertions/Deletions**: Adding or removing nodes can be done without shifting elements, as is required in arrays.

### Disadvantages of Linked Lists:
- **Memory Overhead**: Each node requires extra memory for the pointer/reference.
- **No Random Access**: Unlike arrays, linked lists do not allow direct access to elements. You must traverse the list to find a specific node.

### Example
    """
,
 """"
 Implementing a Binary Search Tree (BST) involves creating a data structure that allows for efficient insertion, deletion, and searching of elements. A BST is a tree where each node has at most two children, and for any given node:
- The left child's value is less than the parent's value.
- The right child's value is greater than the parent's value.

### Basic Structure of a Node:
First, we define a class for the nodes of the tree:

```python
class Node:
    def __init__(self, key):
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child
        self.value = key  # The value of the node
```

### Binary Search Tree Class:
Next, we create a class for the Binary Search Tree itself, which will include methods for insertion, searching, and traversal.

```python
class BinarySearchTree:
    def __init__(self):
        self.root = None  # The root of the tree

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)  # If the tree is empty, set the root
        else:
            self._insert_recursively(self.root, key)  # Call the recursive insert function

    def _insert_recursively(self, node, key):
        if key < node.value:  # If the key is less than the current node's value
            if node.left is None:
                node.left = Node(key)  # Insert as left child
            else:
                self._insert_recursively(node.left, key)  # Recur on the left subtree
        else:  # If the key is greater than or equal to the current node's value
            if node.right is None:
                node.right = Node(key)  # Insert as right child
            else:
                self._insert_recursively(node.right, key)  # Recur on the right subtree

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        if node is None or node.value == key:  # Base case: found or reached a leaf
            return node
    """
,
 """A **hash table** (or hash map) is a data structure that stores key-value pairs and provides efficient access to the values based on their keys. It uses a hash function to compute an index (or hash code) into an array of buckets or slots, from which the desired value can be found.

### Key Characteristics of Hash Tables:

1. **Key-Value Pair Storage**:
   - Each entry in a hash table consists of a unique key and an associated value. The key is used to retrieve the value.

2. **Hash Function**:
   - A hash function takes an input (the key) and produces an integer (the hash code), which is then used to determine the index in the underlying array where the value will be stored. A good hash function minimizes collisions and distributes keys uniformly across the array.

3. **Collision Handling**:
   - A collision occurs when two keys hash to the same index. There are several strategies to handle collisions:
     - **Chaining**: Each index in the array points to a linked list (or another data structure) that holds all entries that hash to the same index.
     - **Open Addressing**: When a collision occurs, the algorithm searches for the next available slot in the array according to a probing sequence (e.g., linear probing, quadratic probing).

4. **Efficiency**:
   - Hash tables offer average-case time complexity of O(1) for search, insert, and delete operations, making them very efficient for lookups. However, the worst-case time complexity can degrade to O(n) if many collisions occur and the hash table is poorly designed.

### Basic Operations:

1. **Insertion**:
   - Compute the hash code for the key using the hash function.
   - If there is no collision, store the key-value pair at the computed index.
   - If there is a collision, use the collision handling strategy to store the pair.

2. **Search**:
   - Compute the hash code for the key.
   - Access the index in the array and check if the key exists. If there are collisions, traverse the linked list (or probe) to find the key.

3. **Deletion**:
   - Compute the hash code for the key.
   - Access the index and remove the key-value pair, handling any necessary adjustments if using chaining or open addressing.

### Example:

Here’s a simple example of a hash table implementation in Python using chaining for collision resolution:


    """
]

# Store
dataset = client.create_dataset(
    dataset_name=dataset_name,
    description="QA pairs about Leetcode Tutor model.",
)
client.create_examples(
    inputs=[{"question": q} for q in inputs],
    outputs=[{"answer": a} for a in outputs],
    dataset_id=dataset.id,
)