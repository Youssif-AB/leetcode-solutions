class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = 0

        for i in range(k):
            max_avg += nums[i]
        
        max_avg = max_avg
        largest_avg = max_avg

        for j in range(k, len(nums)):
            max_avg = max_avg - nums[j - k] + nums[j]
            if max_avg > largest_avg:
                largest_avg = max_avg
        
        return largest_avg/k
            