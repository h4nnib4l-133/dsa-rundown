#include "../test_runner.h"

bool is_match(char* s, char* p) {
    return false;
}

int main() {
    TEST_BOOL("aa vs a",    is_match("aa", "a"),      false);
    TEST_BOOL("aa vs a*",   is_match("aa", "a*"),     true);
    TEST_BOOL("ab vs .*",   is_match("ab", ".*"),     true);
    TEST_BOOL("aab vs c*a*b", is_match("aab","c*a*b"),true);
    TEST_SUMMARY();
}
