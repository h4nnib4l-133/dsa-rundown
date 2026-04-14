#include "../test_runner.h"

#define MAX_STACK 1000

typedef struct {
    int data[MAX_STACK];
    int mins[MAX_STACK];
    int top;
} MinStack;

void ms_init(MinStack* s) { s->top = -1; }

void ms_push(MinStack* s, int val) {
    /* your code */
}

void ms_pop(MinStack* s) {
    /* your code */
}

int ms_top(MinStack* s) {
    return -1;
}

int ms_get_min(MinStack* s) {
    return -1;
}

int main() {
    MinStack s;
    ms_init(&s);
    ms_push(&s, -2);
    ms_push(&s, 0);
    ms_push(&s, -3);
    TEST_INT("min after pushes", ms_get_min(&s), -3);
    ms_pop(&s);
    TEST_INT("top after pop", ms_top(&s), 0);
    TEST_INT("min after pop", ms_get_min(&s), -2);
    TEST_SUMMARY();
}
