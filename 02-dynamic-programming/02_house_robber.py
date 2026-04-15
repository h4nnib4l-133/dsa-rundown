import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# House Robber (LC #198) -- Medium
# Array of money in each house. Can't rob two adjacent houses.
# Return max money you can rob.
#
# Example:
#   [1,2,3,1] -> 4  (rob house 0 + house 2: 1+3)
#   [2,7,9,3,1] -> 12  (rob house 0+2+4: 2+9+1)
#
#   Key: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
#        "skip this house" vs "rob this house + best from 2 back".

def rob(nums):
    pass


run_tests(rob, [
    (([1,2,3,1],),         4),     # skip 1,3 -> take 0,2
    (([2,7,9,3,1],),      12),     # take 0,2,4
    (([2,1,1,2],),         4),     # take first and last
    (([0],),               0),     # zero money
    (([100],),           100),     # single house
    (([1,2],),             2),     # two houses, take bigger
    (([2,1],),             2),     # two houses, take first
    (([1,3,1,3,100],),   103),     # skip middle, take 1+100 or 3+100
    (([10,1,1,10],),      20),     # take first and last
    (([0,0,0,0],),         0),     # all zero
])
