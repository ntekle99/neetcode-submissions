# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 0->1->2->3
# 0->1->2->3<-4<-5<-6
# 1 3 2 5 3 None
# 1 3 2 5 3
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        temp = slower = head 
        faster = head.next
        while faster!= None:
            slower = slower.next
            faster = faster.next
            if faster == None:
                break
            faster = faster.next

        prev = None
        curr = slower.next
        slower.next = None
        nxt = curr.next

        while curr!=None:
            curr.next = prev
            prev = curr
            curr = nxt
            if nxt != None:
                nxt = nxt.next
        
        #print(prev.val,temp.val)
        #real_first = temp
        while temp!=None and prev!=None:
            nxt_1 = temp.next
            nxt_2 = prev.next
            temp.next = prev
            prev.next = nxt_1
            temp = nxt_1

            prev = nxt_2

