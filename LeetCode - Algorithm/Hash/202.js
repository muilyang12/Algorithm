// 202. Happy Number
// https://leetcode.com/problems/happy-number/

/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function (n) {
  const hash = {};

  let currentTarget = String(n);

  while (!hash[currentTarget]) {
    const digitSquareSum = getDigitSquareSum(currentTarget);
    if (digitSquareSum == 1) return true;

    hash[currentTarget] = digitSquareSum;

    currentTarget = digitSquareSum;
  }

  return false;
};

var getDigitSquareSum = (numberStr) => {
  let result = 0;

  for (let i = 0; i < numberStr.length; i++) result += Number(numberStr[i]) ** 2;

  return String(result);
};

// 2 -> 4 -> 16 -> 37 -> 58 (9 + 49) -> 89 (25 + 64) -> 145 (64 + 81) -> 42 (1 + 16 + 25) -> 20 -> 4
