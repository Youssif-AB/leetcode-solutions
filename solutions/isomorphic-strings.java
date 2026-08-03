// https://leetcode.com/problems/isomorphic-strings

import java.util.*;

class Solution {
    public boolean isIsomorphic(String s, String t) {
        
        int counter = 0;
        int counter_2 = 0;
        
        HashMap<Character, Character> words = new HashMap<Character, Character>();
        
        String letters = "";
        
        
        if (s.length() != t.length())
        {
            return false;
        }
        
        for (int i = 0; i < s.length(); i++)
        {
            
            if (words.containsKey(s.charAt(i)))
            {
                if ((words.get(s.charAt(i))).equals(t.charAt(i)))
                {
                    System.out.println(words.get(s.charAt(i)));
                    counter++;
                }
                else
                {
                    System.out.println("broken");
                    return false;
                }
            }
            else if (words.containsValue(t.charAt(i)))
            {
               for (int a = 0; a < words.size(); a++)
               {
                   if ((words.get(s.charAt(a))).equals(t.charAt(a)))
                   {
                       letters += Character.toString(s.charAt(a));
                   }
               }
                
                for (int b = 1; b < letters.length(); b++)
                {
                    if ((Character.toString(letters.charAt(b))).equals(Character.toString(letters.charAt(b - 1))))
                    {
                        counter_2++;
                    }
                }
                
                if (counter_2 != letters.length())
                {
                    return false;
                }
                
            }
            else
            {
                words.put(s.charAt(i), t.charAt(i));
                counter++;
                System.out.println("Character inputted");
            }
        }
        
        if (counter == s.length())
        {
            return true;
        }
        
        return false;
        
    }
}