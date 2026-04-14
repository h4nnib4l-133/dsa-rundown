#include "../test_runner.h"

int trap(int* height, int n) {
    return -1;
}

int main() {
    TEST_INT("basic",  trap(ARR(0,1,0,2,1,0,1,3,2,1,2,1), 12), 6);
    TEST_INT("valley", trap(ARR(4,2,0,3,2,5), 6),               9);
    TEST_INT("tiny",   trap(ARR(1,0,1), 3),                      1);
    TEST_SUMMARY();
}
