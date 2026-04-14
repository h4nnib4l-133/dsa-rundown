#include "../test_runner.h"

int find_min_arrow_shots(int points[][2], int n) {
    return -1;
}

int main() {
    int p1[][2] = {{10,16},{2,8},{1,6},{7,12}};
    TEST_INT("overlapping", find_min_arrow_shots(p1, 4), 2);
    int p2[][2] = {{1,2},{3,4},{5,6},{7,8}};
    TEST_INT("disjoint",    find_min_arrow_shots(p2, 4), 4);
    int p3[][2] = {{1,2},{2,3},{3,4},{4,5}};
    TEST_INT("touching",    find_min_arrow_shots(p3, 4), 2);
    TEST_SUMMARY();
}
