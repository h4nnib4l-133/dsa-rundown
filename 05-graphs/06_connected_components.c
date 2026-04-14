#include "../test_runner.h"

int count_components(int n, int edges[][2], int num_edges) {
    return -1;
}

int main() {
    int e1[][2] = {{0,1},{1,2},{3,4}};
    TEST_INT("2 components", count_components(5, e1, 3), 2);
    int e2[][2] = {{0,1},{1,2},{2,3},{3,4}};
    TEST_INT("1 component",  count_components(5, e2, 4), 1);
    TEST_INT("no edges",     count_components(4, NULL, 0), 4);
    TEST_SUMMARY();
}
