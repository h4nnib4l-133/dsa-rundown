#include "../test_runner.h"

void daily_temperatures(int* temps, int n, int* out) {
    for (int i = 0; i < n; i++) out[i] = 0;
}

int main() {
    int out[10];
    daily_temperatures(ARR(73,74,75,71,69,72,76,73), 8, out);
    TEST_ARR("basic", out, ARR(1,1,4,2,1,1,0,0), 8);
    daily_temperatures(ARR(30,40,50,60), 4, out);
    TEST_ARR("increasing", out, ARR(1,1,1,0), 4);
    TEST_SUMMARY();
}
