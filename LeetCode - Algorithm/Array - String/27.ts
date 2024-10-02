// 27. Remove Element
// https://leetcode.com/problems/remove-element/

// time complexity: O(n)
// space complexity: O(1)
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
This logic is also quite sound. Although maintaining the sequence wasn't necessary, I personally didn't 
want to disrupt it, so I chose this approach. I used 'current' to iterate through the array, 'destination' 
to keep track of where to place a new number that wasn't equal to 'val,' and 'result' to count the numbers 
that differed from 'val.'
`;

`
nums = [0,1,2,2,3,0,4,2], val = 2
        ^
des = -1
`;
