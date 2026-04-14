#include "../test_runner.h"

void bfs_shortest(int n, int edges[][2], int num_edges, int start, int* dist) {
    for (int i = 0; i < n; i++) dist[i] = -1;
}

int main() {
    int dist[10];
    int e1[][2] = {{0,1},{0,2},{1,3}};
    bfs_shortest(4, e1, 3, 0, dist);
    TEST_ARR("4 nodes", dist, ARR(0,1,1,2), 4);

    int e2[][2] = {{0,1}};
    bfs_shortest(3, e2, 1, 0, dist);
    TEST_ARR("unreachable", dist, ARR(0,1,-1), 3);
    TEST_SUMMARY();
}
