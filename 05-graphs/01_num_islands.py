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
# Count islands in a 2D binary grid.
#
#   Key: DFS/BFS flood fill. Mark visited cells. Count connected components of '1's.

def num_islands(grid):
    pass


run_tests(num_islands, [
    (([["1","1","1","1","0"],
       ["1","1","0","1","0"],
       ["1","1","0","0","0"],
       ["0","0","0","0","0"]],), 1),
    (([["1","1","0","0","0"],
       ["1","1","0","0","0"],
       ["0","0","1","0","0"],
       ["0","0","0","1","1"]],), 3),
])
