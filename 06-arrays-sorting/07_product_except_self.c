#include "../test_runner.h"

void product_except_self(int* nums, int n, int* out) {
    /* your code */
}

int main() {
    int out[10];
    product_except_self(ARR(1,2,3,4), 4, out);
    TEST_ARR("basic", out, ARR(24,12,8,6), 4);
    product_except_self(ARR(2,3), 2, out);
    TEST_ARR("two", out, ARR(3,2), 2);
    TEST_SUMMARY();
}
