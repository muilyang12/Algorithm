// 46. Permutations
// https://leetcode.com/problems/permutations/

import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<Integer> numsList = new ArrayList<>();
        for (int num : nums) {
            numsList.add(num);
        }

        return this.generateAllCases(numsList);
    }

    private List<List<Integer>> generateAllCases(List<Integer> nums) {
        if (nums.size() == 1) {
            List<List<Integer>> result = new ArrayList<>();
            result.add(new ArrayList<>(Arrays.asList(nums.get(0))));

            return result;
        }

        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < nums.size(); i++) {
            int targetValue = nums.get(i);
            nums.remove(i);

            List<List<Integer>> nextResults = this.generateAllCases(nums);

            for (List<Integer> nextResultElem : nextResults) {
                nextResultElem.add(0, targetValue);
                result.add(nextResultElem);
            }

            nums.add(i, targetValue);
        }

        return result;
    }
}

/*
 * [1,2,3]
 * - 1, [2,3]
 * --- 1, 2, [3]
 * --- 1, 3, [2]
 * - 2, [1,3]
 * --- ...
 * - 3, [1,2]
 * --- ...
 */

/*
 * Arrays.asList() returns a fixed-size list, meaning I cannot add or remove
 * elements from it. But I can modify existing elements using set().
 * 
 * List.of() returns an immutable list, meaning I cannot add, remove, or modify
 * elements. Any attempt to change the list will result in an error.
 * 
 * Therefore, if I want to create a list with initial values that can be
 * modified, I should use new ArrayList<>(Arrays.asList()).
 */