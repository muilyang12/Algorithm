// 322. Coin Change
// https://leetcode.com/problems/coin-change/

/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */

// Divide-and-conquer (Depth First Search (DFS))
// time complexity: O(n^m) || space complexity: O(m) (n: number of coins, m: amount)
var coinChange = function (coins, amount) {
  const dfs = (amountRest) => {
    let result = Infinity;

    if (amountRest === 0) return 0;
    if (amountRest < 0) return -1;

    for (let i = 0; i < coins.length; i++) {
      let tempResult = dfs(amountRest - coins[i]);
      if (tempResult === -1) continue;

      result = Math.min(result, tempResult + 1);
    }

    return result;
  };

  const result = dfs(amount);

  return result < Infinity ? result : -1;
};
