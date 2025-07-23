// 15. 3Sum
// https://leetcode.com/problems/3sum/

function threeSum(nums: number[]): number[][] {
  const sortedNums = nums.sort((a, b) => a - b);

  const checker = new Set<string>();
  const result: number[][] = [];

  for (let i = 0; i < nums.length - 2; i++) {
    let left = i + 1;
    let right = sortedNums.length - 1;

    while (left < right) {
      if (sortedNums[i] + sortedNums[left] + sortedNums[right] == 0) {
        const key = `${sortedNums[i]},${sortedNums[left]},${sortedNums[right]}`;

        if (!checker.has(key)) {
          checker.add(key);
          result.push([sortedNums[i], sortedNums[left], sortedNums[right]]);
        }

        left += 1;
        right -= 1;
      } else if (sortedNums[i] + sortedNums[left] + sortedNums[right] < 0) {
        left += 1;
      } else {
        right -= 1;
      }
    }
  }

  return result;
}

// 이건 조금 어렵네.
