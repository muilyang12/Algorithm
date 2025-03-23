// 279. Perfect Squares
// https://leetcode.com/problems/perfect-squares/

// time complexity: O(n * root(n))
// space complexity: O(n)
class Solution {
    public int numSquares(int n) {
        int[] memo = new int[n + 1];

        for (int i = 1; i < n + 1; i++) {
            int current = 1;

            while (0 <= i - Math.pow(current, 2)) {
                memo[i] = memo[i] > 0 ? Math.min(memo[i], memo[i - (int) Math.pow(current, 2)] + 1)
                        : memo[i - (int) Math.pow(current, 2)] + 1;

                current += 1;
            }
        }

        return memo[n];
    }
}

// n = 12
//
// [0, 1, 2, 3, 1, 2, 0, 0, 0, 0, 0, 0, 0]
// i = 5
// current = 2

/*
 * It is impressive that the time complexity of this algorithm includes
 * root(n). This is because the line "while (0 <= i - Math.pow(current, 2))"
 * makes roughly root(n) iterations. The variable "current" increases by 1 until
 * current^2 > n, so the number of repetitions is approximately root(n).
 */