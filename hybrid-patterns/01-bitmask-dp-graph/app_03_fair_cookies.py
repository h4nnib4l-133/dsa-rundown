import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Fair Distribution of Cookies (LC #2305) -- Medium
# Input:  cookies: List[int], k: int (children)
# Output: int (minimize MAX cookies given to any child)
# Distribute bags of cookies (all) among k children.
# Minimize the maximum total any child receives.
#
# Example:
# #   cookies=[8,15,10,20,8], k=2  -> 31
#
#   Pattern: BITMASK DP
#   Key: dp[k][mask] = min of max when k children distributed cookies in mask.
#        For each submask of mask, dp[k][mask] = min(max(dp[k-1][mask^sub], sum(sub))).

def distribute_cookies(cookies, k):
    pass

run_tests(distribute_cookies, [
    (([8,15,10,20,8], 2),         31),
    (([6,1,3,2,2,4,1,2], 3),       7),
    (([1,2,3], 3),                 3),
])
