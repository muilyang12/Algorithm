// 322. Coin Change
// https://leetcode.com/problems/coin-change/

/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */

// Divide-and-conquer (Depth First Search (DFS))
// time complexity: O(n^m) || space complexity: O(m) (n: number of coins, m: amount)
var coinChange1 = function (coins, amount) {
  const dfs = (amountReft) => {
    let result = Infinity;

    if (amountReft === 0) return 0;
    if (amountReft < 0) return -1;

    for (let i = 0; i < coins.length; i++) {
      let tempResult = dfs(amountReft - coins[i]);
      if (tempResult === -1) continue;

      result = Math.min(result, tempResult + 1);
    }

    return result;
  };

  const result = dfs(amount);

  return result < Infinity ? result : -1;
};

// Breadth First Search (BFS) // Queue
var coinChange2 = function (coins, amount) {
  const queue = [];

  while (queue.length > 0) {
    const [count, total] = queue.shift();
  }
};
