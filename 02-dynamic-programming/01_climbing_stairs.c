#include "../test_runner.h"

int climb_stairs(int n) {
    return -1;
}

int main() {
    TEST_INT("n=2",  climb_stairs(2),  2);
    TEST_INT("n=3",  climb_stairs(3),  3);
    TEST_INT("n=1",  climb_stairs(1),  1);
    TEST_INT("n=5",  climb_stairs(5),  8);
    TEST_INT("n=10", climb_stairs(10), 89);
    TEST_SUMMARY();
}
