#include "../test_runner.h"

void longest_palindrome(char* s, char* out) {
    out[0] = '\0';
}

int main() {
    char out[256];
    longest_palindrome("racecar", out);
    TEST_STR("full", out, "racecar");
    longest_palindrome("a", out);
    TEST_STR("single", out, "a");
    TEST_SUMMARY();
}
