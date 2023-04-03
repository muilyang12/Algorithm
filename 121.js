// 121. Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

/**
 * @param {number[]} prices
 * @return {number}
 */

// Brute Force
// time complexity: O(n^2) || space complexity: O(1)
var maxProfit1 = function (prices) {
  const length = prices.length;

  let profit = 0;

  for (let i = 0; i < length; i++) {
    for (let j = i + 1; j < length; j++) {
      profit = Math.max(prices[j] - prices[i], profit);
    }
  }

  return profit;
};

// time complexity: O(n) || space complexity: O(1)
var maxProfit2 = function (prices) {
  let memo = 99999;
  let max = 0;

  for (let i = 0; i < prices.length; i++) {
    if (prices[i] < memo) {
      memo = prices[i];
    } else {
      max = Math.max(max, prices[i] - memo);
    }
  }

  return max;
};
