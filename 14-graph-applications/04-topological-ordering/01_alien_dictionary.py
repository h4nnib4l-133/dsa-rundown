import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Alien Dictionary (LC #269) -- Hard
# Input:  words: List[str] (sorted in alien alphabet order)
# Output: str (valid character order, or '' if impossible)
# Given words in alien alphabet order, figure out the character ordering.
#
# Example:
# #   ["wrt","wrf","er","ett","rftt"]  -> "wertf"
#   ["z","x","z"]  -> "" (contradiction)
#
#   WHY THIS IS A TOPOLOGICAL SORT:
#   Adjacent word pairs reveal ordering constraints (first differing char).
#   Build directed graph of char -> char. Topologically sort.
#
#   Key: Extract edges from adjacent word pairs. Run Kahn's BFS or DFS topsort.
#        Handle edge case: if word2 is a prefix of word1 in wrong order, invalid.

def alien_order(words):
    pass


def solve(words, expected_valid):
    result = alien_order(words)
    if not expected_valid:
        return result == ''
    if not result:
        return False
    pos = {c: i for i, c in enumerate(result)}
    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        found = False
        for a, b in zip(w1, w2):
            if a != b:
                if pos.get(a, -1) >= pos.get(b, -1):
                    return False
                found = True
                break
        if not found and len(w1) > len(w2):
            return False
    return True

run_tests(alien_order, [
    ((["wrt","wrf","er","ett","rftt"], True),  True),
    ((["z","x","z"], False),                    True),     # returns '' correctly
    ((["ab","adc"], True),                      True),
    ((["abc","ab"], False),                     True),
])
