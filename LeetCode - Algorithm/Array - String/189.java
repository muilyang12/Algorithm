// 189. Rotate Array
// https://leetcode.com/problems/rotate-array/

class Solution {
    // Time Limit Exceeded :(
    public void rotate1(int[] nums, int k) {
        int numElementsToRotate = k % nums.length;
        int firstElementToMove = nums.length - numElementsToRotate;

        for (int i = firstElementToMove; i > 0; i--) {
            int temp = nums[i - 1];

            for (int j = 0; j < numElementsToRotate; j++) {
                nums[i + j - 1] = nums[i + j];
            }

            nums[i + numElementsToRotate - 1] = temp;
        }
    }

    public void rotate2(int[] nums, int k) {
        int numElementsToRotate = k % nums.length;

        this.reverse(nums, 0, nums.length - 1);
        this.reverse(nums, 0, numElementsToRotate - 1);
        this.reverse(nums, numElementsToRotate, nums.length - 1);

    }

    public void reverse(int[] nums, int from, int to) {
        int left = from;
        int right = to;

        while (left < right) {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;

            left += 1;
            right -= 1;
        }
    }
}