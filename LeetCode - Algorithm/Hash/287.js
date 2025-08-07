// 287. Find the Duplicate Number
// https://leetcode.com/problems/find-the-duplicate-number/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function (nums) {
  const numsSet = new Set();

  for (let num of nums) {
    if (numsSet.has(num)) return num;

    numsSet.add(num);
  }
};
