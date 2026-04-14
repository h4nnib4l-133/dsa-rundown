#include "../test_runner.h"

/* ---- WRITE YOUR SOLUTION HERE ---- */

int search(int* nums, int n, int target) {
    return -1;
}

/* ---- END SOLUTION ---- */

int main() {
    TEST_INT("mid element",      search(ARR(1,2,3,4,5), 5, 3),       2);
    TEST_INT("first element",    search(ARR(1,2,3,4,5), 5, 1),       0);
    TEST_INT("last element",     search(ARR(1,2,3,4,5), 5, 5),       4);
    TEST_INT("not found",        search(ARR(1,2,3,4,5), 5, 6),      -1);
    TEST_INT("with negatives",   search(ARR(-1,0,3,5,9,12), 6, 9),   4);
    TEST_INT("single found",     search(ARR(5), 1, 5),                0);
    TEST_INT("single not found", search(ARR(5), 1, 3),               -1);
    TEST_SUMMARY();
}
