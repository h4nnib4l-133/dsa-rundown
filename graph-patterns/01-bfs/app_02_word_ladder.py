import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Word Ladder (LC #127) -- Hard
# Input:  beginWord: str, endWord: str, wordList: List[str]
# Output: int (length of shortest transformation sequence, 0 if impossible)
# Transform beginWord to endWord, changing one letter at a time.
# Each intermediate word must be in wordList.
#
# Example:
# #   begin="hit", end="cog", words=["hot","dot","dog","lot","log","cog"]
#   hit -> hot -> dot -> dog -> cog = length 5
#
#   WHY THIS IS A BFS SHORTEST PATH:
#   States are words. Edge between two words if they differ by exactly one letter.
#   Min transformations = shortest path in this word graph. BFS for unweighted shortest.
#
#   Key: BFS. For each word, generate all one-letter mutations and check membership in set.
#        Optimization: use wildcard patterns (h*t maps to [hat, hot]) for O(L*26) neighbors.

def ladder_length(begin_word, end_word, word_list):
    pass

run_tests(ladder_length, [
    (("hit", "cog", ["hot","dot","dog","lot","log","cog"]),  5),
    (("hit", "cog", ["hot","dot","dog","lot","log"]),        0),
    (("a", "c", ["a","b","c"]),                              2),
    (("hot", "dog", ["hot","dog","dot"]),                    3),
])
