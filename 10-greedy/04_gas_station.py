import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def can_complete_circuit(gas, cost):
    pass


run_tests(can_complete_circuit, [
    (([1,2,3,4,5], [3,4,5,1,2]),  3),
    (([2,3,4], [3,4,3]),          -1),
])
