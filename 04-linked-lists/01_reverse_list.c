#include "../test_runner.h"

typedef struct ListNode {
    int val;
    struct ListNode* next;
} ListNode;

ListNode* make_node(int val) {
    ListNode* n = malloc(sizeof(ListNode));
    n->val = val; n->next = NULL;
    return n;
}

ListNode* make_list(int* arr, int n) {
    if (n == 0) return NULL;
    ListNode* head = make_node(arr[0]);
    ListNode* curr = head;
    for (int i = 1; i < n; i++) {
        curr->next = make_node(arr[i]);
        curr = curr->next;
    }
    return head;
}

void to_array(ListNode* head, int* out, int* len) {
    *len = 0;
    while (head) { out[(*len)++] = head->val; head = head->next; }
}

/* ---- WRITE YOUR SOLUTION HERE ---- */

ListNode* reverse_list(ListNode* head) {
    return NULL;
}

/* ---- END SOLUTION ---- */

int main() {
    int out[10], len;
    to_array(reverse_list(make_list(ARR(1,2,3,4,5), 5)), out, &len);
    TEST_ARR("5 nodes", out, ARR(5,4,3,2,1), 5);

    to_array(reverse_list(make_list(ARR(1,2), 2)), out, &len);
    TEST_ARR("2 nodes", out, ARR(2,1), 2);

    to_array(reverse_list(make_list(ARR(1), 1)), out, &len);
    TEST_ARR("1 node", out, ARR(1), 1);

    to_array(reverse_list(NULL), out, &len);
    TEST_INT("empty", len, 0);

    TEST_SUMMARY();
}
