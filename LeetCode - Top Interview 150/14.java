// 14. Longest Common Prefix
// https://leetcode.com/problems/longest-common-prefix/

class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }

        String commonPrefix = strs[0];

        int current = 1;

        while (current < strs.length) {
            String str = strs[current];

            while (!str.startsWith(commonPrefix)) {
                commonPrefix = commonPrefix.substring(0, commonPrefix.length() - 1);
            }

            current += 1;
        }

        return commonPrefix;
    }
}

/*
 * ["flower","flow","flight"]
 */