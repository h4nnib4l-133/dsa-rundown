#include "../test_runner.h"

int alternating_characters(char* s) {
    return -1;
}

int main() {
    TEST_INT("AAAA",     alternating_characters("AAAA"),     3);
    TEST_INT("BBBBB",    alternating_characters("BBBBB"),    4);
    TEST_INT("ABABABAB", alternating_characters("ABABABAB"), 0);
    TEST_INT("AAABBB",   alternating_characters("AAABBB"),   4);
    TEST_SUMMARY();
}
