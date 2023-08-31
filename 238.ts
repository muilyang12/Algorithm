// 238. Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/

function productExceptSelf1(nums: number[]): number[] {
  return nums.map((num, index) => {
    let result = 1;

    for (let j = 0; j < nums.length; j++) {
      if (index !== j) {
        result *= nums[j];
      }
    }

    return result;
  });
}

function productExceptSelf2(nums: number[]): number[] {
  const memo: number[] = [];

  return nums.map((num, index) => {
    let result = 1;

    if (index - 1 >= 0 && memo[index - 1]) {
      result *= memo[index - 1];

      for (let i = index + 1; i < nums.length; i++) {
        result *= nums[i];
      }
    } else {
      let valueToMemo = 1;
      for (let i = 0; i <= index - 1; i++) {
        valueToMemo *= nums[i];
      }

      memo[index - 1] = valueToMemo;

      result *= memo[index - 1];

      for (let i = index + 1; i < nums.length; i++) {
        result *= nums[i];
      }
    }

    return result;
  });
}
