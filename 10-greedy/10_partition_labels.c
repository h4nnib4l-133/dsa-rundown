#include "../test_runner.h"

void partition_labels(char* s, int* out, int* out_len) {
    *out_len = 0;
}

int main() {
    int out[30], len;
    partition_labels("ababcbacadefegdehijhklij", out, &len);
    TEST_ARR("three parts", out, ARR(9,7,8), 3);
    partition_labels("eccbbbbdec", out, &len);
    TEST_ARR("one part", out, ARR(10), 1);
    TEST_SUMMARY();
}
