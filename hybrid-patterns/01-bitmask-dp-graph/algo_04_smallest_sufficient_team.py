import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Smallest Sufficient Team (LC #1125) -- Hard
# Input:  req_skills: List[str], people: List[List[str]]
# Output: List[int] (indices of people forming smallest team covering all skills)
# Pick MIN team where union of skills covers req_skills.
#
# Example:
# #   skills=["java","nodejs","reactjs"]
#   people=[["java"],["nodejs"],["nodejs","reactjs"]]  -> [0,2]
#
#   Pattern: BITMASK DP (set cover)
#   Key: Skills -> bitmask index. Person -> skill bitmask.
#        dp[mask] = min team covering skills in mask.
#        For each person, try adding them. Track picked people.

def smallest_sufficient_team(req_skills, people):
    pass


def solve(req_skills, people):
    team = smallest_sufficient_team(req_skills, people)
    # validate: team covers all skills and is minimum
    covered = set()
    for i in team:
        covered.update(people[i])
    return covered.issuperset(set(req_skills))

run_tests(smallest_sufficient_team, [
    ((["java","nodejs","reactjs"], [["java"],["nodejs"],["nodejs","reactjs"]]),  True),
    ((["algorithms","math","java","reactjs","csharp","aws"],
      [["algorithms","math","java"],["algorithms","math","reactjs"],
       ["java","csharp","aws"],["reactjs","csharp"],
       ["csharp","math"],["aws","java"]]),  True),
])
