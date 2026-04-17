import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Accounts Merge (LC #721) -- Medium
# Input:  accounts: List[[name, *emails]]
# Output: List[[name, *sorted_emails]]
# Two accounts are the same person if they share ANY email.
# Merge accounts for the same person.
#
# Example:
# #   See file for full example -- accounts with shared emails merge.
#
#   WHY THIS IS A UNION-FIND (over strings):
#   Emails are nodes. Within each account, union all emails together.
#   After processing, group emails by root. Attach name from any account containing
#   that root email.
#
#   Key: 1. Union all emails within each account.
#        2. Group emails by root. For each group, pick a representative account
#           to get the name. Sort emails within group.

def accounts_merge(accounts):
    pass


def solve(accounts):
    result = accounts_merge(accounts)
    normalized = [[acc[0]] + sorted(acc[1:]) for acc in result]
    return sorted(normalized, key=lambda x: (x[0], x[1] if len(x) > 1 else ''))

run_tests(solve, [
    (([["John","john1@x.com","john2@x.com"],
       ["John","john3@x.com"],
       ["John","john2@x.com","john4@x.com"]],),
     [["John","john1@x.com","john2@x.com","john4@x.com"],["John","john3@x.com"]]),
    (([["Alex","a@x.com"]],),
     [["Alex","a@x.com"]]),
])
