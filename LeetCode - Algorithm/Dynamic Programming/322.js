// 322. Coin Change
// https://leetcode.com/problems/coin-change/

/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
  const memo = Array(amount + 1).fill(Number.POSITIVE_INFINITY);
  memo[0] = 0;

  for (let i = 0; i < amount + 1; i++) {
    coins.forEach((coin) => {
      if (i - coin < 0) return;

      memo[i] = Math.min(memo[i], memo[i - coin] + 1);
    });
  }

  if (!Number.isFinite(memo[memo.length - 1])) return -1;
  else return memo[memo.length - 1];
};
