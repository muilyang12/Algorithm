// 20. Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

// Stack
// time complexity: O(n) || space complexity: O(n)
function isValid(s: string): boolean {
  const parenthesesToNum = {
    "(": 1,
    "{": 2,
    "[": 3,
    ")": 4,
    "}": 5,
    "]": 6,
  };
  const stack: number[] = [];

  for (let i = 0; i < s.length; i++) {
    const num = parenthesesToNum[s[i]];

    if (num <= 3) {
      stack.push(num);

      continue;
    }

    const last = stack.pop();
    if (last !== num - 3) return false;
  }

  if (stack.length > 0) return false;

  return true;
}
