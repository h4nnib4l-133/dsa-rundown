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


ListNode* merge_two_lists(ListNode* l1, ListNode* l2) {
    return NULL;
}

int main() {
    int out[10], len;
    to_array(merge_two_lists(make_list(ARR(1,2,4),3), make_list(ARR(1,3,4),3)), out, &len);
    TEST_ARR("basic", out, ARR(1,1,2,3,4,4), 6);
    to_array(merge_two_lists(NULL, make_list(ARR(0),1)), out, &len);
    TEST_ARR("one empty", out, ARR(0), 1);
    to_array(merge_two_lists(NULL, NULL), out, &len);
    TEST_INT("both empty", len, 0);
    TEST_SUMMARY();
}
