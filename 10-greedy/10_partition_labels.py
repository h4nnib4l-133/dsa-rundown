import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Partition Labels (LC #763) -- Medium
# Max partitions so each letter appears in at most one part.
#
#   Key: Record last occurrence of each char. Extend partition end to `max(end, last[char])`. When i reaches end, cut.

def partition_labels(s):
    pass


run_tests(partition_labels, [
    (("ababcbacadefegdehijhklij",), [9,7,8]),
    (("eccbbbbdec",),                [10]),
])
