// 70. Climbing Stairs
// https://leetcode.com/problems/climbing-stairs/


// Dynamic Programming
// time complexity: O(n) || space complexity: O(n)
function climbStairs1(n: number): number {
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

// Dynamic Programming
// time complexity: O(n) || space complexity: O(2) = O(1)
function climbStairs2(n: number): number {
    let dpVar01 = 1;
    let dpVar02 = 2;

    for (let i = 3; i < n + 1; i++) {
        const tempResult = dpVar01 + dpVar02;

        dpVar01 = dpVar02;
        dpVar02 = tempResult;
    }

    if (n < 3) return n;
    else  return dpVar02;
};
