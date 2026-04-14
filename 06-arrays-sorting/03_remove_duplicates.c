#include "../test_runner.h"

int remove_duplicates(int* nums, int n) {
    return -1;
}

int main() {
    int a1[] = {1,1,2};
    TEST_INT("basic",  remove_duplicates(a1, 3), 2);
    int a2[] = {0,0,1,1,1,2,2,3,3,4};
    TEST_INT("longer", remove_duplicates(a2, 10), 5);
    int a3[] = {1};
    TEST_INT("single", remove_duplicates(a3, 1), 1);
    TEST_SUMMARY();
}
