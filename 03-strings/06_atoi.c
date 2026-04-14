#include "../test_runner.h"
#include <limits.h>
#include <ctype.h>

int my_atoi(char* s) {
    return 0;
}

int main() {
    TEST_INT("basic",      my_atoi("42"),             42);
    TEST_INT("negative",   my_atoi("   -42"),        -42);
    TEST_INT("with words", my_atoi("4193 with words"),4193);
    TEST_INT("no digits",  my_atoi("words and 987"),  0);
    TEST_INT("overflow",   my_atoi("-91283472332"),   INT_MIN);
    TEST_SUMMARY();
}
