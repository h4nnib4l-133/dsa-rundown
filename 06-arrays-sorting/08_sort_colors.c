#include "../test_runner.h"

void sort_colors(int* nums, int n) {
    /* your code */
}

int main() {
    int a1[] = {2,0,2,1,1,0};
    sort_colors(a1, 6);
    TEST_ARR("basic", a1, ARR(0,0,1,1,2,2), 6);

    int a2[] = {2,0,1};
    sort_colors(a2, 3);
    TEST_ARR("small", a2, ARR(0,1,2), 3);
    TEST_SUMMARY();
}
