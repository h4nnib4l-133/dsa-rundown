#include "../test_runner.h"

bool can_jump(int* nums, int n) {
    return false;
}

int main() {
    TEST_BOOL("reachable",   can_jump(ARR(2,3,1,1,4), 5), true);
    TEST_BOOL("unreachable", can_jump(ARR(3,2,1,0,4), 5), false);
    TEST_BOOL("single",      can_jump(ARR(0), 1),         true);
    TEST_SUMMARY();
}
