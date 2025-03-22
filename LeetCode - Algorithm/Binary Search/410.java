// 410. Split Array Largest Sum
// https://leetcode.com/problems/split-array-largest-sum/

// time complexity: O(n + n * log (sum - max)) = O(n log (sum - max))
// space complexity: O(1)
class Solution {
    int[] nums;
    int k;

    public int splitArray(int[] nums, int k) {
        this.nums = nums;
        this.k = k;

        int maxValue = 0;
        int sumValue = 0;

        for (int num : nums) {
            maxValue = Math.max(maxValue, num);
            sumValue += num;
        }

        int left = maxValue;
        int right = sumValue;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (this.isPossibleToSplitLessThan(mid)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    private boolean isPossibleToSplitLessThan(int value) {
        int currentSum = 0;
        int numGroup = 1;

        for (int num : this.nums) {
            currentSum += num;

            if (currentSum > value) {
                currentSum = num;
                numGroup += 1;
            }
        }

        if (numGroup > this.k)
            return false;

        return true;
    }
}

/*
 * This problem is really challenging. The idea of setting the maximum value in
 * the array as the initial left and the sum of all values in the array as the
 * initial right is a fascinating perspective. Moreover, the approach of using
 * binary search to continuously check whether a value is possible and find the
 * minimum possible value is even more impressive.
 */

/*
 * The way we calculate time complexity is important here. In binary search, the
 * time complexity is log(the number of possible values within the search
 * range). So, instead of habitually using log n, we should use log(sum - max)
 * in this case. Also, don't forget that since the function is repeatedly called
 * inside the while loop, it gets multiplied by n.
 */