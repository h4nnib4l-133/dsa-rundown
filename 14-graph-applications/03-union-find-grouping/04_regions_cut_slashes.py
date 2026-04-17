import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Regions Cut by Slashes (LC #959) -- Medium
# Input:  grid: List[str] (each char is ' ', '/', or '\\')
# Output: int (number of regions formed)
# n x n grid where each cell has a slash shape. Count regions.
#
# Trick: subdivide each cell into 4 triangles (top, right, bottom, left).
# Union them based on slash type. Count final components.
#
# Example:
# #   [" /",
#    "/ "]    -> 2   (two regions: upper-left and lower-right)
#
#   WHY THIS IS A UNION-FIND (clever state expansion):
#   Trick: model each cell as 4 sub-regions. No slash = union all 4.
#   '/' = union top+left and bottom+right. '\\' = union top+right and bottom+left.
#   Then union adjacent cells' matching triangles.
#
#   Key: 4 triangles per cell: top=0, right=1, bottom=2, left=3.
#        Union within cell based on char. Union with neighbors:
#        bottom of (r,c) with top of (r+1,c); right of (r,c) with left of (r,c+1).

def regions_by_slashes(grid):
    pass

run_tests(regions_by_slashes, [
    (([" /","/ "],),       2),
    (([" /","  "],),       1),
    (([" /","/\\"],),      4),
    ((["/\\","\\/"],),     5),
    ((["//","/ "],),       3),
])
