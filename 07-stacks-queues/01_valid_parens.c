#include "../test_runner.h"

bool is_valid(char* s) {
    return false;
}

int main() {
    TEST_BOOL("simple",   is_valid("()"),     true);
    TEST_BOOL("all types",is_valid("()[]{}"), true);
    TEST_BOOL("mismatch", is_valid("(]"),     false);
    TEST_BOOL("interleave",is_valid("([)]"),  false);
    TEST_BOOL("nested",   is_valid("{[]}"),   true);
    TEST_BOOL("empty",    is_valid(""),       true);
    TEST_SUMMARY();
}
