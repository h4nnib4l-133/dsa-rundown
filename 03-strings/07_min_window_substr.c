#include "../test_runner.h"

void min_window(char* s, char* t, char* out) {
    out[0] = '\0';
}

int main() {
    char out[256];
    min_window("ADOBECODEBANC", "ABC", out); TEST_STR("basic",     out, "BANC");
    min_window("a", "a", out);               TEST_STR("single",    out, "a");
    min_window("a", "aa", out);              TEST_STR("impossible", out, "");
    TEST_SUMMARY();
}
