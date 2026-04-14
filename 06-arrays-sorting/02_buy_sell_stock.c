#include "../test_runner.h"

int max_profit(int* prices, int n) {
    return -1;
}

int main() {
    TEST_INT("basic",     max_profit(ARR(7,1,5,3,6,4), 6), 5);
    TEST_INT("decreasing",max_profit(ARR(7,6,4,3,1), 5),   0);
    TEST_INT("small",     max_profit(ARR(2,4,1), 3),        2);
    TEST_INT("single",    max_profit(ARR(1), 1),             0);
    TEST_SUMMARY();
}
