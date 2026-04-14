#include "../test_runner.h"

/* Returns count of merged intervals, modifies intervals in-place */
int merge_intervals(int intervals[][2], int n) {
    return -1;
}

int main() {
    int iv1[][2] = {{1,3},{2,6},{8,10},{15,18}};
    int cnt = merge_intervals(iv1, 4);
    TEST_INT("count", cnt, 3);
    TEST_ARR("first", iv1[0], ARR(1,6), 2);
    TEST_SUMMARY();
}
