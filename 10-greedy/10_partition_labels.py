import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def partition_labels(s):
    pass


run_tests(partition_labels, [
    (("ababcbacadefegdehijhklij",), [9,7,8]),
    (("eccbbbbdec",),                [10]),
])
