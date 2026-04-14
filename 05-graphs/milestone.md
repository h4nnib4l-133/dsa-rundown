# Basic Graph Algorithms

## The Patterns

1. **BFS** -- shortest path in unweighted graphs, level-order traversal. Use queue.
2. **DFS** -- cycle detection, connected components, topological sort. Use stack/recursion.
3. **Topological sort** -- DAG ordering. Kahn's (BFS + indegree) or DFS post-order.
4. **Union-Find** -- connected components, cycle detection in undirected graphs.
5. **Dijkstra** -- shortest path in weighted graphs (non-negative). Min-heap.

**Representations:**
- Adjacency list: `graph[u] = [(v, w), ...]` -- most common
- Grid as implicit graph: neighbors are up/down/left/right cells

**C tips:** Adjacency list with array of linked lists or 2D array. BFS queue with circular buffer or array.

---

## Problems

### 1. Number of Islands (LC #200) -- Medium
Count islands in a 2D binary grid.
- **Key:** DFS/BFS flood fill. Mark visited cells. Count connected components of '1's.
- **Files:** `01_num_islands.py`, `01_num_islands.c`

### 2. BFS Shortest Reach (HackerRank) -- Medium
Find shortest distances from a start node to all others in unweighted graph.
- **Key:** Standard BFS. Distance = level * edge_weight.
- **Files:** `02_bfs_shortest.py`, `02_bfs_shortest.c`

### 3. Course Schedule (LC #207) -- Medium
Can you finish all courses given prerequisites? (Cycle detection in directed graph)
- **Key:** Topological sort with Kahn's algorithm. If sorted count != numCourses, cycle exists.
- **Alternative:** DFS with 3 colors (white/gray/black)
- **Files:** `03_course_schedule.py`, `03_course_schedule.c`

### 4. Clone Graph (LC #133) -- Medium
Deep copy a connected undirected graph.
- **Key:** BFS/DFS with hashmap {original -> clone}
- **Files:** `04_clone_graph.py`, `04_clone_graph.c`

### 5. Pacific Atlantic Water Flow (LC #417) -- Medium
Find cells that can flow to both Pacific and Atlantic oceans.
- **Key:** Reverse thinking -- BFS/DFS from ocean borders inward. Intersect reachable sets.
- **Files:** `05_pacific_atlantic.py`, `05_pacific_atlantic.c`

### 6. Number of Connected Components (LC #323) -- Medium
Count connected components in undirected graph.
- **Key:** DFS/BFS from each unvisited node, or Union-Find
- **Files:** `06_connected_components.py`, `06_connected_components.c`

### 7. Rotting Oranges (LC #994) -- Medium
Minimum time for all oranges to rot. Multi-source BFS.
- **Key:** Add all rotten oranges to queue initially. BFS level = time.
- **Files:** `07_rotting_oranges.py`, `07_rotting_oranges.c`

### 8. Word Ladder (LC #127) -- Hard
Shortest transformation sequence from beginWord to endWord.
- **Key:** BFS where neighbors differ by exactly one character.
- **Optimization:** Pattern matching with wildcards, e.g., `h*t` matches `hot`, `hat`
- **Files:** `08_word_ladder.py`, `08_word_ladder.c`

### 9. Is Graph Bipartite? (LC #785) -- Medium
Can graph be 2-colored?
- **Key:** BFS/DFS coloring. If neighbor has same color, not bipartite.
- **Files:** `09_bipartite.py`, `09_bipartite.c`

### 10. Network Delay Time (LC #743) -- Medium
Min time for signal to reach all nodes from source.
- **Key:** Dijkstra's algorithm. Answer = max of all shortest distances.
- **Files:** `10_network_delay.py`, `10_network_delay.c`
