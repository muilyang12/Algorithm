// 55. Jump Game
// https://leetcode.com/problems/jump-game/

class Solution {
    public boolean canJump(int[] nums) {
        boolean[] memo = new boolean[nums.length];
        memo[0] = true;

        for (int i = 0; i < nums.length; i++) {
            if (!memo[i])
                continue;

            for (int j = 1; j <= nums[i]; j++) {
                if (i + j >= nums.length)
                    return true;

                memo[i + j] = true;
            }
        }

        return memo[memo.length - 1];
    }
}

/*
 * nums = [2,3,1,1,4]
 * [t,t,t,t,t,f]
 */