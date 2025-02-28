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
