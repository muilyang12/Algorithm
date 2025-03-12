// 72. Edit Distance
// https://leetcode.com/problems/edit-distance/

// Time Limit Exceeded :(
// time complexity: O(3^(m + n))
class Solution1 {
    String word1;
    String word2;

    public int minDistance(String word1, String word2) {
        this.word1 = word1;
        this.word2 = word2;

        return getDistance(0, 0);
    }

    private int getDistance(int index1, int index2) {
        if (index1 == this.word1.length() && index2 == this.word2.length())
            return 0;

        if (index1 == this.word1.length())
            return 1 + getDistance(index1, index2 + 1);

        if (index2 == this.word2.length())
            return 1 + getDistance(index1 + 1, index2);

        if (word1.charAt(index1) == word2.charAt(index2))
            return getDistance(index1 + 1, index2 + 1);

        int afterInsert = 1 + getDistance(index1, index2 + 1);
        int afterDelete = 1 + getDistance(index1 + 1, index2);
        int afterReplace = 1 + getDistance(index1 + 1, index2 + 1);

        return Math.min(Math.min(afterInsert, afterDelete), afterReplace);
    }
}

class Solution2 {
    public int minDistance(String word1, String word2) {
        int[][] memo = new int[word1.length() + 1][word2.length() + 1];

        for (int i = 0; i < word1.length() + 1; i++) {
            memo[i][word2.length()] = word1.length() - i;
        }

        for (int j = 0; j < word2.length() + 1; j++) {
            memo[word1.length()][j] = word2.length() - j;
        }

        for (int i = word1.length() - 1; i >= 0; i--) {
            for (int j = word2.length() - 1; j >= 0; j--) {
                if (word1.charAt(i) == word2.charAt(j)) {
                    memo[i][j] = memo[i + 1][j + 1];

                    continue;
                }

                int afterInsert = 1 + memo[i][j + 1];
                int afterDelete = 1 + memo[i + 1][j];
                int afterReplace = 1 + memo[i + 1][j + 1];

                memo[i][j] = Math.min(afterInsert, Math.min(afterDelete, afterReplace));
            }
        }

        return memo[0][0];
    }
}

// word1 = "horse"
// word2 = "ros"

/*
 * ___r__o__s
 * h [0, 0, 0, 5]
 * o [0, 0, 0, 4]
 * r [0, 0, 2, 3]
 * s [0, 0, 1, 2]
 * e [0, 0, 1, 1]
 * __[3, 2, 1, 0]
 */