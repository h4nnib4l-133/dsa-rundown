#include "../test_runner.h"

/* Write result into out[0], out[1] */
void two_sum(int* nums, int n, int target, int* out) {
    out[0] = -1; out[1] = -1;
}

int main() {
    int r[2];
    two_sum(ARR(2,7,11,15), 4, 9, r); TEST_ARR("basic",  r, ARR(0,1), 2);
    two_sum(ARR(3,2,4), 3, 6, r);     TEST_ARR("mid",    r, ARR(1,2), 2);
    two_sum(ARR(3,3), 2, 6, r);       TEST_ARR("dupes",  r, ARR(0,1), 2);
    TEST_SUMMARY();
}
