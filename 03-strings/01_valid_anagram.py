# ============================================================
# PATTERN: STRINGS
# ============================================================
# 1. **Frequency counting** -- use hash map / array[26] to count character occurrences
# 2. **Two pointers** -- palindrome check, reverse, compare from both ends
# 3. **Sliding window** -- fixed or variable window for substring problems
# 4. **Hashing/sorting as key** -- group strings by canonical form
#
# **C tips:** Strings are `char[]` with null terminator. Use `strlen()`, `strcmp()`, `strncpy()`. Be careful with buffer sizes.
#
# ---
# ============================================================

import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Valid Anagram (LC #242) -- Easy
# Given two strings s and t, return True if t is an anagram of s.
# Anagram = same characters, same frequency, different order.
#
# Example:
#   "anagram", "nagaram" -> True  (both have a:3, n:1, g:1, r:1, m:1)
#   "rat", "car"         -> False (different chars)
#
#   Key: Count character frequencies. Both must match.
#        Use array[26] or Counter/dict.

def is_anagram(s, t):
    pass


run_tests(is_anagram, [
    (("anagram", "nagaram"), True),
    (("rat", "car"),         False),
    (("a", "a"),             True),
    (("ab", "a"),            False),    # different lengths
    (("", ""),               True),     # both empty
    (("ab", "ba"),           True),     # simple swap
    (("aacc", "ccac"),       False),    # same chars, different freq
    (("listen", "silent"),   True),     # classic anagram
])
