// 134. Gas Station
// https://leetcode.com/problems/gas-station/

/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */

// Time Limit Exceeded. :(
// time complexity: O(n^2)
var canCompleteCircuit = function (gas, cost) {
  let possibleStartPoint = -1;

  for (i = 0; i < gas.length; i++) {
    if (gas[i] < cost[i]) continue;
    if (gas[i] === 0) continue;

    let current = i;
    let currentGas = 0;

    for (j = 0; j < gas.length; j++) {
      currentGas += gas[current];

      currentGas -= cost[current];
      current += 1;

      if (current === gas.length) current = 0;
      if (currentGas < 0) break;
      if (current === i) possibleStartPoint = i;
    }
  }

  return possibleStartPoint;
};
