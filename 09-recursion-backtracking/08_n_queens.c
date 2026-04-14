#include "../test_runner.h"

int solve_n_queens(int n) {
    return -1;
}

int main() {
    TEST_INT("n=4", solve_n_queens(4), 2);
    TEST_INT("n=1", solve_n_queens(1), 1);
    TEST_INT("n=8", solve_n_queens(8), 92);
    TEST_SUMMARY();
}
