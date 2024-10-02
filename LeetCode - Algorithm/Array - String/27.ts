// 27. Remove Element
// https://leetcode.com/problems/remove-element/

function removeElement(nums: number[], val: number): number {
  let result = 0;

  let current = 0;

  let destination = -1;

  while (current < nums.length) {
    const num = nums[current];

    if (num !== val) result += 1;

    if (num === val && destination < 0) {
      destination = current;
    } else if (num !== val && destination >= 0) {
      nums[destination] = num;

      destination += 1;
    }

    current += 1;
  }

  return result;
}

`
nums = [0,1,2,2,3,0,4,2], val = 2
                ^
des = 2
`;
