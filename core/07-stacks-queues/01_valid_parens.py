# ============================================================
# PATTERN: STACKS QUEUES
# ============================================================
# 1. **Matching/balancing** -- brackets, parentheses validation
# 2. **Monotonic stack** -- next greater/smaller element, histogram
# 3. **Stack as evaluator** -- postfix expressions, calculators
# 4. **Deque** -- sliding window max/min (monotonic deque)
# 5. **Simulate one with another** -- queue using stacks, stack using queues
#
# **C tips:** Implement stack with array + top index. Queue with circular buffer or two stacks.
#
# ---
# ============================================================

import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Valid Parentheses (LC #20) -- Easy
# Input:  s: str (only contains '(', ')', '{', '}', '[', ']')
# Output: bool (True if brackets are balanced and properly nested)
# Given string of '(', ')', '{', '}', '[', ']', check if it's balanced.
# Every open bracket must be closed by same type in correct order.
#
# Example:
#   "()"       -> True
#   "()[]{}"   -> True
#   "(]"       -> False
#   "([)]"     -> False  (interleaved, not nested)
#   "{[]}"     -> True   (nested)
#
#   Key: Stack. Push opening brackets.
#        On closing bracket, pop and check if it matches.

def is_valid(s):
    pass


run_tests(is_valid, [
    (("()",),       True),
    (("()[]{}",),   True),
    (("(]",),       False),
    (("([)]",),     False),     # interleaved
    (("{[]}",),     True),      # nested
    (("",),         True),      # empty string
    (("(",),        False),     # unclosed
    ((")",),        False),     # no opener
    (("(((())))",), True),      # deeply nested
    (("{{{}}}[]",), True),      # mixed nested
    (("[",),        False),     # single open bracket
])
