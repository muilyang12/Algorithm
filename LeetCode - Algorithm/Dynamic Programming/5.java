// 5. Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/

class Solution {
    public String longestPalindrome(String s) {
        boolean[][] memo = new boolean[s.length()][s.length()];

        for (int i = 0; i < s.length(); i++)
            memo[i][i] = true;

        for (int i = 0; i <= s.length() - 2; i++)
            if (s.charAt(i) == s.charAt(i + 1))
                memo[i][i + 1] = true;

        for (int i = 2; i < s.length(); i++) {
            for (int j = 0; j < s.length() - i; j++) {
                if (!memo[j + 1][j + i - 1])
                    continue;

                if (s.charAt(j) == s.charAt(j + i))
                    memo[j][j + i] = true;
            }
        }

        for (int i = s.length() - 1; i >= 0; i--) {
            for (int j = 0; j < s.length() - i; j++) {
                if (memo[j][j + i])
                    return s.substring(j, j + i + 1);
            }
        }

        return "";
    }
}

/*
 * s = "babad"
 * ___b_a_b_a_d
 * b [t,f,t,f,f]
 * a [f,t,f,t,f]
 * b [f,f,t,f,f]
 * a [f,f,f,t,f]
 * d [f,f,f,f,t]
 */

/*
 * s = "aaaaa"
 * ___b_a_b_a_d
 * b [t,t,f,f,f]
 * a [f,t,t,f,f]
 * b [f,f,t,t,f]
 * a [f,f,f,t,t]
 * d [f,f,f,f,t]
 */

/*
 * s = "a"
 * ___a
 * a [t]
 */