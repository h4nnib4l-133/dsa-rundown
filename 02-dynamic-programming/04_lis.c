#include "../test_runner.h"

int length_of_lis(int* nums, int n) {
    return -1;
}

int main() {
    TEST_INT("basic",      length_of_lis(ARR(10,9,2,5,3,7,101,18), 8), 4);
    TEST_INT("with dups",  length_of_lis(ARR(0,1,0,3,2,3), 6),         4);
    TEST_INT("all same",   length_of_lis(ARR(7,7,7,7,7), 5),           1);
    TEST_INT("sorted",     length_of_lis(ARR(1,2,3,4,5), 5),           5);
    TEST_INT("single",     length_of_lis(ARR(1), 1),                    1);
    TEST_SUMMARY();
}
