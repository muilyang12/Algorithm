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

/*
 * In Java, the 'int' type can store values ranging from -2,147,483,648 to
 * 2,147,483,647 (Roughly -2 × 10^9 to 2 × 10^9).
 * 
 * In this problem, the constraints for element values are 1 <= piles[i] <=
 * 10^9, meaning that adding or subtracting just two or three such values can
 * exceed the 'int' range. Therefore, I need to use the 'long' type for variable
 * hours in this problem. I must be cautious when performing arithmetic
 * operations in Java and check the constraints.
 */