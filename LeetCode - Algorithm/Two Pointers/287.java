// 287. Find the Duplicate Number
// https://leetcode.com/problems/find-the-duplicate-number/

// time complexity: O(n)
// space complexity: O(1)
class Solution {
    public int findDuplicate(int[] nums) {
        int slow = 0;
        int fast = 0;

        slow = nums[slow];
        fast = nums[fast];
        fast = nums[fast];

        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
            fast = nums[fast];
        }

        int target = 0;

        while (target != slow) {
            slow = nums[slow];
            target = nums[target];
        }

        return target;
    }
}

/*
 * Sadly, this question is more about memorizing the process. The distance from
 * the start of the graph to the beginning of the cycle is the same as the
 * distance from the start of the cycle to the point where the fast and slow
 * pointers intersect. So, we will use two pointers, slow and fast, to find the
 * intersection point. This step is key to determining the starting location of
 * the cycle.
 * 
 * So, to get familiar with the concept of Floyd's cycle detection, I should
 * probably solve this question multiple times.
 */