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


ListNode* add_two_numbers(ListNode* l1, ListNode* l2) {
    return NULL;
}

int main() {
    int out[10], len;
    to_array(add_two_numbers(make_list(ARR(2,4,3),3), make_list(ARR(5,6,4),3)), out, &len);
    TEST_ARR("342+465", out, ARR(7,0,8), 3);
    to_array(add_two_numbers(make_list(ARR(9,9,9),3), make_list(ARR(1),1)), out, &len);
    TEST_ARR("999+1", out, ARR(0,0,0,1), 4);
    TEST_SUMMARY();
}
