#include "../test_runner.h"

int min_eating_speed(int* piles, int n, int h) {
    return -1;
}

int main() {
    TEST_INT("basic",      min_eating_speed(ARR(3,6,7,11), 4, 8),        4);
    TEST_INT("tight",      min_eating_speed(ARR(30,11,23,4,20), 5, 5),  30);
    TEST_INT("relaxed",    min_eating_speed(ARR(30,11,23,4,20), 5, 6),  23);
    TEST_SUMMARY();
}
