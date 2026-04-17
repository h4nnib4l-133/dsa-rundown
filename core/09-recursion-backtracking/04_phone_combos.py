import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Letter Combinations of Phone Number (LC #17) -- Medium
# Input:  digits: str (string of digits '2'-'9')
# Output: List[str] (all possible letter combinations)
# Map digits to letters, generate all combinations.
#
#   Key: Backtrack through digits. For each digit, try all mapped letters.

def letter_combinations(digits):
    pass


run_tests(letter_combinations, [
    (("23",),  sorted(["ad","ae","af","bd","be","bf","cd","ce","cf"])),
    (("",),    []),
    (("2",),   ["a","b","c"]),
])
