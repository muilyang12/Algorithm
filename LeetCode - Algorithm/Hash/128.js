// 128. Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  let result = 0;

  const numsSet = new Set(nums);

  for (let i = 0; i < nums.length; i++) {
    if (numsSet.has(nums[i] - 1)) continue;

    let currentNum = nums[i];
    let currentCount = 0;
    while (numsSet.has(currentNum)) {
      currentCount += 1;
      currentNum += 1;
    }

    result = Math.max(result, currentCount);
  }

  return result;
};

`
nums = [100,4,200,1,3,2]

1, 2, 3, 4, 100, 200
`;
