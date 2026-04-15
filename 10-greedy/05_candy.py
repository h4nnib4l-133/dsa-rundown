import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Candy (LC #135) -- Hard
# Min candies for children with ratings. Higher rating than neighbor = more candy.
#
#   Key: Two passes. Left-to-right: if rating increases, increment. Right-to-left: same. Take max at each position.

def candy(ratings):
    pass


run_tests(candy, [
    (([1,0,2],),    5),
    (([1,2,2],),    4),
    (([1,3,2,2,1],),7),
])
