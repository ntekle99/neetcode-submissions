# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#[0,1,2,3]
# [3 next = 2]
# [0] = curr
# [1] = second

# curr = 0
# temp = 1

# 1-> 0, 0-> 2
# temp = 1
# curr = 2
# curr 

# temp.next = temp_2
# curr.next = temp
# temp.nxt = curr
# 




class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev,curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr 
            curr = temp 
        return prev

            

