#include "../test_runner.h"

int longest_common_subseq(char* t1, char* t2) {
    return -1;
}

int main() {
    TEST_INT("basic",    longest_common_subseq("abcde", "ace"), 3);
    TEST_INT("same",     longest_common_subseq("abc", "abc"),   3);
    TEST_INT("none",     longest_common_subseq("abc", "def"),   0);
    TEST_INT("empty",    longest_common_subseq("", "abc"),      0);
    TEST_SUMMARY();
}
