// 17. Letter Combinations of a Phone Number
// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

class Solution {
    Map<Integer, String[]> numberCharMap;

    public Solution() {
        this.numberCharMap = new HashMap<>();
        this.numberCharMap.put(2, new String[] { "a", "b", "c" });
        this.numberCharMap.put(3, new String[] { "d", "e", "f" });
        this.numberCharMap.put(4, new String[] { "g", "h", "i" });
        this.numberCharMap.put(5, new String[] { "j", "k", "l" });
        this.numberCharMap.put(6, new String[] { "m", "n", "o" });
        this.numberCharMap.put(7, new String[] { "p", "q", "r", "s" });
        this.numberCharMap.put(8, new String[] { "t", "u", "v" });
        this.numberCharMap.put(9, new String[] { "w", "x", "y", "z" });
    }

    public List<String> letterCombinations(String digits) {
        if (digits.length() < 1)
            return Arrays.asList();

        return this.generateAllCases(digits.toCharArray(), 0, digits.length() - 1);
    }

    public List<String> generateAllCases(char[] digits, int from, int to) {
        if (from == to)
            return Arrays.asList(this.numberCharMap.get(Integer.parseInt(String.valueOf(digits[from]))));

        String[] currentChars = this.numberCharMap.get(Integer.parseInt(String.valueOf(digits[from])));

        List<String> result = new ArrayList<>();

        List<String> nextResults = this.generateAllCases(digits, from + 1, to);

        for (String character : currentChars) {
            for (String res : nextResults) {
                result.add(character + res);
            }
        }

        return result;
    }
}

// digits = "23"

/*
 * In Java,
 * 
 * 1. Array Initialization
 * int[] arr1 = {1, 2, 3};
 * int[] arr2 = new int[]{1, 2, 3};
 * 
 * The "new" keyword is required when initializing an array with values unless
 * it's part of a declaration.
 * 
 * int[] arr3;
 * arr3 = {1, 2, 3}; // Wrong
 * 
 * int[] arr3;
 * arr4 = new int[]{1, 2, 3}; // Okay
 * 
 * hash.put(1, { 'a', 'b', 'c' }); // Wrong
 * 
 * hash.put(1, new char[] { 'a', 'b', 'c' }); // Okay
 * 
 * 
 * 
 * 2. List Initialization
 * 
 * - Mutable List
 * List<Integer> mutableList = new ArrayList<>(Arrays.asList(1, 2, 3));
 * 
 * - Immutable List
 * List<Integer> immutableList = List.of(1, 2, 3);
 * 
 * 
 * 
 * 3. Set Initialization
 * 
 * - Mutable Set
 * Set<Integer> mutableSet = new HashSet<>(Arrays.asList(1, 2, 3));
 * 
 * - Immutable Set
 * Set<Integer> immutableSet = Set.of(1, 2, 3);
 * 
 * 
 * 
 * 4. Map Initialization
 * Unlike Python, Java does not have direct dictionary literals.
 * 
 * - Mutable Map
 * Map<String, Integer> mutableMap = new HashMap<>();
 * mutableMap.put("a", 1);
 * mutableMap.put("b", 2);
 * mutableMap.put("c", 3);
 * 
 * - Immutable Map
 * Map<String, Integer> immutableMap = Map.of("a", 1, "b", 2);
 */

/*
 * public void processArray(int[] numbers)
 * -> processArray(new int[]{1, 2, 3});
 * 
 * public void processList(List<Integer> numbers)
 * -> processList(Arrays.asList(4, 5, 6));
 * 
 * public void processSet(Set<String> items)
 * -> processSet(new HashSet<>(Arrays.asList("A", "B", "C")));
 * 
 * public void processMap(Map<String, Integer> map)
 * -> Impossible to use with Mutable Map.
 */