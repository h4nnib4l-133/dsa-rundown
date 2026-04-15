import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Word Ladder (LC #127) -- Hard
# Input:  beginWord: str, endWord: str, wordList: List[str]
# Output: int (length of shortest sequence including start+end, or 0)
# Transform beginWord to endWord, changing one letter at a time.
# Each intermediate word must be in wordList.
# Return LENGTH of shortest transformation sequence (including start+end), or 0.
#
# Example:
#   begin="hit", end="cog", words=["hot","dot","dog","lot","log","cog"]
#   hit -> hot -> dot -> dog -> cog  = 5
#
#   Key: BFS where neighbors differ by exactly one character.
#        Optimization: wildcard patterns like "h*t" -> ["hot","hat"].

def ladder_length(begin_word, end_word, word_list):
    """Return length of shortest transformation, 0 if impossible"""
    pass


run_tests(ladder_length, [
    (("hit", "cog", ["hot","dot","dog","lot","log","cog"]),  5),
    (("hit", "cog", ["hot","dot","dog","lot","log"]),        0),    # endWord not in list
    (("hot", "dog", ["hot","dog","dot"]),                    3),    # hot->dot->dog
    (("a", "c", ["a","b","c"]),                              2),    # a->c
    (("hit", "hit", ["hit"]),                                1),    # already there? (edge case)
])
