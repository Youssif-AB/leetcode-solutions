# https://leetcode.com/problems/merge-sorted-array

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums3 = []
        for i in range(m):
            nums3.append(nums1[i])
        for i in range(n):
            nums3.append(nums2[i])
        
        for i in range(len(nums1)):
            nums1[i] = nums3[i]
    
        nums1.sort()