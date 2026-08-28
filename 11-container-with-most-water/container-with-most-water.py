class Solution(object):
    def maxArea(self, height):
        max_area = 0
        i = 0
        j = len(height) - 1

        while i != j:
            if max_area < ((j - i) * min(height[i], height[j])):
                max_area = ((j - i) * min(height[i], height[j]))
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area