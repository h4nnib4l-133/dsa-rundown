#include "../test_runner.h"

typedef struct TreeNode {
    int val;
    struct TreeNode *left, *right;
} TreeNode;

TreeNode* make_tnode(int val) {
    TreeNode* n = malloc(sizeof(TreeNode));
    n->val = val; n->left = NULL; n->right = NULL;
    return n;
}

int max_depth(TreeNode* root) {
    return -1;
}

int main() {
    TreeNode* r = make_tnode(3);
    r->left = make_tnode(9);
    r->right = make_tnode(20);
    r->right->left = make_tnode(15);
    r->right->right = make_tnode(7);
    TEST_INT("depth 3", max_depth(r), 3);
    TEST_INT("null",    max_depth(NULL), 0);
    TEST_SUMMARY();
}
