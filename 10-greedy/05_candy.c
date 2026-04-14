#include "../test_runner.h"

int candy(int* ratings, int n) {
    return -1;
}

int main() {
    TEST_INT("basic",    candy(ARR(1,0,2), 3),    5);
    TEST_INT("plateau",  candy(ARR(1,2,2), 3),    4);
    TEST_INT("mountain", candy(ARR(1,3,2,2,1), 5),7);
    TEST_SUMMARY();
}
