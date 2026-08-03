// https://leetcode.com/problems/is-subsequence

class Solution {
 public boolean isSubsequence(String s1, String s2) {
        if (s1.length() == 0) return true;

        int n = 0;
        for (int i = 0; i < s2.length() && n < s1.length(); i++) {
            if (s2.charAt(i) == s1.charAt(n)) n++;
        }

        return n == s1.length() ? true : false;
    }
}