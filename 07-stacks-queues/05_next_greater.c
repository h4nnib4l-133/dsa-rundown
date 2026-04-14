#include "../test_runner.h"

void next_greater_element(int* nums1, int n1, int* nums2, int n2, int* out) {
    for (int i = 0; i < n1; i++) out[i] = -1;
}

int main() {
    int out[10];
    next_greater_element(ARR(4,1,2), 3, ARR(1,3,4,2), 4, out);
    TEST_ARR("basic", out, ARR(-1,3,-1), 3);
    next_greater_element(ARR(2,4), 2, ARR(1,2,3,4), 4, out);
    TEST_ARR("simple", out, ARR(3,-1), 2);
    TEST_SUMMARY();
}
