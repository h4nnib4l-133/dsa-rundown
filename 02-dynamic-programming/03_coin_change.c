#include "../test_runner.h"

int coin_change(int* coins, int n, int amount) {
    return -1;
}

int main() {
    TEST_INT("quarters",   coin_change(ARR(1,5,10,25), 4, 30),  2);
    TEST_INT("basic",      coin_change(ARR(1,2,5), 3, 11),      3);
    TEST_INT("impossible", coin_change(ARR(2), 1, 3),           -1);
    TEST_INT("zero",       coin_change(ARR(1), 1, 0),            0);
    TEST_INT("large",      coin_change(ARR(1,2,5), 3, 100),    20);
    TEST_SUMMARY();
}
