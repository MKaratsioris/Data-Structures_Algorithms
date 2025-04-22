# Data Structures


## 1. Array
- Description: A collection of items stored in a fixed sequence.
- Use Case: Ideal for quick access when the position is known.

## 2. Single / Double Linked List
- Description: A sequence of nodes where each node points to the next.
- Use Case: Flexible for adding or removing elements dynamically.

## 3. Queue
- Description: A line where items are added at the back and removed from the front.
- Use Case: Best for task management and order processing.

## 4. Stack
- Description: A collection of elements with Last In, First Out (LIFO) access.
- Use Case: Useful for undo operations and managing function calls.

## 5. Dictionary | HashTable | HashMap
- Description: A data structure that uses keys for quick value retrieval.
- Use Case: Effective for fast data access and implementing dictionaries.

## 6. HashSet
- Description: A collection that stores unique items and supports fast membership checks.
- Use Case: Useful for eliminating duplicates and tracking unique values.

## 7. Tree
- Description: A hierarchical structure with a single root and branching nodes.
- Use Case: Useful for representing organizational hierarchies or family trees.

## 8. Trie
- Description: A tree-like structure used for storing strings with shared prefixes.
- Use Case: Ideal for tasks like autocomplete and spell-checking.

## 9. Max Heap
- Description: A tree-based structure where the largest value is always at the root.
- Use Case: Efficient for operations where the largest element needs to be accessed frequently.

## 10. Graph
- Description: A set of nodes connected by edges.
- Use Case: Perfect for mapping relationships, like social networks or transportation systems.


## Space-Time Complexity
|    Data Structure   |  Access |    Search   |    Insert   |    Delete   |  Space Complexity |
|:-------------------:|:-------:|:-----------:|:-----------:|:-----------:|:-----------------:|
|         Array       |   O(1)  |     O(N)    |     O(N)          O(N)    |        O(N)       |
|     Linked Lists    |   O(N)  |     O(N)    |     O(1)    |     O(1)    |        O(N)       |
|         Queue       |   O(N)  |     O(N)    |     O(1)    |     O(1)    |        O(N)       |
|         Stack       |   O(N)  |     O(N)    |     O(1)    |     O(1)    |        O(N)       |
|      Dictionary     |    -    | O(1) / O(N) | O(1) / O(N) | O(1) / O(N) |        O(N)       |
|        HashSet      |    -    |     O(1)    |     O(1)    |     O(1)    |        O(N)       |
|         Tree        |   O(-)  |     O(-)    |     O(-)    |     O(-)    |        O(-)       |
|         Trie        |   O(-)  |     O(-)    |     O(-)    |     O(-)    |        O(-)       |
|       Max Heap      |   O(-)  |     O(-)    |     O(-)    |     O(-)    |        O(-)       |
|         Graph       |   O(-)  |     O(-)    |     O(-)    |     O(-)    |        O(-)       |