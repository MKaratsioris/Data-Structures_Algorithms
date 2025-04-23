# Algorithms

## Recursion

|        Algorithm      | Time Complexity  | Space Complexity  |
|:---------------------:|:----------------:|:-----------------:|
|    Factorial recur    |        O(n)      |        O(n)       |
|    Factorial iter     |        O(n)      |        O(1)       |
|  Fibonacci recur-n    |       O(2^n)     |        O(n)       |
|  Fibonacci recur-mem  |        O(n)      |        O(n)       |
|    Fibonacci iter     |        O(n)      |        O(1)       |
|    Fibonacci analyt   |        O(1)      |        O(1)       |
| Euclidean GCD - recur | O(log min(a, b)) | O(log min(a, b))  |
| Euclidean GCD - iter  | O(log min(a, b)) |        O(1)       |
|     Prime number      |        O(√n)     |        O(1)       |

## Searching

| Algorithm | Best Time | Average Time | Worst Time | Space | Data Type | Notes |
|:---------:|:---------:|:------------:|:----------:|:-----:|:---------:|:-----:|
| Linear Search | O(1) | O(n) | O(n) | O(1) | Array/List | No need for sorting |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) or O(log n) | Sorted Array | Requires sorted data |
| Jump Search | O(1) | O(√n) | O(√n) | O(1) | Sorted Array | Balance between linear & binary |
| Ternary Search | O(1) | O(log₃ n) | O(log₃ n) | O(log n) | Sorted Array | Less efficient than binary in practice |
| Exponential Search | O(1) | O(log n) | O(log n) | O(log n) | Sorted Array | Efficient for unbounded arrays |
| Depth-First Search (DFS) | O(1) | O(V + E) | O(V + E) | O(V) | Graph/Tree | Recursive or using a stack |
| Breadth-First Search (BFS) | O(1) | O(V + E) | O(V + E) | O(V) | Graph/Tree | Uses a queue, finds shortest path |

NOTE: n = number of elements (array); V = vertices, E = edges (graph)

### 1. Linear Search
- Scans each element until it finds the target.
- Works on unsorted arrays.
- Simple, but inefficient for large data.

Linear search tries to search for a value by looping through each element of the list one-by-one. If the element is found, the algorithm stops and returns the result. Otherwise, the algorithm continues till the last element, if it is not exist, it will return False. Its run complexity is O(n), which is not great.

### 2. Binary Search
- Divide-and-conquer on sorted data.
- Repeatedly halves the search range.
- Very efficient, but needs sorting first.

The Binary Search algorithm is arguably the best, but it requires your array to be sorted. It simply works by getting the middle index and comparing it with your target. If the target is greater than the middle, it will ignore the left part and search the right part. Remember the array is sorted. It will repeat this process until finding the target. The special thing about binary search is that it runs in O(log(n)).

Binary Search can be implemented recursively or iterable. The recursive method requires a space complexity of O(log(n)) , as it will store the recursive calls on the heap. However, this is negligible as it’s not memory-consuming to store this tiny space. Moreover, the recursive call implementation is cleaner. The iterable method requires a space complexity of O(1).

### 3. Jump Search
- Jumps ahead by a fixed block size (√n), then linear search in the block.
- Trade-off: fewer comparisons than linear, easier than binary.

This algorithm is similar to the Linear Search algorithm, but it has some adjustments. It divides the array into several blocks. Each block has the size of √n. Then we check if the last item is less than the target or not. If it is greater, we search this block linearly.

### 4. Ternary Search
- Similar to binary, but divides into 3 parts.
- Theoretically O(log₃ n), but in practice it's usually slower than binary due to more comparisons per step.

Ternary Search is another algorithm that is similar to Binary Search. It works by dividing the array into three parts instead of two and checking some five conditions instead of three. By dividing the array into 3 parts, we get 2 middle items. First, we will check if any of those 2 middle items equals the target. If not, we will determine which part of the array the target is in and recursively search it.

### 5. Exponential Search
- Doubles the range until the target is exceeded, then binary search in that range.
- Very useful when the array size is unknown or infinite (e.g., streams).

The Exponential Search uses the Binary Search algorithm but in a different way. It starts with an element of the array and compares it with the target. If the target is greater, it doubles the number of elements taken from the array. Typically this number is called bound. If the bound is greater than the target, we search the array from bound /2 to bound. In this search, we use binary search. This algorithm runs in O(log(i)) not O(log(n)) because we only search from the bound to its half.

### 6. Depth First Search - DFS
- Explores as deep as possible before backtracking.
- Can be recursive or stack-based.
- Useful for pathfinding, cycle detection, and topological sorting.

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
- Explores all neighbors before going deeper.
- Uses a queue.
- Finds shortest path in unweighted graphs.

- Target a point close to the starting vertex/node.
- Applications:
    - Web crawling
    - Finding shortest path in unweighted graphs
    - Finding connected locations using GPS.

## Sorting

| Algorithm | Best Time | Average Time | Worst Time | Space | In-place | Stable |
|:---------:|:---------:|:------------:|:----------:|:-----:|:--------:|:------:|
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ✅ | ❌ |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ❌ | ✅ |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ✅ | ❌ |
| Shell Sort | O(n log n)* | O(n log² n)* | O(n²)* | O(1) | ✅ | ❌ |

NOTE: Shell Sort complexities vary based on the gap sequence used.

## Graph

|   Algorithm    |   Time Complexity    | Space Complexity  |
|:--------------:|:--------------------:|:-----------------:|
|     Kruskal    |                      |        O(-)       |
|      Prims     |                      |        O(-)       |

## Path finding

|   Algorithm    |   Time Complexity    | Space Complexity  |
|:--------------:|:--------------------:|:-----------------:|
|     Dijstra    |                      |        O(-)       |
|        A*      |                      |        O(-)       |
|  Backtracking  |                      |        O(-)       |

## Cryptography

|   Algorithm    |   Time Complexity    | Space Complexity  |
|:--------------:|:--------------------:|:-----------------:|
|  Chemo cipher  |                      |        O(-)       |
| Caesar cipher  |                      |        O(-)       |
|  Morse cipher  |                      |        O(-)       |
|      Luhn      |                      |        O(-)       |