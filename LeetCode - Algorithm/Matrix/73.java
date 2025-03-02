// 73. Set Matrix Zeroes
// https://leetcode.com/problems/set-matrix-zeroes/

import java.util.Set;
import java.util.HashSet;

class Solution {
    public void setZeroes(int[][] matrix) {
        Set<Integer> rows = new HashSet<>();
        Set<Integer> cols = new HashSet<>();

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    rows.add(i);
                    cols.add(j);
                }
            }
        }

        for (int row : rows)
            for (int j = 0; j < matrix[0].length; j++)
                matrix[row][j] = 0;

        for (int col : cols)
            for (int i = 0; i < matrix.length; i++)
                matrix[i][col] = 0;
    }
}
