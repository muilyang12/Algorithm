// 238. Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/

import java.util.Arrays;

class Solution {
    // time complexity: O(2n) = O(n)
    public int[] productExceptSelf(int[] nums) {
        int zeroCount = 0;
        int zeroIndex = -1;

        int allValuesProducted = 1;

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];

            if (num == 0 && zeroCount == 0) {
                zeroCount += 1;
                zeroIndex = i;
            } else if (num == 0 && zeroCount == 1) {
                int[] zeros = new int[nums.length];
                Arrays.fill(zeros, 0);

                return zeros;
            } else {
                allValuesProducted *= num;
            }
        }

        int[] result = new int[nums.length];
        Arrays.fill(result, 0);

        if (zeroCount == 1)
            result[zeroIndex] = allValuesProducted;
        else
            for (int i = 0; i < nums.length; i++) {
                result[i] = allValuesProducted / nums[i];
            }

        return result;
    }
}