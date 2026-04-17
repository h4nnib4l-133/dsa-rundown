import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Find All Recipes You Can Make (LC #2115) -- Medium
# Input:  recipes: List[str], ingredients: List[List[str]], supplies: List[str]
# Output: List[str] (recipes you can make, given supplies and recursive ingredient lookup)
# A recipe can be made if all its ingredients are either in supplies or are
# other recipes that can themselves be made.
#
# Example:
# #   recipes=["bread"], ingredients=[["yeast","flour"]], supplies=["yeast","flour","corn"]
#   -> ["bread"]
#
#   recipes=["bread","sandwich"], ingredients=[["yeast","flour"],["bread","meat"]], supplies=["yeast","flour","meat"]
#   -> ["bread","sandwich"]
#
#   WHY THIS IS A TOPOLOGICAL SORT:
#   Ingredients -> recipes form a DAG. Start with supplies as 'ready'.
#   Topologically process: when all of a recipe's ingredients are ready, recipe is ready.
#
#   Key: Edge from ingredient -> recipe. Indegree = len(ingredients[i]).
#        Start queue with supplies. BFS: when all ingredients satisfied, mark recipe ready.

def find_all_recipes(recipes, ingredients, supplies):
    pass


def solve(recipes, ingredients, supplies):
    return sorted(find_all_recipes(recipes, ingredients, supplies))

run_tests(solve, [
    ((["bread"], [["yeast","flour"]], ["yeast","flour","corn"]),
     ["bread"]),
    ((["bread","sandwich"], [["yeast","flour"],["bread","meat"]], ["yeast","flour","meat"]),
     ["bread","sandwich"]),
    ((["bread"], [["yeast","flour"]], ["yeast"]),
     []),
])
