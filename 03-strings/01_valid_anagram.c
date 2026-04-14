#include "../test_runner.h"

bool is_anagram(char* s, char* t) {
    return false;
}

int main() {
    TEST_BOOL("anagram",  is_anagram("anagram","nagaram"), true);
    TEST_BOOL("not",      is_anagram("rat","car"),         false);
    TEST_BOOL("single",   is_anagram("a","a"),             true);
    TEST_BOOL("diff len", is_anagram("ab","a"),            false);
    TEST_BOOL("empty",    is_anagram("",""),               true);
    TEST_SUMMARY();
}
