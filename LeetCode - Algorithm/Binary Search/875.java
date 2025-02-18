// 875. Koko Eating Bananas
// https://leetcode.com/problems/koko-eating-bananas/

class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1;
        int right = -1;

        for (int pile : piles) {
            right = Math.max(right, pile);
        }

        while (left <= right) {
            int mid = (left + right) / 2;

            long hours = 0;

            for (int pile : piles) {
                int quotient = (int) Math.ceil((double) pile / mid);
                hours += quotient;
            }

            if (hours > h) {
                left = mid + 1;
            } else if (hours <= h) {
                right = mid - 1;
            }
        }

        return left;
    }
}