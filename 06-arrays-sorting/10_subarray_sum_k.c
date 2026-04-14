#include "../test_runner.h"

int subarray_sum(int* nums, int n, int k) {
    return -1;
}

int main() {
    TEST_INT("basic",     subarray_sum(ARR(1,1,1), 3, 2), 2);
    TEST_INT("mixed",     subarray_sum(ARR(1,2,3), 3, 3), 2);
    TEST_INT("with neg",  subarray_sum(ARR(1,-1,0), 3, 0),3);
    TEST_SUMMARY();
}
