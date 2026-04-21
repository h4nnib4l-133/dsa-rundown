import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Long Pressed Name (LC #925) -- Easy
# Input:  name: str, typed: str
# Output: bool (could typed be name with some keys long-pressed?)
# Some keys in name may be held too long (repeated). Check if typed is valid.
#
# Example:
# #   name="alex", typed="aaleex" -> True
#   name="saeed", typed="ssaaedd" -> False
#
#   Greedy insight: Two pointers: i on name, j on typed. Advance j always. If mismatch, j must match j-1.

def is_long_pressed_name(name, typed):
    pass

run_tests(is_long_pressed_name, [
    (("alex", "aaleex"),     True),
    (("saeed", "ssaaedd"),   False),
    (("leelee", "lleeelee"), True),
    (("laiden", "laiden"),   True),
    (("alex", "aaleexa"),    False),
])
