// 1011. Capacity To Ship Packages Within D Days
// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

// time complexity: O(n + n * log (sum - max)) = O(n * log (sum - max))
// space complexity: O(1)
class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int maxWeight = 0;
        int totalWeight = 0;

        for (int weight : weights) {
            maxWeight = Math.max(maxWeight, weight);
            totalWeight += weight;
        }

        int left = maxWeight;
        int right = totalWeight;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (this.isPossibleToShip(mid, weights, days)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    private boolean isPossibleToShip(int capacity, int[] weights, int days) {
        int currentWeight = 0;
        int currentDays = 1;

        for (int weight : weights) {
            currentWeight += weight;

            if (currentWeight > capacity) {
                currentWeight = weight;
                currentDays += 1;
            }
        }

        if (currentDays > days)
            return false;

        return true;
    }
}

/*
 * I didn't intentionally solve these two problems in a row, but the approach
 * and structure of the solution are exactly the same as the one used in the
 * "410. Split Array Largest Sum" problem.
 */