// 198. House Robber
// https://leetcode.com/problems/house-robber/

class Solution {
    public int rob(int[] nums) {
        int[] memo = new int[nums.length + 1];
        memo[0] = 0;
        memo[1] = nums[0];

        for (int i = 1; i < nums.length; i++) {
            memo[i + 1] = Math.max(memo[i - 1] + nums[i], memo[i]);
        }

        return Math.max(memo[memo.length - 1], memo[memo.length - 2]);
    }
}

// Input: nums = [2,7,9,3,1]
// Output: 12