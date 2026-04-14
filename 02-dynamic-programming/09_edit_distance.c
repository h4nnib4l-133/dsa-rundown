#include "../test_runner.h"

int min_distance(char* w1, char* w2) {
    return -1;
}

int main() {
    TEST_INT("horse->ros",  min_distance("horse", "ros"),           3);
    TEST_INT("intention",   min_distance("intention", "execution"), 5);
    TEST_INT("empty to abc",min_distance("", "abc"),                3);
    TEST_INT("same",        min_distance("abc", "abc"),             0);
    TEST_SUMMARY();
}
