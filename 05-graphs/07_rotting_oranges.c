#include "../test_runner.h"

int oranges_rotting(int grid[][3], int rows, int cols) {
    return -1;
}

int main() {
    int g1[][3] = {{2,1,1},{1,1,0},{0,1,1}};
    TEST_INT("basic",      oranges_rotting(g1, 3, 3),  4);
    int g2[][3] = {{2,1,1},{0,1,1},{1,0,1}};
    TEST_INT("impossible", oranges_rotting(g2, 3, 3), -1);
    TEST_SUMMARY();
}
