#include "../test_runner.h"

bool can_finish(int n, int prereqs[][2], int num_prereqs) {
    return false;
}

int main() {
    int p1[][2] = {{1,0}};
    TEST_BOOL("no cycle",   can_finish(2, p1, 1), true);
    int p2[][2] = {{1,0},{0,1}};
    TEST_BOOL("has cycle",  can_finish(2, p2, 2), false);
    int p3[][2] = {{1,0},{2,1}};
    TEST_BOOL("chain",      can_finish(3, p3, 2), true);
    TEST_SUMMARY();
}
