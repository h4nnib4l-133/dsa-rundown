# DSA Revision

300 Python problems organized by topic and pattern.

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
  01-bitmask-dp-graph/         (5 algo + 5 app)
  02-dag-dp/                   (5 algo + 5 app)
  03-shortest-path-as-dp/      (5 algo + 5 app)
  04-tree-dp/                  (5 algo + 5 app)
  05-grid-dp-as-graph/         (5 algo + 5 app)

greedy-patterns/               50 problems -- greedy sub-patterns
  01-interval-scheduling/      (5 algo + 5 app)  meeting rooms, taps, events
  02-heap-greedy/              (5 algo + 5 app)  IPO, furthest building
  03-exchange-argument/        (5 algo + 5 app)  sort-by-custom-key, pairing
  04-two-pointer-greedy/       (5 algo + 5 app)  sort+scan from both ends
  05-sort-and-scan/            (5 algo + 5 app)  pair/reduce after sort
```

## algo_ vs app_ prefix

Within pattern folders:

- **algo_*.py** -- direct algorithm practice. The problem explicitly asks for the pattern.
- **app_*.py** -- story problems. You must RECOGNIZE which pattern to use.

## Running

```bash
cd ~/PC/dsa-revision
python3 core/01-binary-search/01_search_sorted.py
python3 greedy-patterns/02-heap-greedy/app_02_ipo.py
```

Imports auto-locate the repo root -- works at any depth.

## File format

```python
# Problem Name (LC #xxx) -- Difficulty
# Input:  types
# Output: type
# Description
#
# Example:
#   input -> output  (why)
#
#   Key / Greedy insight: algorithm hint

def solve(...):
    pass                  # <-- write here

run_tests(solve, [...])   # tests pre-written
```

## Totals

| Section | Problems |
|---|---|
| core | 100 |
| dp-patterns | 50 |
| graph-patterns | 50 |
| hybrid-patterns | 50 |
| greedy-patterns | 50 |
| **Total** | **300** |
