// https://leetcode.com/problems/roman-to-integer

import java.io.*;
import java.util.*;


class Solution {
    public int romanToInt(String s) {
        
        String[] symbol = {"I", "V", "X", "L", "C", "D", "M"};
        int[] value = {1,5,10,50,100,500,1000};
        
        int result = 0;
        
        for (int i = 0; i < s.length(); i++)
        {
            for (int a = 0; a < symbol.length; a++)
            {
                if (i == s.length() - 1)
                {
                    if (Character.toString(s.charAt(i)).equals(symbol[a]))
                    {
                        result += value[a];
                        break;
                    }
                }
                else if ((Character.toString(s.charAt(i)) + Character.toString(s.charAt(i + 1))).equals("IV"))
                {
                    result += 4;
                    i = i + 1;
                    break;
                }
                else if ((Character.toString(s.charAt(i)) + Character.toString(s.charAt(i + 1))).equals("XL"))
                {
                    result += 40;
                    i = i + 1;
                    break;
                }
                else if ((Character.toString(s.charAt(i)) + Character.toString(s.charAt(i + 1))).equals("XC"))
                {
                    result += 90;
                    i = i + 1;
                    break;
                }
                else if ((Character.toString(s.charAt(i)) + Character.toString(s.charAt(i + 1))).equals("CM"))
                {
                    result += 900;
                    i = i + 1;
                    break;
                }
                else if ((Character.toString(s.charAt(i)) + Character.toString(s.charAt(i + 1))).equals("CD"))
                {
                    result += 400;
                    i = i + 1;
                    break;
                }
                else if ((Character.toString(s.charAt(i)) + Character.toString(s.charAt(i + 1))).equals("IX"))
                {
                    result += 9;
                    i = i + 1;
                    break;
                }
                else if (Character.toString(s.charAt(i)).equals(symbol[a]))
                {
                    result += value[a];
                    break;
                }

            }
            
            
        }
        
        return result;
    }
}