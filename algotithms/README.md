# Algorithms

## Recursion

|   Algorithm    | Time Complexity  | Space Complexity  |
|:--------------:|:----------------:|:-----------------:|
|    Factorial   |       O(-)       |        O(-)       |
|    Fibonacci   |       O(-)       |        O(-)       |
| Euclid Primes  |       O(-)       |        O(-)       |

### 1. Fibonacci

### 2. Factorial

### 3. Euclid Primes

## Searching

|      Algorithm       |  Time Complexity |    Space Complexity  |
|:--------------------:|:----------------:|:--------------------:|
|     Linear Search    |       O(N)       |         O(1)         |
|     Binary Search    |      O(logN)     |    O(1) / O(logN)    |
|      Jump Search     |       O(-)       |         O(-)         |
|    Ternary Search    |       O(-)       |         O(-)         |
|  Exponential Search  |       O(-)       |         O(-)         |
|  Depth First Search  |       O(-)       |         O(-)         |
| Breadth First Search |       O(-)       |         O(-)         |

### 1. Linear Search
---------------------
Linear search tries to search for a value by looping through each element of the list one-by-one. If the element is found, the algorithm stops and returns the result. Otherwise, the algorithm continues till the last element, if it is not exist, it will return False. Its run complexity is O(n), which is not great.

### 2. Jump Search
---------------------
This algorithm is similar to the Linear Search algorithm, but it has some adjustments. It divides the array into several blocks. Each block has the size of √n. Then we check if the last item is less than the target or not. If it is greater, we search this block linearly.

### 3. Binary Search
---------------------
The Binary Search algorithm is arguably the best, but it requires your array to be sorted. It simply works by getting the middle index and comparing it with your target. If the target is greater than the middle, it will ignore the left part and search the right part. Remember the array is sorted. It will repeat this process until finding the target. The special thing about binary search is that it runs in O(log(n)).

Binary Search can be implemented recursively or iterable. The recursive method requires a space complexity of O(log(n)) , as it will store the recursive calls on the heap. However, this is negligible as it’s not memory-consuming to store this tiny space. Moreover, the recursive call implementation is cleaner. The iterable method requires a space complexity of O(1).

### 4. Ternary Search
---------------------
Ternary Search is another algorithm that is similar to Binary Search. It works by dividing the array into three parts instead of two and checking some five conditions instead of three. By dividing the array into 3 parts, we get 2 middle items. First, we will check if any of those 2 middle items equals the target. If not, we will determine which part of the array the target is in and recursively search it.

### 5. Exponential Search
The Exponential Search uses the Binary Search algorithm but in a different way. It starts with an element of the array and compares it with the target. If the target is greater, it doubles the number of elements taken from the array. Typically this number is called bound. If the bound is greater than the target, we search the array from bound /2 to bound. In this search, we use binary search. This algorithm runs in O(log(i)) not O(log(n)) because we only search from the bound to its half.

### 6. Depth First Search - DFS
There are 3 ways of traversing a Binary Tree using DFS: `in-order`, `pre-order`, and `post-order` traversal.

`In-order traversal` traverses the left subtree of the current node, followed by the current node, and finally, the right subtree. Starting from the root, we move to the root’s left child and keep going down until we find a node with no left child. Since this node doesn’t have a right child, we move backward. As this node has a right child, we move here. This node doesn’t have any children, so we go backward. We repeat these steps for the rest of the tree’s nodes If applied to a binary search tree, output is in ascending order.

`Pre-order traversal` first visits the current node, then traverses the left subtree, and finally, the right subtree. We visit the root and move to its left child. We visit it. We move to its left child and visit it. Then we go backward and move to the right child. We repeat the same steps for the rest of the tree’s nodes.

`post-order traversal` 

- Target a point far away from the starting vertex/node.
- Applications:
    - Solving puzzles with only one solution like mazes.
    - Detecting cycles in graphs.
    - Finding shortest path in weighted graphs.

### 7. Breadth First Search - BFS
BFS starts from the root and visits every node of every tree level before going on to the next level.

- Target a point close to the starting vertex/node.
- Applications:
    - Web crawling
    - Finding shortest path in unweighted graphs
    - Finding connected locations using GPS.

## Sorting

|   Algorithm    |   Time Complexity    | Space Complexity  |
|:--------------:|:--------------------:|:-----------------:|
| Insertion Sort |                      |        O(1)       |
| Selection Sort |                      |        O(1)       |
|   Bubble Sort  |                      |        O(1)       |
|    Merge Sort  |                      |        O(N)       |
|     Heap Sort  |                      |        O(1)       |
|    Quick Sort  |                      |      O(logN)      |
|    Shell Sort  |                      |        O(-)       |

### 1. Insertion Sort
---------------------

### 2. Selection Sort
---------------------

### 3. Bubble Sort
------------------

### 4. Merge Sort
-----------------

### 5. Heap Sort
----------------

### 6. Quick Sort
-----------------

### 7. Shell Sort
-----------------

## Graph

|   Algorithm    |   Time Complexity    | Space Complexity  |
|:--------------:|:--------------------:|:-----------------:|
|     Kruskal    |                      |        O(-)       |
|      Prims     |                      |        O(-)       |

### 1. Kruskal

### 2. Prims

## Path finding

|   Algorithm    |   Time Complexity    | Space Complexity  |
|:--------------:|:--------------------:|:-----------------:|
|     Dijstra    |                      |        O(-)       |
|        A*      |                      |        O(-)       |
|  Backtracking  |                      |        O(-)       |

### 1. Dijstra

### 2. A* path finding

### 3. Backtracking

## Cryptography

|   Algorithm    |   Time Complexity    | Space Complexity  |
|:--------------:|:--------------------:|:-----------------:|
|  Chemo cipher  |                      |        O(-)       |
| Caesar cipher  |                      |        O(-)       |
|  Morse cipher  |                      |        O(-)       |
|      Luhn      |                      |        O(-)       |

### 1. Chemo cipher

### 2. Caesar cipher

### 3. Morse cipher

### 4. Luhn

