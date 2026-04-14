#include "../test_runner.h"

void max_sliding_window(int* nums, int n, int k, int* out, int* out_len) {
    *out_len = 0;
}

int main() {
    int out[10], len;
    max_sliding_window(ARR(1,3,-1,-3,5,3,6,7), 8, 3, out, &len);
    TEST_ARR("basic", out, ARR(3,3,5,5,6,7), 6);
    max_sliding_window(ARR(1), 1, 1, out, &len);
    TEST_ARR("single", out, ARR(1), 1);
    TEST_SUMMARY();
}
