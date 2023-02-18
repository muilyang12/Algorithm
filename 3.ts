// 3. Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

// time complexity: O(n^3) || space complexity: O(n)
function lengthOfLongestSubstring1(s: string): number {
  let result = s.length > 0 ? 1 : 0;

  for (let i = 0; i < s.length; i++) {
    for (let j = i + 1; j < s.length; j++) {
      const string = s.slice(i, j + 1);
      const set = new Set(string); // -> O(n)

      if (string.length === set.size) {
        result = Math.max(result, string.length);
      }
    }
  }

  return result;
}

// time complexity: O(n^2) || space complexity: O(n)
function lengthOfLongestSubstring2(s: string): number {
  let result = 0;

  for (let i = 0; i < s.length; i++) {
    const set = new Set(s[i]);
    result = Math.max(result, set.size);

    for (let j = i + 1; j < s.length; j++) {
      if (set.has(s[j])) break; // -> O(1)

      set.add(s[j]); // -> O(1)
      result = Math.max(result, set.size);
    }
  }

  return result;
}

// Sliding Window
function lengthOfLongestSubstring3(s: string): number {
  let result = 0;

  return result;
}
