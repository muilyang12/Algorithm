// 70. Climbing Stairs
// https://leetcode.com/problems/climbing-stairs/

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  const memo = [];
  for (let i = 0; i < n + 1; i++) memo.push(0);

  memo[1] = 1;
  memo[2] = 2;

  for (let i = 3; i < n + 1; i++) {
    memo[i] = memo[i - 1] + memo[i - 2];
  }

  return memo[n];
};

/*
n = 3
[0, 1, 1, 2]
*/
