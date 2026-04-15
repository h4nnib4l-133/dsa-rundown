import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Word Break (LC #139) -- Medium
# Can string s be segmented into words from dictionary?
#
#   State: `dp[i]` = can s[0..i] be segmented?
#   Transition: `dp[i] = any(dp[j] and s[j:i] in dict)` for j < i

def word_break(s, word_dict):
    pass


run_tests(word_break, [
    (("leetcode", ["leet","code"]),             True),
    (("applepenapple", ["apple","pen"]),        True),
    (("catsandog", ["cats","dog","sand","and","cat"]), False),
    (("a", ["a"]),                              True),
    (("ab", ["a"]),                             False),
])
