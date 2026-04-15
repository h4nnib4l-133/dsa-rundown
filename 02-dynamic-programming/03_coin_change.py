import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Coin Change (LC #322) -- Medium
# Given coin denominations and an amount, find fewest coins to make that amount.
# Unlimited supply of each coin. Return -1 if impossible.
#
# Example:
#   coins = [1,5,10,25], amount = 30 -> 2  (25 + 5)
#   coins = [1,2,5], amount = 11     -> 3  (5 + 5 + 1)
#   coins = [2], amount = 3          -> -1 (impossible, 2 can't make odd)
#   coins = [1], amount = 0          -> 0  (no coins needed)
#
#   Key: dp[a] = min coins to make amount a.
#        dp[a] = min(dp[a-coin] + 1) for each coin.
#        Init dp[0]=0, rest=infinity.

def coin_change(coins, amount):
    """Return min coins needed, or -1 if impossible"""
    pass


run_tests(coin_change, [
    (([1,5,10,25], 30),    2),     # 25+5
    (([1,2,5], 11),        3),     # 5+5+1
    (([2], 3),            -1),     # impossible (odd amount, even coin)
    (([1], 0),             0),     # zero amount
    (([1,2,5], 100),      20),     # 20 x 5
    (([1], 1),             1),     # single coin, single amount
    (([1], 7),             7),     # only pennies
    (([3,7], 11),         -1),     # can't make 11 from 3s and 7s... wait 7+3+? no. -1? Let me check. 3+3+3=9, 7+3=10, 7+7=14. Yes -1.
    (([186,419,83,408], 6249), 20),  # stress case
    (([2], 0),             0),     # zero amount, any coins
])
