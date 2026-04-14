import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def is_match(s, p):
    """'.' matches any char, '*' matches zero or more of preceding"""
    pass


run_tests(is_match, [
    (("aa", "a"),      False),
    (("aa", "a*"),     True),
    (("ab", ".*"),     True),
    (("aab", "c*a*b"), True),
    (("mississippi", "mis*is*p*."), False),
])
