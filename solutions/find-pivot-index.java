// https://leetcode.com/problems/find-pivot-index

class Solution {
    public int pivotIndex(int[] nums) {
        
        int leftsum = 0;
        int rightsum = 0;
        
        int fullsum = 0;
        
        for (int i = 0; i < nums.length; i++)
        {
            fullsum += nums[i];
        }
        
        for (int i = 0; i < nums.length; i++)
        {
            
            rightsum = fullsum - leftsum - nums[i];
            
            if (leftsum == rightsum)
            {
                return i;
            }
            
            
            leftsum += nums[i];
        }
        
        return -1;
    }
}