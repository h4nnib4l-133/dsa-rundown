#include "../test_runner.h"

bool is_balanced(char* s) {
    return false;
}

int main() {
    TEST_BOOL("valid",    is_balanced("{[()]}"),       true);
    TEST_BOOL("invalid",  is_balanced("{[(])}"),       false);
    TEST_BOOL("nested",   is_balanced("{{[[(())]]}}"), true);
    TEST_BOOL("empty",    is_balanced(""),             true);
    TEST_BOOL("single",   is_balanced("{"),            false);
    TEST_SUMMARY();
}
