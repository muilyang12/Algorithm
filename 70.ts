// 70. Climbing Stairs
// https://leetcode.com/problems/climbing-stairs/


// Dynamic Programming
// time complexity: O(n) || space complexity: O(n)
function climbStairs(n: number): number {
  let result = 0;

  const dp: number[] = [];
  dp[0] = null;
  dp[1] = 1;
  dp[2] = 2;

  for (let i = 3; i < n + 1; i++) {
      dp[i] = dp[i - 1] + dp[i - 2];
  }

  result = dp[n];

  return result;
};
