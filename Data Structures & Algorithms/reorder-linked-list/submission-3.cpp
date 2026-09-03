/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        if (head == nullptr|| head->next == nullptr) return;

        auto slow=head;
        auto fast=head->next;
        while (fast !=nullptr){
            fast=fast->next;
            slow = slow->next;
            if (fast!=nullptr) fast=fast->next;
        }

        ListNode* prev = nullptr;
        auto second_head = slow->next;
        slow->next = nullptr;

        while (second_head!=nullptr){
            auto nxt = second_head->next;
            second_head->next = prev;
            prev = second_head;
            second_head = nxt;
        }

        auto traversal_node = head;
        while (prev!=nullptr){
            auto left_next = traversal_node->next;
            traversal_node->next = prev;
            traversal_node=traversal_node->next;
            if (left_next==nullptr){
                return;
            }
            prev = prev->next;
            traversal_node->next = left_next;
            traversal_node = traversal_node->next;
            }

        
        return;

    }
};
