#include "../test_runner.h"

int num_islands(char grid[][5], int rows, int cols) {
    return -1;
}

int main() {
    char g1[][5] = {
        {'1','1','1','1','0'},
        {'1','1','0','1','0'},
        {'1','1','0','0','0'},
        {'0','0','0','0','0'}
    };
    TEST_INT("one island", num_islands(g1, 4, 5), 1);

    char g2[][5] = {
        {'1','1','0','0','0'},
        {'1','1','0','0','0'},
        {'0','0','1','0','0'},
        {'0','0','0','1','1'}
    };
    TEST_INT("three islands", num_islands(g2, 4, 5), 3);
    TEST_SUMMARY();
}
