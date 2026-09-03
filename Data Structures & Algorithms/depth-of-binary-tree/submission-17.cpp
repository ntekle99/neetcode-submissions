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
#include <deque>
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) return 0;
        std::deque<TreeNode*> dq{root};
        int row=0;
        while (dq.size()!=0){
            int size = dq.size();
            for (int i=0;i<size;i++){
                auto element = dq.front();
                dq.pop_front();
                if (element->left!=nullptr){
                    dq.push_back(element->left);
                }
                if (element->right!=nullptr){
                    dq.push_back(element->right);
                }
            }
            row++;
        }
        return row;
    }
};
