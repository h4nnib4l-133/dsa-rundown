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
# Check if two strings are anagrams.
#
#   Key: Frequency count array[26]. Both must match.

def is_anagram(s, t):
    pass


run_tests(is_anagram, [
    (("anagram", "nagaram"), True),
    (("rat", "car"),         False),
    (("a", "a"),             True),
    (("ab", "a"),            False),
    (("", ""),               True),
])
