import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Partition Labels (LC #763) -- Medium
# Partition string into maximum parts so each letter appears in at most one part.
# Return list of part lengths.
#
# Example:
#   "ababcbacadefegdehijhklij"
#   -> [9, 7, 8]
#   Part 1: "ababcbaca" (a,b,c only here)
#   Part 2: "defegde"   (d,e,f,g only here)
#   Part 3: "hijhklij"  (h,i,j,k,l only here)
#
#   Key: Record last occurrence of each char.
#        Scan left to right. Extend partition end to max(end, last[char]).
#        When index reaches end, cut partition.

def partition_labels(s):
    pass


run_tests(partition_labels, [
    (("ababcbacadefegdehijhklij",),  [9,7,8]),
    (("eccbbbbdec",),                 [10]),       # all chars interleaved
    (("abc",),                        [1,1,1]),    # each char unique partition
    (("a",),                          [1]),        # single char
    (("abab",),                       [4]),        # a and b overlap
    (("aabbcc",),                     [2,2,2]),    # each pair separate
])
