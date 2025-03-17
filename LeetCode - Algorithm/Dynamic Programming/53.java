// 53. Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/

import java.util.Arrays;

// Memory Limit Exceeded :(
class Solution1 {
    public int maxSubArray(int[] nums) {
        int result = Integer.MIN_VALUE;

        int[][] memo = new int[nums.length + 1][nums.length + 1];

        for (int i = 0; i < nums.length; i++) {
            memo[i][i] = nums[i];

            result = Math.max(result, memo[i][i]);
        }

        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                memo[i][j] = memo[i][j - 1] + memo[j][j];

                result = Math.max(result, memo[i][j]);
            }
        }

        return result;
    }
}

class Solution2 {
    public int maxSubArray(int[] nums) {
        int[] memo = Arrays.copyOf(nums, nums.length);

        int result = memo[0];

        for (int i = 1; i < memo.length; i++) {
            memo[i] = Math.max(memo[i - 1] + memo[i], memo[i]);

            result = Math.max(result, memo[i]);
        }

        return result;
    }
}

/*
 * nums = [-2,1,-3,4,-1,2,1,-5,4]
 * 
 * [-2,-1, 0, 0, 0, 0, 0, 0, 0, 0]
 * [ 0, 1,-2, 0, 0, 0, 0, 0, 0, 0]
 * [ 0, 0,-3, 1, 0, 0, 0, 0, 0, 0]
 * [ 0, 0, 0, 4, 0, 0, 0, 0, 0, 0]
 * [ 0, 0, 0, 0,-1, 0, 0, 0, 0, 0]
 * [ 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]
 * [ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
 * [ 0, 0, 0, 0, 0, 0, 0,-5, 0, 0]
 * [ 0, 0, 0, 0, 0, 0, 0, 0, 4, 0]
 * [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 */