import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Koko Eating Bananas (LC #875) -- Medium
# Koko eats bananas at speed k (bananas/hour). She has h hours.
# Each hour she picks a pile and eats k bananas from it.
# If pile has < k bananas, she eats the whole pile and waits.
# Find minimum integer k to finish all piles in h hours.
#
# Example:
#   piles = [3,6,7,11], h = 8
#   k=4: hours = ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4) = 1+2+2+3 = 8 <= 8 ✓
#   k=3: hours = 1+2+3+4 = 10 > 8 ✗
#   -> 4
#
#   Key: Binary search on answer (k). lo=1, hi=max(piles).
#        For each k, check if total hours <= h.

def min_eating_speed(piles, h):
    pass


run_tests(min_eating_speed, [
    (([3,6,7,11], 8),         4),      # basic case
    (([30,11,23,4,20], 5),   30),      # h = num piles -> must eat biggest in 1 hour
    (([30,11,23,4,20], 6),   23),      # one extra hour helps
    (([1000000000], 2),       500000000),  # huge pile
    (([3,6,7,11], 4),        11),      # h = num piles, must eat each in 1 hour
    (([1,1,1,1], 4),          1),      # all piles size 1
    (([2,2], 4),              1),      # enough time for speed 1
    (([312884470], 312884469), 2),     # just barely enough time
])
