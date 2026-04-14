#include "../test_runner.h"

int knapsack(int* wt, int* val, int n, int cap) {
    return -1;
}

int main() {
    TEST_INT("basic",    knapsack(ARR(1,2,3), ARR(6,10,12), 3, 5),     22);
    TEST_INT("tight",    knapsack(ARR(2,3,4,5), ARR(3,4,5,6), 4, 5),   7);
    TEST_INT("no fit",   knapsack(ARR(10), ARR(100), 1, 5),             0);
    TEST_INT("pick two", knapsack(ARR(1,1,1), ARR(10,20,30), 3, 2),   50);
    TEST_SUMMARY();
}
