import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# House Robber (LC #198) -- Medium
# Max money from non-adjacent houses.
#
#   State: `dp[i]` = max money considering houses 0..i
#   Transition: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

def rob(nums):
    pass


run_tests(rob, [
    (([1,2,3,1],),       4),
    (([2,7,9,3,1],),    12),
    (([2,1,1,2],),       4),
    (([0],),             0),
    (([100],),         100),
])
