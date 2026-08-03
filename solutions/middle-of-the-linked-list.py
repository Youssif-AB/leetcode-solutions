# https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        final = []
        count = 0
        current = head
        while current: ## means while current is not none, or we've not reached the end i think
            count += 1
            current = current.next
        

        middle = count//2

        current = head
        for i in range(middle):
            current = current.next

        return current

                


