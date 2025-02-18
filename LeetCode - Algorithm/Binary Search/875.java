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

/*
 * In Java, when performing int / int division, the decimal part is always
 * truncated (discarded)
 * 
 * System.out.println(7 / 3); // -> Output: 2
 * 
 * So, if I want a floating-point result after division, you need to convert at
 * least one operand to double.
 * 
 * System.out.println((double) 7 / 3); // Output: 2.3333333333333335
 */