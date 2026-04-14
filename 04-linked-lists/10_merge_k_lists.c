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


/* Simple approach: repeatedly find min head */
ListNode* merge_k_lists(ListNode** lists, int k) {
    return NULL;
}

int main() {
    int out[20], len;
    ListNode* lists[3] = {
        make_list(ARR(1,4,5), 3),
        make_list(ARR(1,3,4), 3),
        make_list(ARR(2,6), 2)
    };
    to_array(merge_k_lists(lists, 3), out, &len);
    TEST_ARR("3 lists", out, ARR(1,1,2,3,4,4,5,6), 8);
    TEST_SUMMARY();
}
