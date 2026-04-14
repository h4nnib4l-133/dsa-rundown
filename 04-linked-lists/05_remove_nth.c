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


ListNode* remove_nth_from_end(ListNode* head, int n) {
    return NULL;
}

int main() {
    int out[10], len;
    to_array(remove_nth_from_end(make_list(ARR(1,2,3,4,5),5), 2), out, &len);
    TEST_ARR("remove 2nd from end", out, ARR(1,2,3,5), 4);
    to_array(remove_nth_from_end(make_list(ARR(1),1), 1), out, &len);
    TEST_INT("remove only", len, 0);
    to_array(remove_nth_from_end(make_list(ARR(1,2),2), 2), out, &len);
    TEST_ARR("remove head", out, ARR(2), 1);
    TEST_SUMMARY();
}
