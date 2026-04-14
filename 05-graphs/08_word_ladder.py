import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def ladder_length(begin_word, end_word, word_list):
    """Return length of shortest transformation, 0 if impossible"""
    pass


run_tests(ladder_length, [
    (("hit", "cog", ["hot","dot","dog","lot","log","cog"]),  5),
    (("hit", "cog", ["hot","dot","dog","lot","log"]),        0),
])
