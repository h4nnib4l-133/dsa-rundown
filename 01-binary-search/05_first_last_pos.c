#include "../test_runner.h"

/* Return via out[0] = first, out[1] = last. Set to -1 if not found */
void search_range(int* nums, int n, int target, int* out) {
    out[0] = -1; out[1] = -1;
}

int main() {
    int r[2];
    search_range(ARR(5,7,7,8,8,10), 6, 8, r); TEST_ARR("found pair",   r, ARR(3,4),   2);
    search_range(ARR(5,7,7,8,8,10), 6, 6, r); TEST_ARR("not found",    r, ARR(-1,-1), 2);
    search_range(NULL, 0, 0, r);               TEST_ARR("empty",        r, ARR(-1,-1), 2);
    search_range(ARR(1), 1, 1, r);             TEST_ARR("single",       r, ARR(0,0),   2);
    search_range(ARR(2,2), 2, 2, r);           TEST_ARR("all same",     r, ARR(0,1),   2);
    TEST_SUMMARY();
}
