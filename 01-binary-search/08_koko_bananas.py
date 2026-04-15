import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Koko Eating Bananas (LC #875) -- Medium
# Koko eats bananas at speed k. Find minimum k to finish all piles in h hours.
#
#   Key: Binary search on answer. For each k, check if `sum(ceil(pile/k)) <= h`

def min_eating_speed(piles, h):
    pass


run_tests(min_eating_speed, [
    (([3,6,7,11], 8),       4),
    (([30,11,23,4,20], 5),  30),
    (([30,11,23,4,20], 6),  23),
    (([1000000000], 2),     500000000),
])
