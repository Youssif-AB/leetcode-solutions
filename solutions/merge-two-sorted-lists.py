# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy

        while list1 is not None or list2 is not None:

            if list1 == None:
                current.next = ListNode(list2.val)
                current = current.next
                list2 = list2.next
            elif list2 == None:
                current.next = ListNode(list1.val)
                current = current.next
                list1 = list1.next
            elif list1.val < list2.val:
                current.next = ListNode(list1.val)
                current = current.next
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                current = current.next
                list2 = list2.next
        
        return dummy.next
            # check if list1 node is smaller than list2 node, if it is put it in new list and advance and check again, otherwise, put list 2 in there and advance and check again

        
        