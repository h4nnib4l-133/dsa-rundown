# DSA Revision for HackerRank

~150 Python problems organized by topic AND by sub-pattern.

## Start Here

1. Open `PROGRESS.md` -- that's your checklist
2. Pick a topic folder
3. Open a `.py` file -- read the problem description at the top, then write the function
4. Run it: `python3 <path>/<file>.py`
5. Move to the next problem

## Structure

### Core topics (100 problems, 10 per topic)

```
01-binary-search/           Binary search patterns
02-dynamic-programming/     1D, 2D, knapsack, string DP
03-strings/                 Sliding window, two pointers
04-linked-lists/            Pointer manipulation
05-graphs/                  BFS, DFS, toposort, Dijkstra
06-arrays-sorting/          Two pointers, prefix sums, intervals
07-stacks-queues/           Monotonic stack, deque
08-trees/                   Traversals, BST
09-recursion-backtracking/  Subsets, permutations
10-greedy/                  Interval scheduling
```

### Sub-pattern drills — "Algorithm-focused"

```
11-dp-algo/
  01-subarray-kadane/            Kadane patterns, subarray sums
  02-stock-state-machine/        Buy/sell with states
  03-knapsack-variants/          0/1, unbounded, multi-dim
  04-grid-dp/                    Grid traversal DP
  05-string-sequence-dp/         LCS, edit distance family

12-graph-algo/
  01-grid-bfs-dfs/               Flood fill, multi-source BFS
  02-topological-sort/           Kahn's / DFS post-order
  03-shortest-path/              Dijkstra, Bellman-Ford
  04-union-find/                 Connected components
  05-cycle-detection/            Directed vs undirected
```

### Sub-pattern drills — "Application-focused"

These look like story problems — the challenge is **identifying which pattern to use**.

```
13-dp-applications/
  01-subarray-kadane/            Transform + Kadane (like Max Server Redundancy)
  02-stock-state-machine/        Real-world state machines (House Robber II, etc.)
  03-knapsack-variants/          Disguised knapsack (Perfect Squares, etc.)
  04-grid-dp/                    Paint House, Paint Fence style
  05-string-sequence-dp/         Subsequence counting problems

14-graph-applications/
  01-bfs-shortest-path/          Open Lock, Word Ladder, Bus Routes
  02-dfs-connectivity/           Keys and Rooms, Evaluate Division
  03-union-find-grouping/        Smallest String w/ Swaps, Accounts Merge
  04-topological-ordering/       Alien Dict, Parallel Courses, Recipes
  05-graph-modeling/             Sliding Puzzle, Reconstruct Itinerary
                                 (problems that LOOK non-graph but ARE)
```

## Running

```bash
cd ~/PC/dsa-revision
python3 01-binary-search/01_search_sorted.py
python3 14-graph-applications/05-graph-modeling/01_sliding_puzzle.py
```

## File format

Every `.py` file has this structure:

```python
# Problem Name (LC #xxx) -- Difficulty
# Input:  types
# Output: type
# Description
#
# Example:
#   input -> output  (why)
#
#   Key: algorithm hint

def solve(...):
    pass      # <-- you write here

run_tests(solve, [
    # tests pre-written
])
```

## Timeline (2 days)

- **Day 1**: Core topics 01-05 + dip into sub-patterns 11, 12
- **Day 2**: Core topics 06-10 + application problems 13, 14

## Key idea

- **Algo folders (11, 12)** — drill the pattern itself
- **Application folders (13, 14)** — practice IDENTIFYING the pattern from a story

The hardest part of interviews is recognizing "this story problem wants Dijkstra"
or "this needs Kadane with a transformation." That's what the application
folders train.
