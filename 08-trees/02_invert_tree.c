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

TreeNode* invert_tree(TreeNode* root) {
    return NULL;
}

int main() {
    TreeNode* r = make_tnode(4);
    r->left = make_tnode(2); r->right = make_tnode(7);
    r->left->left = make_tnode(1); r->left->right = make_tnode(3);
    TreeNode* inv = invert_tree(r);
    TEST_INT("root", inv->val, 4);
    TEST_INT("swapped left", inv->left->val, 7);
    TEST_INT("swapped right", inv->right->val, 2);
    TEST_SUMMARY();
}
