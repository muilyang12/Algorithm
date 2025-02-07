// 345. Reverse Vowels of a String
// https://leetcode.com/problems/reverse-vowels-of-a-string/

import java.util.Set;
import java.util.Stack;

class Solution {
    public String reverseVowels(String s) {
        Stack<Character> usedVowels = new Stack<>();

        Set<Character> vowels = Set.of('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');

        for (int i = 0; i < s.length(); i++) {
            if (vowels.contains(s.charAt(i))) {
                usedVowels.push(s.charAt(i));
            }
        }

        String result = "";

        for (int i = 0; i < s.length(); i++) {
            if (vowels.contains(s.charAt(i))) {
                result += usedVowels.pop();
            } else {
                result += s.charAt(i);
            }
        }

        return result;
    }
}