// 2300. Successful Pairs of Spells and Potions
// https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

import java.util.Arrays;

// time complexity: O(m log m + n * log m) = O((n + m) log n)
// space complexity: O(m + n) = O(n + m)
class Solution {
    int[] potions;
    long success;

    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int[] sortedPotions = Arrays.copyOf(potions, potions.length);
        Arrays.sort(sortedPotions);
        this.potions = sortedPotions;
        this.success = success;

        int[] result = new int[spells.length];

        for (int i = 0; i < spells.length; i++) {
            result[i] = this.getCountSuccessfulPair(spells[i]);
        }

        return result;
    }

    private int getCountSuccessfulPair(int targetSpell) {
        int left = 0;
        int right = this.potions.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            long currentValue = (long) targetSpell * this.potions[mid];

            if (currentValue >= this.success) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return this.potions.length - left;
    }
}

/*
 * When multiplying two "int" values, the calculation is first performed within
 * the "int" range, and only then is the result converted to "long". This can
 * lead to an overflow if the product exceeds the "int" limit. To prevent this,
 * one of the operands must be explicitly cast to "long" before multiplication.
 * 
 * Wrong: long currentValue = targetSpell * this.potions[mid];
 * -> May cause overflow
 * Correct: long currentValue = (long) targetSpell * this.potions[mid];
 */