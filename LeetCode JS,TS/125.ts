// 125. Valid Palindrome
// https://leetcode.com/problems/valid-palindrome/

// Two Pointers
// time complexity: O(2n) = O(n) || space complexity: O(2n) = O(n)
function isPalindrome(s: string): boolean {
  const alphanumeric = Array.from("abcdefghijklmnopqrstuvwxyz0123456789");

  const lowerCasedString = s.toLowerCase();
  const filteredString = Array.from(lowerCasedString).filter((letter) =>
    alphanumeric.includes(letter)
  );

  let left = 0;
  let right = filteredString.length - 1;

  while (left < right) {
    if (filteredString[left] !== filteredString[right]) return false;

    left += 1;
    right -= 1;
  }

  return true;
}
