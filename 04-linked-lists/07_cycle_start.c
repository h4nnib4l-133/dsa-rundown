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


ListNode* detect_cycle(ListNode* head) {
    return NULL;
}

int main() {
    ListNode* n1=make_node(3); ListNode* n2=make_node(2);
    ListNode* n3=make_node(0); ListNode* n4=make_node(-4);
    n1->next=n2; n2->next=n3; n3->next=n4; n4->next=n2;
    TEST_INT("cycle at 2", detect_cycle(n1)->val, 2);
    TEST_BOOL("no cycle", detect_cycle(make_node(1)) == NULL, true);
    TEST_SUMMARY();
}
