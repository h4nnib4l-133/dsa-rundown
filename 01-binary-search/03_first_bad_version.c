#include "../test_runner.h"

static int _bad_version;
bool isBadVersion(int v) { return v >= _bad_version; }

int first_bad_version(int n) {
    return -1;
}

int main() {
    _bad_version = 4; TEST_INT("bad=4 n=5",   first_bad_version(5),   4);
    _bad_version = 1; TEST_INT("bad=1 n=5",   first_bad_version(5),   1);
    _bad_version = 1; TEST_INT("bad=1 n=1",   first_bad_version(1),   1);
    _bad_version = 7; TEST_INT("bad=7 n=10",  first_bad_version(10),  7);
    _bad_version = 50;TEST_INT("bad=50 n=100",first_bad_version(100), 50);
    TEST_SUMMARY();
}
