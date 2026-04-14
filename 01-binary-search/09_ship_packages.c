#include "../test_runner.h"

int ship_within_days(int* weights, int n, int days) {
    return -1;
}

int main() {
    TEST_INT("basic",   ship_within_days(ARR(1,2,3,4,5,6,7,8,9,10), 10, 5), 15);
    TEST_INT("small",   ship_within_days(ARR(3,2,2,4,1,4), 6, 3),            6);
    TEST_INT("tight",   ship_within_days(ARR(1,2,3,1,1), 5, 4),              3);
    TEST_SUMMARY();
}
