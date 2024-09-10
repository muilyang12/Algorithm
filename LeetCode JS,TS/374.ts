// 374. Guess Number Higher or Lower
// https://leetcode.com/problems/guess-number-higher-or-lower/

// Divide-and-conquer - Recursive
// time complexity: O(logn) || space complexity: O(1)
function guessNumber(n: number): number {
  let left = 1;
  let right = n;

  let mid;

  while (left <= right) {
    mid = Math.floor((left + right) / 2);

    if (guess(mid) === 0) {
      return mid;
    } else if (guess(mid) === 1) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return 0;
}

function guess(num: number): number {
  return 1;
}
