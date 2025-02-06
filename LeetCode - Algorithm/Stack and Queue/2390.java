// 2390. Removing Stars From a String
// https://leetcode.com/problems/removing-stars-from-a-string/

class Solution {
    public String removeStars(String s) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != '*') {
                sb.append(s.charAt(i));
            } else {
                sb.deleteCharAt(sb.length() - 1);
            }
        }

        return sb.toString();
    }
}

// leet**cod*e
// ^

/*
 * When building strings in Java, using StringBuilder is generally the best
 * approach.
 * 
 * StringBuilder sb = new StringBuilder(); // Default capacity of 16
 * StringBuilder sb = new StringBuilder(10); // Specified initial capacity of 16
 * 
 * When you append characters to a StringBuilder and its current capacity is
 * exceeded, Java automatically increases the capacity to accommodate the
 * additional characters.
 * 
 * sb.append("Hello !!");
 * sb.insert(5, " World");
 * sb.replace();
 * sb.delete();
 * sb.deleteCharAt();
 */