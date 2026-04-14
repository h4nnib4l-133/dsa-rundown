#include "../test_runner.h"

bool word_break(char* s, char** dict, int dict_size) {
    return false;
}

int main() {
    char* d1[] = {"leet","code"};
    TEST_BOOL("leetcode",   word_break("leetcode", d1, 2), true);
    char* d2[] = {"apple","pen"};
    TEST_BOOL("applepenapple", word_break("applepenapple", d2, 2), true);
    char* d3[] = {"cats","dog","sand","and","cat"};
    TEST_BOOL("catsandog",  word_break("catsandog", d3, 5), false);
    TEST_SUMMARY();
}
