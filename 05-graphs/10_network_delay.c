#include "../test_runner.h"

int network_delay_time(int times[][3], int num_edges, int n, int k) {
    return -1;
}

int main() {
    int t1[][3] = {{2,1,1},{2,3,1},{3,4,1}};
    TEST_INT("basic",       network_delay_time(t1, 3, 4, 2),  2);
    int t2[][3] = {{1,2,1}};
    TEST_INT("direct",      network_delay_time(t2, 1, 2, 1),  1);
    TEST_INT("unreachable", network_delay_time(t2, 1, 2, 2), -1);
    TEST_SUMMARY();
}
