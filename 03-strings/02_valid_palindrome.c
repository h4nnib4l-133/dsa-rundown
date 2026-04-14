#include "../test_runner.h"
#include <ctype.h>

bool is_palindrome(char* s) {
    return false;
}

int main() {
    TEST_BOOL("panama",   is_palindrome("A man, a plan, a canal: Panama"), true);
    TEST_BOOL("racecar",  is_palindrome("race a car"),                     false);
    TEST_BOOL("space",    is_palindrome(" "),                              true);
    TEST_BOOL("single",   is_palindrome("a"),                              true);
    TEST_SUMMARY();
}
