// 15. 3Sum
// https://leetcode.com/problems/3sum/

// Brute Force
// time complexity: O(n^3) || space complexity: O(1)
function threeSum1(nums: number[]): number[][] {
  const result: number[][] = [];
  const added = new Set();

  const length = nums.length;
  for (let i = 0; i < length - 2; i++) {
    for (let j = i + 1; j < length - 1; j++) {
      for (let k = j + 1; k < length; k++) {
        if (nums[i] + nums[j] + nums[k] === 0) {
          const answer = [nums[i], nums[j], nums[k]].sort((a, b) => a - b);
        
          if (!added.has(answer.join(""))) {
            result.push(answer);
            added.add(answer.join(""));
          }
        }
      }
    }
  }

  return result;
}

function threeSum2(nums: number[]): number[][] {
  const result: number[][] = [];
  const added = new Set();

  const length = nums.length;
  for (let i = 0; i < length - 2; i++) {
    const history = new Set();

    for (let j = i + 1; j < length - 1; j++) {
      const complement = 0 - (nums[i] + nums[j]);

      if (history.has(complement)) {
        const answer = [nums[i], complement, nums[j]];

        if (!added.has(answer.join(""))) {
          result.push(answer);
          added.add(answer.join(""));
        }
      } else {
        history.add(nums[j]);
      }
    }
  }

  return result;
}

// Sorting + Two Pointer
// time complexity: O(2 * n^2) = O(n^2) || space complexity: O(1)
function threeSum3(nums: number[]): number[][] {
  const result: number[][] = [];
  const added = new Set();

  const copiedNums = [...nums];
  const sortedNums = copiedNums.sort((a, b) => a - b);

  for (let i = 0; i < sortedNums.length - 2; i++) {
    let left = i + 1;
    let right = sortedNums.length - 1;

    while (left < right) {
      const complement = 0 - sortedNums[i];

      if (sortedNums[left] + sortedNums[right] < complement) {
        left += 1;
      } else if (sortedNums[left] + sortedNums[right] > complement) {
        right -= 1;
      } else {
        const answer = [sortedNums[i], sortedNums[left], sortedNums[right]];

        if (!added.has(answer.join(""))) {
          result.push(answer);
          added.add(answer.join(""));

          break;
        }
      }
    }
  }

  return result;
}
