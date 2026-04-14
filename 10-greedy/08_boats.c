#include "../test_runner.h"

int num_rescue_boats(int* people, int n, int limit) {
    return -1;
}

int main() {
    TEST_INT("pair",   num_rescue_boats(ARR(1,2), 2, 3),    1);
    TEST_INT("mixed",  num_rescue_boats(ARR(3,2,2,1), 4, 3),3);
    TEST_INT("heavy",  num_rescue_boats(ARR(3,5,3,4), 4, 5),4);
    TEST_SUMMARY();
}
