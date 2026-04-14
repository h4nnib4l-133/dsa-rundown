#include "../test_runner.h"

int find_peak(int* nums, int n) {
    return -1;
}

int main() {
    int i;
    /* We check the result is a valid peak */
    i = find_peak(ARR(1,2,3,1), 4);
    TEST_BOOL("peak in [1,2,3,1]", (i>=0 && i<4 && (i==0||((int[]){1,2,3,1})[i]>((int[]){1,2,3,1})[i-1]) && (i==3||((int[]){1,2,3,1})[i]>((int[]){1,2,3,1})[i+1])), true);

    i = find_peak(ARR(1), 1);
    TEST_INT("single element", i, 0);

    i = find_peak(ARR(1,2), 2);
    TEST_BOOL("two elements", i == 0 || i == 1, true);

    TEST_SUMMARY();
}
