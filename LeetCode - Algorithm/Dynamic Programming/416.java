// 416. Partition Equal Subset Sum
// https://leetcode.com/problems/partition-equal-subset-sum/

import java.util.Set;
import java.util.HashSet;

class Solution {
    public boolean canPartition(int[] nums) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        if (totalSum % 2 == 1) {
            return false;
        }

        int targetSum = totalSum / 2;

        Set<Integer> sums = new HashSet<>();
        sums.add(0);

        for (int num : nums) {
            if (num > targetSum)
                continue;
            else if (num == targetSum)
                return true;

            Set<Integer> currentSums = new HashSet<>();

            for (int sum : sums) {
                if (sum > targetSum)
                    continue;
                else if (sum + num > targetSum)
                    continue;
                else if (sum + num == targetSum)
                    return true;

                currentSums.add(sum + num);
            }

            sums.addAll(currentSums);
        }

        return false;
    }
}

// nums = [1,5,11,5]
// sums = [0,1,5,6]

// currentSums = []