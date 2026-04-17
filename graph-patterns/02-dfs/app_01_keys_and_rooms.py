import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Keys and Rooms (LC #841) -- Medium
# Input:  rooms: List[List[int]] (rooms[i] = keys available in room i)
# Output: bool (True if you can visit all rooms starting from room 0)
# Room 0 is unlocked initially. Each room contains keys to other rooms.
# Can you visit every room?
#
# Example:
# #   [[1],[2],[3],[]]        -> True   (0->1->2->3)
#   [[1,3],[3,0,1],[2],[0]]  -> False (room 2 never accessed)
#
#   WHY THIS IS A DFS REACHABILITY:
#   Classic graph reachability. Nodes = rooms, edges = keys. 
#   Question is: is room 0's connected component the entire graph?
#
#   Key: DFS from room 0. Collect visited rooms. True iff visited.size == len(rooms).

def can_visit_all_rooms(rooms):
    pass

run_tests(can_visit_all_rooms, [
    (([[1],[2],[3],[]],),              True),
    (([[1,3],[3,0,1],[2],[0]],),       False),
    (([[]],),                          True),     # single room
    (([[1],[]],),                      True),
    (([[2],[],[]],),                   False),    # room 1 unreachable
])
