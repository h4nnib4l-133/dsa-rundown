# String Manipulation

## The Patterns

1. **Frequency counting** -- use hash map / array[26] to count character occurrences
2. **Two pointers** -- palindrome check, reverse, compare from both ends
3. **Sliding window** -- fixed or variable window for substring problems
4. **Hashing/sorting as key** -- group strings by canonical form

**C tips:** Strings are `char[]` with null terminator. Use `strlen()`, `strcmp()`, `strncpy()`. Be careful with buffer sizes.

---

## Problems

### 1. Valid Anagram (LC #242) -- Easy
Check if two strings are anagrams.
- **Key:** Frequency count array[26]. Both must match.
- **Files:** `01_valid_anagram.py`, `01_valid_anagram.c`

### 2. Valid Palindrome (LC #125) -- Easy
Check palindrome considering only alphanumeric chars, case-insensitive.
- **Key:** Two pointers from both ends, skip non-alphanumeric
- **Files:** `02_valid_palindrome.py`, `02_valid_palindrome.c`

### 3. Longest Substring Without Repeating Characters (LC #3) -- Medium
Find length of longest substring with all unique characters.
- **Key:** Sliding window + hashset. Move left pointer when duplicate found.
- **Files:** `03_longest_unique_substr.py`, `03_longest_unique_substr.c`

### 4. Group Anagrams (LC #49) -- Medium
Group strings that are anagrams of each other.
- **Key:** Sort each string as key, or use frequency tuple as key
- **Files:** `04_group_anagrams.py`, `04_group_anagrams.c`

### 5. Longest Palindromic Substring (LC #5) -- Medium
Find the longest palindromic substring.
- **Key:** Expand around each center (handle odd and even length)
- **Files:** `05_longest_palindrome_substr.py`, `05_longest_palindrome_substr.c`

### 6. String to Integer - atoi (LC #8) -- Medium
Implement atoi with whitespace, sign, overflow handling.
- **Key:** State machine or step-by-step parsing. Clamp to INT_MIN/INT_MAX.
- **Files:** `06_atoi.py`, `06_atoi.c`

### 7. Minimum Window Substring (LC #76) -- Hard
Find smallest window in s containing all characters of t.
- **Key:** Sliding window + two frequency maps. Expand right, shrink left.
- **Hint:** Track `have` vs `need` count to know when window is valid
- **Files:** `07_min_window_substr.py`, `07_min_window_substr.c`

### 8. Longest Common Prefix (LC #14) -- Easy
Find longest common prefix among array of strings.
- **Key:** Vertical scanning -- compare char by char across all strings
- **Files:** `08_longest_common_prefix.py`, `08_longest_common_prefix.c`

### 9. Alternating Characters (HackerRank) -- Easy
Count deletions to make no two adjacent characters the same.
- **Key:** Count consecutive duplicates
- **Files:** `09_alternating_chars.py`, `09_alternating_chars.c`

### 10. Regular Expression Matching (LC #10) -- Hard
Implement regex with `.` and `*` support.
- **Key:** DP. `dp[i][j]` = does s[0..i] match p[0..j]? Handle `*` by zero or more matches.
- **Files:** `10_regex_matching.py`, `10_regex_matching.c`
