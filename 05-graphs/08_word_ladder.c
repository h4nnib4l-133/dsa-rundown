#include "../test_runner.h"

int ladder_length(char* begin, char* end, char** words, int n) {
    return 0;
}

int main() {
    char* w1[] = {"hot","dot","dog","lot","log","cog"};
    TEST_INT("found",     ladder_length("hit","cog",w1,6), 5);
    char* w2[] = {"hot","dot","dog","lot","log"};
    TEST_INT("not found", ladder_length("hit","cog",w2,5), 0);
    TEST_SUMMARY();
}
