import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Edit Distance (LC #72) -- Medium
# Given two words, find minimum operations to convert word1 to word2.
# Operations: insert a char, delete a char, replace a char.
#
# Example:
#   "horse" -> "ros" = 3
#     horse -> rorse (replace h with r)
#     rorse -> rose  (delete r)
#     rose  -> ros   (delete e)
#
#   "intention" -> "execution" = 5
#
#   Key: dp[i][j] = edit distance of word1[0:i] and word2[0:j].
#        If chars match: dp[i-1][j-1] (no operation needed).
#        Else: 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
#              (delete,   insert,   replace)

def min_distance(word1, word2):
    pass


run_tests(min_distance, [
    (("horse", "ros"),           3),
    (("intention", "execution"), 5),
    (("", "abc"),                3),     # 3 inserts
    (("abc", ""),                3),     # 3 deletes
    (("abc", "abc"),             0),     # identical
    (("a", "b"),                 1),     # single replace
    (("", ""),                   0),     # both empty
    (("kitten", "sitting"),      3),     # classic example
    (("sunday", "saturday"),     3),     # insert a,t + replace n->r
])
