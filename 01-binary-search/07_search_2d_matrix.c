#include "../test_runner.h"

bool search_matrix(int matrix[][4], int rows, int cols, int target) {
    return false;
}

int main() {
    int m1[][4] = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
    TEST_BOOL("found 3",     search_matrix(m1, 3, 4, 3),   true);
    TEST_BOOL("not found 13",search_matrix(m1, 3, 4, 13),  false);
    int m2[][4] = {{1}};
    TEST_BOOL("single found",    search_matrix(m2, 1, 1, 1), true);
    TEST_BOOL("single not found",search_matrix(m2, 1, 1, 2), false);
    TEST_SUMMARY();
}
