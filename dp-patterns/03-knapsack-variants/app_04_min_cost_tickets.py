import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Minimum Cost For Tickets (LC #983) -- Medium
# Input:  days: List[int] (travel days), costs: List[int] (1-day, 7-day, 30-day pass costs)
# Output: int (min total cost)
# Travel on specific days. Choose between buying 1/7/30-day passes.
#
# Example:
# #   days=[1,4,6,7,8,20], costs=[2,7,15] -> 11
#     (7-day pass on day 1 covers days 1-7; 1-day pass on day 20. 7+2*2=11)
#
#   Pattern: DP ON DAYS
#   Key: dp[day] = min cost to cover up to day.
#        If day is travel: dp[day] = min(dp[day-1]+cost1, dp[day-7]+cost7, dp[day-30]+cost30).
#        Else dp[day] = dp[day-1].

def mincost_tickets(days, costs):
    pass

run_tests(mincost_tickets, [
    (([1,4,6,7,8,20], [2,7,15]),                 11),
    (([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]),   17),
    (([1], [2,7,15]),                              2),
    (([1,2,3], [10,15,20]),                       15),     # 7-day pass
])
