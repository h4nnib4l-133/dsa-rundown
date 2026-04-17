import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Minimum Genetic Mutation (LC #433) -- Medium
# Input:  start: str, end: str (8-char gene), bank: List[str] (valid genes)
# Output: int (min mutations to transform start -> end, -1 if impossible)
# Gene is 8 chars from {A,C,G,T}. Each mutation changes one character.
# Each intermediate gene must be in bank.
#
# Example:
# #   start="AACCGGTT", end="AACCGGTA", bank=["AACCGGTA"]  -> 1
#   start="AACCGGTT", end="AAACGGTA", bank=["AACCGGTA","AACCGCTA","AAACGGTA"]  -> 2
#
#   WHY THIS IS A BFS SHORTEST PATH:
#   Same pattern as Word Ladder. States are genes. Edges between genes
#   differing by one character. BFS for minimum mutations.
#
#   Key: BFS. For each gene, try replacing each position with A/C/G/T.
#        Check if resulting gene is in bank and unvisited.

def min_mutation(start, end, bank):
    pass

run_tests(min_mutation, [
    (("AACCGGTT", "AACCGGTA", ["AACCGGTA"]),                1),
    (("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]),  2),
    (("AACCGGTT", "AACCGGTT", []),                          0),     # same
    (("AACCGGTT", "AAAAAAAA", ["AAAAAAAA"]),               -1),     # too far
])
