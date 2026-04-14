#include "../test_runner.h"

int search_rotated(int* nums, int n, int target) {
    return -1;
}

int main() {
    TEST_INT("right half",   search_rotated(ARR(4,5,6,7,0,1,2), 7, 0),  4);
    TEST_INT("left half",    search_rotated(ARR(4,5,6,7,0,1,2), 7, 5),  1);
    TEST_INT("not found",    search_rotated(ARR(4,5,6,7,0,1,2), 7, 3), -1);
    TEST_INT("single miss",  search_rotated(ARR(1), 1, 0),             -1);
    TEST_INT("single hit",   search_rotated(ARR(1), 1, 1),              0);
    TEST_INT("two elements", search_rotated(ARR(3,1), 2, 1),            1);
    TEST_SUMMARY();
}
