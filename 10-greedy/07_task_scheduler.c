#include "../test_runner.h"

int least_interval(char* tasks, int num_tasks, int n) {
    return -1;
}

int main() {
    TEST_INT("basic",    least_interval("AAABBB", 6, 2), 8);
    TEST_INT("no cool",  least_interval("AAABBB", 6, 0), 6);
    TEST_SUMMARY();
}
