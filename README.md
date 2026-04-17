# DSA Revision

250 Python problems organized by topic and pattern.

## Start Here

1. Open `PROGRESS.md` -- the checklist
2. Pick a folder based on what you want to practice
3. Open a `.py` file: problem description is at the top
4. Write the function, run it: `python3 <path>/<file>.py`

## Structure

```
core/                          100 problems -- standard topic revision
  01-binary-search/            (10)
  02-dynamic-programming/      (10)
  03-strings/                  (10)
  04-linked-lists/             (10)
  05-graphs/                   (10)
  06-arrays-sorting/           (10)
  07-stacks-queues/            (10)
  08-trees/                    (10)
  09-recursion-backtracking/   (10)
  10-greedy/                   (10)

dp-patterns/                   50 problems -- DP sub-patterns
  01-subarray-kadane/          (5 algo + 5 app)
  02-stock-state-machine/      (5 algo + 5 app)
  03-knapsack-variants/        (5 algo + 5 app)
  04-grid-dp/                  (5 algo + 5 app)
  05-string-sequence-dp/       (5 algo + 5 app)

graph-patterns/                50 problems -- graph sub-patterns
  01-bfs/                      (5 algo + 5 app)
  02-dfs/                      (5 algo + 5 app)
  03-shortest-path/            (5 algo + 5 app)
  04-union-find/               (5 algo + 5 app)
  05-topological-sort/         (5 algo + 5 app)

hybrid-patterns/               50 problems -- DP + Graph combined
  01-bitmask-dp-graph/         (5 algo + 5 app)  TSP, visit all nodes
  02-dag-dp/                   (5 algo + 5 app)  topsort + DP
  03-shortest-path-as-dp/      (5 algo + 5 app)  Bellman-Ford, weighted BFS
  04-tree-dp/                  (5 algo + 5 app)  House Robber III, cameras
  05-grid-dp-as-graph/         (5 algo + 5 app)  Cherry Pickup, Dungeon
```

## algo_ vs app_ prefix

Within pattern folders:

- **algo_*.py** — direct algorithm practice. The problem statement explicitly
  asks for the pattern (e.g., "implement shortest path").
- **app_*.py** — story problems. Harder: you must RECOGNIZE which pattern to use.
  (e.g., "Minimum cookies to distribute fairly" = bitmask DP.)

This split is deliberate: knowing an algorithm and recognizing when to apply it
are different skills. Application problems train the second one.

## Running

```bash
cd ~/PC/dsa-revision
python3 core/01-binary-search/01_search_sorted.py
python3 hybrid-patterns/04-tree-dp/algo_04_binary_tree_cameras.py
```

Imports work at any depth — the test runner auto-locates the repo root.

## File format

```python
# Problem Name (LC #xxx) -- Difficulty
# Input:  types
# Output: type
# Description
#
# Example:
#   input -> output  (explanation)
#
#   Pattern: BFS / Kadane / etc.
#   Key: algorithm hint

def solve(...):
    pass                  # <-- write solution here

run_tests(solve, [...])   # pre-written tests
```

## Timeline (2 days)

- **Day 1**: core/ (topics 01–05) + dip into dp-patterns/ and graph-patterns/
- **Day 2**: core/ (topics 06–10) + application drills + hybrid-patterns/

## Totals

| Section | Problems |
|---|---|
| core | 100 |
| dp-patterns | 50 |
| graph-patterns | 50 |
| hybrid-patterns | 50 |
| **Total** | **250** |
