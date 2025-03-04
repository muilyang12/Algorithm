// 128. Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/

import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.LinkedList;

class Solution {
    // Time Limit Exceeded :(
    // time complexity: O(n^2)
    public int longestConsecutive1(int[] nums) {
        Set<Integer> numsSet = new HashSet<>();
        for (int num : nums)
            numsSet.add(num);

        int result = 0;

        for (int num : nums) {
            int currentCount = 1;

            int target = num + 1;
            while (numsSet.contains(target)) {
                currentCount += 1;

                target += 1;
            }

            target = num - 1;
            while (numsSet.contains(target)) {
                currentCount += 1;

                target -= 1;
            }

            result = Math.max(result, currentCount);
        }

        return result;
    }

    // time complexity: O(3n) = O(n)
    public int longestConsecutive2(int[] nums) {
        Set<Integer> numsSet = new HashSet<>();
        for (int num : nums)
            numsSet.add(num);

        List<Integer> maxValues = new LinkedList<>();

        for (int num : nums) {
            if (numsSet.contains(num - 1))
                continue;

            maxValues.add(num);
        }

        int result = 0;

        for (int i = 0; i < maxValues.size(); i++) {
            int currentCount = 0;

            int target = maxValues.get(i);
            while (numsSet.contains(target)) {
                currentCount += 1;

                target += 1;
            }

            result = Math.max(result, currentCount);
        }

        return result;
    }
}

/*
 * Even though the second method has a time complexity of O(n), the LeetCode
 * system is returning a "Time Limit Exceeded" message. :( I understand getting
 * a "Time Limit Exceeded" message for the first method since its time
 * complexity is O(n^2), but the second method should be accepted. :(
 */