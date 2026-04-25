# 8-Puzzle-Solver-Using-BFS-DFS-and-A-Search-Algorithms
Project
Course: Artificial Intelligence Lab

Course Code: CSE-316

Section : 232_d4

Mahinul Islam Rabby - 232002011

Thiaba Rahman Methi - 232002042

An interactive Artificial Intelligence project that solves the classic 8-puzzle problem using three search algorithms: Breadth-First Search (BFS), Depth-First Search (DFS), and A* Search. This project also includes a GUI built with Tkinter to visualize the puzzle and solution steps.

The 8-puzzle problem is a sliding puzzle consisting of a 3×3 grid with 8 numbered tiles and one empty space. The goal is to transform an initial configuration into a predefined goal state by moving tiles. This project demonstrates how different AI search algorithms solve the same problem with varying efficiency.

**Algorithms Used**
**1.Breadth-First Search (BFS)**
1. Start with the initial puzzle state.
2. Add the initial state to a queue.
3. Mark the initial state as visited.
4. While the queue is not empty:
   a. Remove the front state from the queue.
   b. Check if it is the goal state.
      - If yes, return the solution path.
   c. Generate all possible child states by moving the blank tile.
   d. For each child state:
      - If it is not visited:
        i. Mark it as visited.
        ii. Add it to the queue.
5. If no solution is found, return failure.


**Depth-First Search (DFS)**
1. Start with the initial puzzle state.
2. Add the initial state to a stack.
3. Mark the initial state as visited.
4. While the stack is not empty:
   a. Pop the top state from the stack.
   b. Check if it is the goal state.
      - If yes, return the solution path.
   c. If the current depth is less than the maximum depth:
      i. Generate all possible child states.
      ii. For each child state:
          - If it is not visited:
            Add it to the stack.
5. If no solution is found, return failure.


**A Stear Search**
1. Start with the initial puzzle state.
2. Calculate:
   f(n) = g(n) + h(n)

   Where:
   g(n) = cost from initial state to current state
   h(n) = Manhattan distance heuristic

3. Add the initial state to a priority queue.
4. While the priority queue is not empty:
   a. Remove the state with the lowest f(n) value.
   b. Check if it is the goal state.
      - If yes, return the solution path.
   c. Generate all possible child states.
   d. For each child state:
      i. Calculate g(n), h(n), and f(n).
      ii. Add the child state to the priority queue.
5. If no solution is found, return failure.

   
**Technologies Used**
1. Python 3.x
2. Tkinter (GUI)
3. collections (deque)
4. heapq (priority queue)
5. time module
6. random module

GOAL_STATE = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

**Input:**

[ 1  2  3 ]
[ 4  0  6 ]
[ 7  5  8 ]

**Output**

Step 1:
[ 1  2  3 ]
[ 4  0  6 ]
[ 7  5  8 ]

Step 2:
[ 1  2  3 ]
[ 4  5  6 ]
[ 7  0  8 ]

Step 3 (Goal):
[ 1  2  3 ]
[ 4  5  6 ]
[ 7  8  0 ]
