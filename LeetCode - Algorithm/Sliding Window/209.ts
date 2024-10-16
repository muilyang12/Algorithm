// 209. Minimum Size Subarray Sum
// https://leetcode.com/problems/minimum-size-subarray-sum/

function minSubArrayLen(target: number, nums: number[]): number {
  let result = Number.POSITIVE_INFINITY;

  let left = 0;
  let right = 0;

  let currentSum = nums[right];

  while (right < nums.length) {
    if (currentSum < target) {
      right += 1;
      currentSum += nums[right];
    } else {
      result = Math.min(result, right - left + 1);

      currentSum -= nums[left];
      left += 1;
    }
  }

  return result < Number.POSITIVE_INFINITY ? result : 0;
}

`
Subarray: a contiguous non-empty sequence of elements within an array. -> The elements should be contiguous.

The question asks to find a subarray. Since subarray means contiguous elements, sliding window is a perfect solution.
And, I can maintain a variable for the sum, adding the right pointer value and subtracting the left pointer value.
`;

`
target = 7, nums = [2,3,1,2,4,3]
                    ^
`;
