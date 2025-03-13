// 1143. Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/

class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int[][] memo = new int[text1.length() + 1][text2.length() + 1];

        for (int i = text1.length() - 1; i >= 0; i--) {
            for (int j = text2.length() - 1; j >= 0; j--) {
                if (text1.charAt(i) == text2.charAt(j)) {
                    memo[i][j] = 1 + memo[i + 1][j + 1];

                    continue;
                }

                memo[i][j] = Math.max(memo[i + 1][j], memo[i][j + 1]);
            }
        }

        return memo[0][0];
    }
}

/*
 * text1 = "abcde", text2 = "ace"
 * ___a_c_e
 * a [0,0,1,0]
 * b [0,0,1,0]
 * c [0,2,1,0]
 * d [0,1,1,0]
 * e [0,1,1,0]
 * __[0,0,0,0]
 */