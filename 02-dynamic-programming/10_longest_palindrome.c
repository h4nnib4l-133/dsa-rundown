#include "../test_runner.h"

/* Write result into out buffer */
void longest_palindrome(char* s, char* out) {
    out[0] = '\0';
}

int main() {
    char out[256];
    longest_palindrome("babad", out);
    int len1 = strlen(out);
    TEST_BOOL("babad len>=3", len1 >= 3, true);

    longest_palindrome("cbbd", out);
    int len2 = strlen(out);
    TEST_BOOL("cbbd len>=2", len2 >= 2, true);

    longest_palindrome("a", out);
    TEST_STR("single char", out, "a");

    longest_palindrome("racecar", out);
    TEST_STR("full palindrome", out, "racecar");

    TEST_SUMMARY();
}
