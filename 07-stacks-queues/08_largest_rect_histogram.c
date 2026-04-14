#include "../test_runner.h"

int largest_rectangle_area(int* heights, int n) {
    return -1;
}

int main() {
    TEST_INT("basic",  largest_rectangle_area(ARR(2,1,5,6,2,3), 6), 10);
    TEST_INT("two",    largest_rectangle_area(ARR(2,4), 2),          4);
    TEST_INT("single", largest_rectangle_area(ARR(1), 1),            1);
    TEST_SUMMARY();
}
