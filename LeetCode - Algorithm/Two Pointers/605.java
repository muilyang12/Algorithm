// 605. Can Place Flowers
// https://leetcode.com/problems/can-place-flowers/

class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int rest = n;

        int current = 0;

        while (current < flowerbed.length) {
            if ((current - 1 < 0 || flowerbed[current - 1] == 0)
                    && flowerbed[current] == 0
                    && (current + 1 >= flowerbed.length || flowerbed[current + 1] == 0)) {
                rest -= 1;
            }

            current += 1;
        }

        if (rest <= 0) {
            return true;
        } else {
            return false;
        }
    }
}