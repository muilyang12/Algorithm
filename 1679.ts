// 1679. Max Number of K-Sum Pairs
// https://leetcode.com/problems/max-number-of-k-sum-pairs/

// Two Pointers
// time complexity: O(nlogn) || space complexity: O(n)
function maxOperations(nums: number[], k: number): number {
  let result = 0;

  const copiedNums = [...nums];
  copiedNums.sort((a, b) => (a > b ? 1 : -1));

  let left = 0;
  let right = copiedNums.length - 1;

  while (left < right) {
    const sum = copiedNums[left] + copiedNums[right];

    if (sum > k) {
      right -= 1;
    } else if (sum < k) {
      left += 1;
    } else {
      result += 1;

      left += 1;
      right -= 1;
    }
  }

  return result;
}
