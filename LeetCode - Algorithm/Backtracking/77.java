// 77. Combinations
// https://leetcode.com/problems/combinations/

import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

class Solution {
    int n;
    int k;

    public List<List<Integer>> combine(int n, int k) {
        this.n = n;
        this.k = k;

        List<List<Integer>> result = new ArrayList<>();

        List<Integer> initialCurrent = new ArrayList<>();
        Set<Integer> initialUsedNumber = new HashSet<>();

        this.generateAllCases(result, initialCurrent, initialUsedNumber);

        return result;
    }

    private void generateAllCases(List<List<Integer>> result, List<Integer> current, Set<Integer> usedNumber) {
        if (current.size() == this.k) {
            result.add(new ArrayList<>(current));

            return;
        }

        int startValue = current.size() > 0 ? current.get(current.size() - 1) : 1;

        for (int i = startValue; i <= this.n; i++) {
            if (usedNumber.contains(i))
                continue;

            current.add(i);
            usedNumber.add(i);
            this.generateAllCases(result, current, usedNumber);
            current.remove(current.size() - 1);
            usedNumber.remove(i);
        }
    }
}

// Input: n = 4, k = 2
// Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]