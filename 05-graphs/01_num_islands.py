# ============================================================
# PATTERN: GRAPHS
# ============================================================
# 1. **BFS** -- shortest path in unweighted graphs, level-order traversal. Use queue.
# 2. **DFS** -- cycle detection, connected components, topological sort. Use stack/recursion.
# 3. **Topological sort** -- DAG ordering. Kahn's (BFS + indegree) or DFS post-order.
# 4. **Union-Find** -- connected components, cycle detection in undirected graphs.
# 5. **Dijkstra** -- shortest path in weighted graphs (non-negative). Min-heap.
#
# **Representations:**
# - Adjacency list: `graph[u] = [(v, w), ...]` -- most common
# - Grid as implicit graph: neighbors are up/down/left/right cells
#
# **C tips:** Adjacency list with array of linked lists or 2D array. BFS queue with circular buffer or array.
#
# ---
# ============================================================

import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Number of Islands (LC #200) -- Medium
# Input:  grid: List[List[str]] ('1' = land, '0' = water)
# Output: int (number of islands)
# Given 2D grid of '1' (land) and '0' (water), count number of islands.
# An island is surrounded by water and formed by connecting adjacent lands
# (horizontal/vertical, NOT diagonal).
#
# Example:
#   [["1","1","0","0","0"],
#    ["1","1","0","0","0"],      -> 3 islands
#    ["0","0","1","0","0"],
#    ["0","0","0","1","1"]]
#
#   Key: DFS/BFS flood fill. For each unvisited '1', start DFS to mark
#        all connected land as visited. Count how many times you start DFS.

def num_islands(grid):
    pass


run_tests(num_islands, [
    (([["1","1","1","1","0"],
       ["1","1","0","1","0"],
       ["1","1","0","0","0"],
       ["0","0","0","0","0"]],), 1),     # one big island
    (([["1","1","0","0","0"],
       ["1","1","0","0","0"],
       ["0","0","1","0","0"],
       ["0","0","0","1","1"]],), 3),     # three islands
    (([["0","0","0"],
       ["0","0","0"]],),         0),     # no land
    (([["1"]],),                 1),     # single cell island
    (([["0"]],),                 0),     # single cell water
    (([["1","0","1","0","1"]],), 3),     # single row, 3 islands
    (([["1"],["0"],["1"]],),     2),     # single column, 2 islands
])
