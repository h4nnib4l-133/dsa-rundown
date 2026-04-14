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


void reorder_list(ListNode* head) {
    /* your code */
}

int main() {
    int out[10], len;
    ListNode* h = make_list(ARR(1,2,3,4), 4);
    reorder_list(h);
    to_array(h, out, &len);
    TEST_ARR("4 nodes", out, ARR(1,4,2,3), 4);

    h = make_list(ARR(1,2,3,4,5), 5);
    reorder_list(h);
    to_array(h, out, &len);
    TEST_ARR("5 nodes", out, ARR(1,5,2,4,3), 5);
    TEST_SUMMARY();
}
