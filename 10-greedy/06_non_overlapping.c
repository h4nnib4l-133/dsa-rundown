#include "../test_runner.h"

int erase_overlap_intervals(int intervals[][2], int n) {
    return -1;
}

int main() {
    int i1[][2] = {{1,2},{2,3},{3,4},{1,3}};
    TEST_INT("one remove", erase_overlap_intervals(i1, 4), 1);
    int i2[][2] = {{1,2},{1,2},{1,2}};
    TEST_INT("two remove", erase_overlap_intervals(i2, 3), 2);
    int i3[][2] = {{1,2},{2,3}};
    TEST_INT("no remove",  erase_overlap_intervals(i3, 2), 0);
    TEST_SUMMARY();
}
