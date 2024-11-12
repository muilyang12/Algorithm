class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int sum = 0;
        double maxAverage = 0.0;

        int left = 0;
        int right = k - 1;

        for (int i = 0; i < k; i++) {
            sum += nums[i];
        }
        maxAverage = ((double) sum) / k;

        left += 1;
        right += 1;

        while (right < nums.length) {
            sum -= nums[left - 1];
            sum += nums[right];
            maxAverage = Math.max(maxAverage, ((double) sum) / k);

            left += 1;
            right += 1;
        }

        return maxAverage;
    }
}