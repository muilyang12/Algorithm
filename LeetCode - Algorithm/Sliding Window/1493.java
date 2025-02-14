// 1493. Longest Subarray of 1's After Deleting One Element
// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution {
    public int longestSubarray(int[] nums) {
        int result = 0;

        int left = 0;
        int right = 0;

        int indexOfZero = -1;

        while (right < nums.length) {
            if (nums[right] == 0 && indexOfZero < 0) {
                indexOfZero = right;
            } else if (nums[right] == 0) {
                result = Math.max(result, right - left - 1);

                left = indexOfZero + 1;
                indexOfZero = right;
            }

            right += 1;
        }

        result = Math.max(result, right - left - 1);

        return result;
    }
}