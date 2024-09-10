// 5. Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/

// Brute Force
// time complexity: O(n^2 * n) = O(n^3) || space complexity: O(1)
function longestPalindrome1(s: string): string {
  function isPalindromic(s: string) {
    const count = Math.floor(s.length / 2);

    for (let i = 0; i < count; i++) {
      if (s[i] !== s[s.length - 1 - i]) return false;
    }

    return true;
  }

  let length = 0;
  let result = "";

  for (let i = 0; i < s.length; i++) {
    for (let j = i; j < s.length; j++) {
      const targetString = s.slice(i, j + 1);

      if (isPalindromic(targetString)) {
        result = targetString.length > length ? targetString : result;
        length = result.length;
      }
    }
  }

  return result;
}

// time complexity: O(n * 2n) = O(n^2) || space complexity: O(1)
function longestPalindrome2(s: string): string {
  let result = "";

  let front: number;
  let rear: number;

  for (let i = 0; i < s.length; i++) {
    front = i;
    rear = i;

    while (front >= 0 && rear <= s.length - 1 && s[front] === s[rear]) {
      if (rear - front + 1 > result.length) {
        result = s.slice(front, rear + 1);
      }

      front -= 1;
      rear += 1;
    }

    front = i;
    rear = i + 1;

    while (front >= 0 && rear <= s.length - 1 && s[front] === s[rear]) {
      const targetString = s.slice(front, rear + 1);

      if (rear - front + 1 > result.length) {
        result = s.slice(front, rear + 1);
      }

      front -= 1;
      rear += 1;
    }
  }

  return result;
}
