import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Accounts Merge (LC #721) -- Medium
# Input:  accounts: List[[name, *emails]]
# Output: List[[name, *sorted_emails]] (merged accounts)
# Two accounts are same person if they share any email.
# Merge them. Output emails sorted alphabetically.
#
# Example:
# #   [["John","a@x.com","b@x.com"],
#    ["John","c@x.com"],
#    ["John","b@x.com","d@x.com"]]
#   -> [["John","a@x.com","b@x.com","d@x.com"], ["John","c@x.com"]]
#
#   Key: Union-Find over emails. Union all emails within same account.
#        Group emails by root. Lookup name from any original account.

def accounts_merge(accounts):
    pass


def solve(accounts):
    result = accounts_merge(accounts)
    # normalize: sort each entry's emails, sort by first email
    normalized = [[acc[0]] + sorted(acc[1:]) for acc in result]
    return sorted(normalized, key=lambda x: (x[0], x[1] if len(x) > 1 else ''))

run_tests(accounts_merge, [
    (([["John","a@x.com","b@x.com"],["John","c@x.com"],["John","b@x.com","d@x.com"]],),
     [["John","a@x.com","b@x.com","d@x.com"],["John","c@x.com"]]),
    (([["Alex","a@x.com"]],),
     [["Alex","a@x.com"]]),
])
