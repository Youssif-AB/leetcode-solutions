class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        index = 0
        while left <= right:
            mid = (left + right) // 2

            print(nums[mid])
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
                index = mid + 1
                print("index is: " + str(index))
            else:
                right = mid - 1
                index = mid if mid != 0 else 0


        return index
                
                