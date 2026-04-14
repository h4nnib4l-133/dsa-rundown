#include "../test_runner.h"

int max_area(int* height, int n) {
    return -1;
}

int main() {
    TEST_INT("basic",   max_area(ARR(1,8,6,2,5,4,8,3,7), 9), 49);
    TEST_INT("minimal", max_area(ARR(1,1), 2),                 1);
    TEST_INT("U shape", max_area(ARR(4,3,2,1,4), 5),          16);
    TEST_SUMMARY();
}
