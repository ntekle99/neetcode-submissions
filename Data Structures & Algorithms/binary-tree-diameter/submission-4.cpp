/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <algorithm>
class Solution {
private:
int mx_diameter = 0;
    int height(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }

        int left_height = height(node->left);
        int right_height = height(node->right);

        mx_diameter = std::max(mx_diameter, left_height + right_height);

        return 1 + std::max(left_height, right_height);
    }
public:
    int diameterOfBinaryTree(TreeNode* root) {
        height(root);
        return mx_diameter;
    }
};
