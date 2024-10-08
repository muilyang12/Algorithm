// 121. Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let buyingPrice = Number.POSITIVE_INFINITY;
  let profit = Number.NEGATIVE_INFINITY;

  for (let i = 0; i < prices.length; i++) {
    if (prices[i] < buyingPrice) buyingPrice = prices[i];
    else profit = Math.max(profit, prices[i] - buyingPrice);
  }

  if (profit < 0) return 0;
  else return profit;
};
