import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Backspace String Compare (LC #844) -- Easy
# Input:  s: str, t: str ('#' represents backspace)
# Output: bool (do s and t produce same result after backspaces?)
# Simulate typing. '#' deletes previous char. Compare final strings.
#
# Example:
# #   s="ab#c", t="ad#c" -> True ("ac" == "ac")
#   s="a##c", t="#a#c" -> True ("c" == "c")
#
#   Greedy insight: Can do stack simulation, or two pointers from END counting '#' skips (O(1) space).

def backspace_compare(s, t):
    pass

run_tests(backspace_compare, [
    (("ab#c", "ad#c"),    True),
    (("ab##", "c#d#"),    True),
    (("a##c", "#a#c"),    True),
    (("a#c", "b"),        False),
    (("", ""),            True),
])
