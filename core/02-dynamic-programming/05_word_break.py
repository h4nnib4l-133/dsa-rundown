import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Word Break (LC #139) -- Medium
# Input:  s: str, word_dict: List[str]
# Output: bool (True if s can be segmented into words from dict)
# Given string s and dictionary of words, can s be segmented into
# a sequence of dictionary words?
#
# Example:
#   s = "leetcode", dict = ["leet","code"]    -> True  ("leet" + "code")
#   s = "applepenapple", dict = ["apple","pen"] -> True ("apple"+"pen"+"apple")
#   s = "catsandog", dict = ["cats","dog","sand","and","cat"] -> False
#
#   Key: dp[i] = can s[0:i] be segmented?
#        dp[i] = True if any dp[j] and s[j:i] in dict, for j < i.

def word_break(s, word_dict):
    pass


run_tests(word_break, [
    (("leetcode", ["leet","code"]),                         True),
    (("applepenapple", ["apple","pen"]),                    True),
    (("catsandog", ["cats","dog","sand","and","cat"]),       False),
    (("a", ["a"]),                                          True),
    (("ab", ["a"]),                                         False),
    (("", ["a"]),                                           True),    # empty string
    (("aaaaaaa", ["aaa","aaaa"]),                            True),   # 3+4 or 4+3
    (("aaaaaab", ["aaa","aaaa"]),                            False),  # can't end with b
    (("cars", ["car","ca","rs"]),                            True),   # ca + rs
])
