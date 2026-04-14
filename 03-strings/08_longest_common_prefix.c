#include "../test_runner.h"

void longest_common_prefix(char** strs, int n, char* out) {
    out[0] = '\0';
}

int main() {
    char out[256];
    char* s1[] = {"flower","flow","flight"};
    longest_common_prefix(s1, 3, out); TEST_STR("fl", out, "fl");
    char* s2[] = {"dog","racecar","car"};
    longest_common_prefix(s2, 3, out); TEST_STR("none", out, "");
    TEST_SUMMARY();
}
