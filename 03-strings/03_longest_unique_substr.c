#include "../test_runner.h"

int length_of_longest_substring(char* s) {
    return -1;
}

int main() {
    TEST_INT("abcabcbb", length_of_longest_substring("abcabcbb"), 3);
    TEST_INT("bbbbb",    length_of_longest_substring("bbbbb"),    1);
    TEST_INT("pwwkew",   length_of_longest_substring("pwwkew"),   3);
    TEST_INT("empty",    length_of_longest_substring(""),         0);
    TEST_INT("dvdf",     length_of_longest_substring("dvdf"),     3);
    TEST_SUMMARY();
}
