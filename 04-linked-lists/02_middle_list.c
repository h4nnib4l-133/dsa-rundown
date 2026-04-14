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


ListNode* middle_node(ListNode* head) {
    return NULL;
}

int main() {
    int out[10], len;
    to_array(middle_node(make_list(ARR(1,2,3,4,5), 5)), out, &len);
    TEST_ARR("odd",  out, ARR(3,4,5), 3);
    to_array(middle_node(make_list(ARR(1,2,3,4,5,6), 6)), out, &len);
    TEST_ARR("even", out, ARR(4,5,6), 3);
    TEST_SUMMARY();
}
