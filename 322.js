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
  queue.push([0, 0]);

  while (queue.length > 0) {
    const [count, total] = queue.shift();

    if (total === amount) return count;

    for (let i = 0; i < coins.length; i++) {
      const newTotal = total + coins[i];
      if (newTotal > amount) continue;

      queue.push([count + 1, newTotal]);
    }
  }

  return -1;
};

// Dynamic Programming + BFS
var coinChange3 = function (coins, amount) {
  const memo = new Set();

  const queue = [];
  queue.push([0, 0]); // count, currentTotal

  while (queue.length > 0) {
    const [count, currentTotal] = queue.shift();

    if (currentTotal === amount) return count;

    if (memo.has(currentTotal)) continue;
    else memo.add(currentTotal);

    let newTotal;
    coins.forEach((coin) => {
      newTotal = currentTotal + coin;

      if (newTotal <= amount) {
        queue.push([count + 1, newTotal]);
      }
    });
  }

  return -1;
};
