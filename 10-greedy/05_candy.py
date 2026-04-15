import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Candy (LC #135) -- Hard
# Children in a line with ratings. Give candies such that:
#   1. Each child gets at least 1 candy.
#   2. Higher rating than neighbor -> more candy than that neighbor.
# Return minimum total candies.
#
# Example:
#   [1,0,2] -> 5  (candies: [2,1,2])
#   [1,2,2] -> 4  (candies: [1,2,1])  (equal rating, no requirement)
#
#   Key: Two passes.
#        Left-to-right: if rating[i] > rating[i-1], candy[i] = candy[i-1]+1.
#        Right-to-left: if rating[i] > rating[i+1], candy[i] = max(candy[i], candy[i+1]+1).
#        Sum all candies.

def candy(ratings):
    pass


run_tests(candy, [
    (([1,0,2],),        5),     # [2,1,2]
    (([1,2,2],),        4),     # [1,2,1]
    (([1,3,2,2,1],),    7),     # [1,2,1,2,1]? let's check: [1,2,1,2,1]? rating[3]=2>rating[4]=1 so candy[3]>candy[4]. [1,2,1,2,1]=7 ✓
    (([1],),            1),     # single child
    (([1,2,3],),        6),     # [1,2,3]
    (([3,2,1],),        6),     # [3,2,1]
    (([1,2,3,2,1],),    9),     # mountain: [1,2,3,2,1]
    (([1,1,1],),        3),     # all equal: [1,1,1]
])
