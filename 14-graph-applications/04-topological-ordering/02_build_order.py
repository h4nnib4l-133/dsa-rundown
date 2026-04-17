import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Build System Task Ordering (custom) -- Medium
# Input:  tasks: List[str], deps: List[[prereq, dependent]]
# Output: List[str] (valid build order, or [] if circular)
# Given tasks with dependencies, return an order to execute them.
#
# Example:
# #   tasks=["compile","link","test"], deps=[["compile","link"],["link","test"]]
#   -> ["compile","link","test"]
#
#   WHY THIS IS A TOPOLOGICAL SORT:
#   Classic dependency resolution. Build DAG, topsort.
#
#   Key: Kahn's algorithm. Track indegree. Process nodes with indegree 0.

def build_order(tasks, deps):
    pass


def solve(tasks, deps):
    result = build_order(tasks, deps)
    if not result:
        return len(deps) > 0 or len(tasks) == 0  # only empty if circular or no tasks
    if len(result) != len(tasks):
        return False
    pos = {t: i for i, t in enumerate(result)}
    for a, b in deps:
        if pos[a] >= pos[b]:
            return False
    return True

run_tests(solve, [
    ((["compile","link","test"], [["compile","link"],["link","test"]]), True),
    ((["a","b","c"], [["a","b"],["b","c"],["c","a"]]),                  True),     # cycle -> []
    ((["a"], []),                                                        True),
    ((["a","b"], []),                                                    True),
])
