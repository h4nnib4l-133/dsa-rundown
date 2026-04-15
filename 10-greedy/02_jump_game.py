import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Jump Game (LC #55) -- Medium
# Input:  nums: List[int] (max jump length at each position)
# Output: bool (True if you can reach the last index)
# Array of max jump lengths. Start at index 0.
# Return True if you can reach the last index.
#
# Example:
#   [2,3,1,1,4] -> True  (0->1->4 or 0->2->3->4)
#   [3,2,1,0,4] -> False (stuck at index 3, which has 0)
#
#   Key: Track farthest reachable index.
#        At each i: if i > farthest, can't reach here -> False.
#        Update farthest = max(farthest, i + nums[i]).

def can_jump(nums):
    pass


run_tests(can_jump, [
    (([2,3,1,1,4],),  True),
    (([3,2,1,0,4],),  False),    # stuck at 0
    (([0],),           True),     # already at end
    (([1,0],),         True),     # jump 1 to reach end
    (([0,1],),         False),    # stuck at index 0
    (([2,0,0],),       True),     # jump over zeros
    (([1,1,1,1],),     True),     # step by step
    (([5,0,0,0,0],),   True),     # big first jump
])
