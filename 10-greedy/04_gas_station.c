#include "../test_runner.h"

int can_complete_circuit(int* gas, int* cost, int n) {
    return -1;
}

int main() {
    TEST_INT("found",     can_complete_circuit(ARR(1,2,3,4,5), ARR(3,4,5,1,2), 5),  3);
    TEST_INT("impossible",can_complete_circuit(ARR(2,3,4), ARR(3,4,3), 3),          -1);
    TEST_SUMMARY();
}
