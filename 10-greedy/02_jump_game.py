import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Jump Game (LC #55) -- Medium
# Can you reach the last index?
#
#   Key: Track farthest reachable index. At each position, update `farthest = max(farthest, i + nums[i])`.

def can_jump(nums):
    pass


run_tests(can_jump, [
    (([2,3,1,1,4],), True),
    (([3,2,1,0,4],), False),
    (([0],),         True),
])
