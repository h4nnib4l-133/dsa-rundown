import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Edit Distance (LC #72) -- Medium
# Min operations (insert/delete/replace) to transform word1 -> word2.
#
#   State: `dp[i][j]` = edit distance of word1[0..i], word2[0..j]
#   Transition: Match: `dp[i-1][j-1]`. Else: `1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`

def min_distance(word1, word2):
    pass


run_tests(min_distance, [
    (("horse", "ros"),        3),
    (("intention", "execution"), 5),
    (("", "abc"),             3),
    (("abc", ""),             3),
    (("abc", "abc"),          0),
])
