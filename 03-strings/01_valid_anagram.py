import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def is_anagram(s, t):
    pass


run_tests(is_anagram, [
    (("anagram", "nagaram"), True),
    (("rat", "car"),         False),
    (("a", "a"),             True),
    (("ab", "a"),            False),
    (("", ""),               True),
])
