import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Word Break as Graph Reachability (LC #139) -- Medium
# Input:  s: str, wordDict: List[str]
# Output: bool (True if s can be segmented into dictionary words)
# Can s be split into words from dictionary?
#
# Normally solved with DP, but can ALSO be modeled as graph reachability:
# Nodes = string positions 0..n. Edge from i to j if s[i:j] in dict.
# Question: is n reachable from 0?
#
# Example:
# #   s="leetcode", dict=["leet","code"]  -> True
#
#   WHY THIS IS A GRAPH REACHABILITY (non-obvious):
#   String positions are nodes. Each valid word placement is an edge.
#   BFS/DFS from position 0 asking 'can I reach n?' is equivalent to DP.
#
#   Key: BFS from index 0. From i, push j (i<j<=n) if s[i:j] is in dict.
#        Return True if n reached. Visited set avoids re-exploration.

def word_break(s, word_dict):
    pass

run_tests(word_break, [
    (("leetcode", ["leet","code"]),         True),
    (("applepenapple", ["apple","pen"]),     True),
    (("catsandog", ["cats","dog","and"]),    False),
    (("a", ["a"]),                           True),
    (("", ["a"]),                            True),
])
