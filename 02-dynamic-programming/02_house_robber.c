#include "../test_runner.h"

int rob(int* nums, int n) {
    return -1;
}

int main() {
    TEST_INT("basic",     rob(ARR(1,2,3,1), 4),    4);
    TEST_INT("larger",    rob(ARR(2,7,9,3,1), 5), 12);
    TEST_INT("symmetric", rob(ARR(2,1,1,2), 4),    4);
    TEST_INT("single",    rob(ARR(100), 1),       100);
    TEST_SUMMARY();
}
