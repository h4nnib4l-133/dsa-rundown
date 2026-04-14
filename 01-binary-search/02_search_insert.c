#include "../test_runner.h"

int search_insert(int* nums, int n, int target) {
    return -1;
}

int main() {
    TEST_INT("exists",       search_insert(ARR(1,3,5,6), 4, 5), 2);
    TEST_INT("insert mid",   search_insert(ARR(1,3,5,6), 4, 2), 1);
    TEST_INT("insert end",   search_insert(ARR(1,3,5,6), 4, 7), 4);
    TEST_INT("insert start", search_insert(ARR(1,3,5,6), 4, 0), 0);
    TEST_INT("single before",search_insert(ARR(1), 1, 0),       0);
    TEST_INT("single after", search_insert(ARR(1), 1, 2),       1);
    TEST_SUMMARY();
}
