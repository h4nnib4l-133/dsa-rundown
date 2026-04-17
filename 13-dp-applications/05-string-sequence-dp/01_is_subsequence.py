import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Number of Matching Subsequences (LC #792) -- Medium
# Input:  s: str, words: List[str]
# Output: int (count of words that are subsequences of s)
# For each word, check if it's a subsequence of s. Count matches.
#
# Naive: O(|s| * sum_word_lengths). Better: process all words in parallel.
#
# Example:
# #   s="abcde", words=["a","bb","acd","ace"]  -> 3   (a, acd, ace)
#
#   WHY THIS IS A STRING SEQUENCE PROCESSING:
#   For each char in s, advance all words waiting on that char simultaneously.
#   Bucket approach: map next-needed-char -> list of (word, progress).
#
#   Key: For each word, put it in bucket[word[0]].
#        For each char in s: pop all words waiting on this char, advance each.
#        Re-bucket them under next needed char. Count finished words.

def num_matching_subseq(s, words):
    pass

run_tests(num_matching_subseq, [
    (("abcde", ["a","bb","acd","ace"]),                    3),
    (("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]),  2),
    (("abc", []),                                            0),
    (("abc", ["a","b","c","abc","ab","bc","ac"]),           7),
])
