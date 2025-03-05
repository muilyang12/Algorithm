// 1456. Maximum Number of Vowels in a Substring of Given Length
// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

import java.util.Set;

class Solution {
    public int maxVowels(String s, int k) {
        Set<Character> vowels = Set.of('a', 'e', 'i', 'o', 'u');

        int result = 0;

        int left = 0;
        int right = k - 1;

        for (int i = left; i <= right; i++) {
            if (vowels.contains(s.charAt(i)))
                result += 1;
        }

        int nextCount = result;

        while (right < s.length() - 1) {
            if (vowels.contains(s.charAt(left))) {
                nextCount -= 1;
            }

            if (vowels.contains(s.charAt(right + 1))) {
                nextCount += 1;
            }

            left += 1;
            right += 1;

            result = Math.max(result, nextCount);
        }

        return result;
    }
}

// s = "leetcode", k = 3