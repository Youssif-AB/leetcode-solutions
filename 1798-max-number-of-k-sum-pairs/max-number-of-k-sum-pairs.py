from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        counts = Counter(nums)
        counter = 0
        for x in counts:
            if x != k/2:
                if counts[k - x] > 0:
                    amount = min(counts[x], counts[k - x])
                    counter += amount
                    counts[x] -= amount
                    counts[k-x] -= amount
            else:
                if counts[k - x] > 0:
                    amount = int(counts[x] // 2)
                    counter += amount
                    counts[x] -= amount

        return counter            

    
        