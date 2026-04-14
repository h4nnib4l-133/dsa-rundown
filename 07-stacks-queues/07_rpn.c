#include "../test_runner.h"

int eval_rpn(char** tokens, int n) {
    return 0;
}

int main() {
    char* t1[] = {"2","1","+","3","*"};
    TEST_INT("basic", eval_rpn(t1, 5), 9);
    char* t2[] = {"4","13","5","/","+"};
    TEST_INT("division", eval_rpn(t2, 5), 6);
    TEST_SUMMARY();
}
