#include "../test_runner.h"

int unique_paths(int m, int n) {
    return -1;
}

int main() {
    TEST_INT("3x7", unique_paths(3, 7), 28);
    TEST_INT("3x2", unique_paths(3, 2),  3);
    TEST_INT("1x1", unique_paths(1, 1),  1);
    TEST_INT("7x3", unique_paths(7, 3), 28);
    TEST_INT("3x3", unique_paths(3, 3),  6);
    TEST_SUMMARY();
}
