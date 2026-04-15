import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Letter Combinations of Phone Number (LC #17) -- Medium
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
