# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head

        prev = None
        curr = head
        nxt = head.next
        while curr != None:
            curr.next = prev
            prev = curr
            curr = nxt
            if nxt !=None:
                nxt = nxt.next
        return prev