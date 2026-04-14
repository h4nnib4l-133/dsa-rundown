#include "../test_runner.h"

int max_profit(int* prices, int n) {
    return -1;
}

int main() {
    TEST_INT("ups and downs", max_profit(ARR(7,1,5,3,6,4), 6), 7);
    TEST_INT("all up",        max_profit(ARR(1,2,3,4,5), 5),   4);
    TEST_INT("all down",      max_profit(ARR(7,6,4,3,1), 5),   0);
    TEST_SUMMARY();
}
