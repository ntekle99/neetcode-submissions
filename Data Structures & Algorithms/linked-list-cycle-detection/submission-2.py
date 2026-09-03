# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        slower = head
        faster = head.next
        while slower!=None and faster!=None:
            if slower == faster:
                return True
            slower = slower.next
            faster = faster.next

            if slower == faster:
                return True
            if faster == None:
                return False
            faster = faster.next
        return False