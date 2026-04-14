#include "../test_runner.h"

int jump(int* nums, int n) {
    return -1;
}

int main() {
    TEST_INT("basic",  jump(ARR(2,3,1,1,4), 5), 2);
    TEST_INT("alt",    jump(ARR(2,3,0,1,4), 5), 2);
    TEST_INT("single", jump(ARR(1), 1),          0);
    TEST_SUMMARY();
}
