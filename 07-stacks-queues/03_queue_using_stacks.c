#include "../test_runner.h"

#define MAX_Q 1000

typedef struct {
    int s1[MAX_Q], s2[MAX_Q];
    int top1, top2;
} MyQueue;

void q_init(MyQueue* q) { q->top1 = -1; q->top2 = -1; }

void q_push(MyQueue* q, int x) { /* your code */ }
int q_pop(MyQueue* q) { return -1; }
int q_peek(MyQueue* q) { return -1; }
bool q_empty(MyQueue* q) { return true; }

int main() {
    MyQueue q;
    q_init(&q);
    q_push(&q, 1);
    q_push(&q, 2);
    TEST_INT("peek", q_peek(&q), 1);
    TEST_INT("pop",  q_pop(&q),  1);
    TEST_BOOL("not empty", q_empty(&q), false);
    TEST_SUMMARY();
}
