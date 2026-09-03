# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 == None:
        #     return list2
        # if list2 == None:
        #     return list1

        # if list1.val > list2.val:
        #     head = ListNode(list2.val)
        #     list2= list2.next
        # else:
        #     head = ListNode(list1.val)
        #     list1 = list1.next
        temp_head = head = ListNode()

        while list2 != None and list1!= None:
            if list1.val > list2.val:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next
            head = head.next
        head.next = list1 or list2
        return temp_head.next