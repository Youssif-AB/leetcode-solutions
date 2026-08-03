// https://leetcode.com/problems/palindrome-number

import java.util.*;

class Solution {
    public boolean isPalindrome(int x) {
        
        String x_string = Integer.toString(x);
        char[] x_array = new char[x_string.length()];
        char[] x_array_backwards = new char[x_string.length()];
        
        for (int i = 0; i < x_string.length(); i++)
        {
            x_array[i] = x_string.charAt(i);
            x_array_backwards[i] = x_string.charAt(x_string.length() - (i + 1));
        }
        
        return Arrays.equals(x_array, x_array_backwards);
        
    }
}