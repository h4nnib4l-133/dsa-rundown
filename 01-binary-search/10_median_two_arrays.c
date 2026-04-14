#include "../test_runner.h"

double find_median(int* nums1, int n1, int* nums2, int n2) {
    return 0.0;
}

int main() {
    TEST_FLOAT("odd total",  find_median(ARR(1,3), 2, ARR(2), 1),   2.0, 0.001);
    TEST_FLOAT("even total", find_median(ARR(1,2), 2, ARR(3,4), 2), 2.5, 0.001);
    TEST_FLOAT("all zeros",  find_median(ARR(0,0), 2, ARR(0,0), 2), 0.0, 0.001);
    TEST_FLOAT("one empty",  find_median(NULL, 0, ARR(1), 1),       1.0, 0.001);
    TEST_SUMMARY();
}
