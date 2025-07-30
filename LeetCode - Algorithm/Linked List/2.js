// 2. Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  const dummy = new ListNode(-1);
  let current = dummy;

  let currentL1 = l1;
  let currentL2 = l2;

  let carry = 0;

  while (currentL1 || currentL2) {
    if (currentL1 && currentL2) {
      let number = currentL1.val + currentL2.val + carry;
      carry = number >= 10 ? 1 : 0;
      const rest = number >= 10 ? number - 10 : number;

      current.next = new ListNode(rest);

      current = current.next;
      currentL1 = currentL1.next;
      currentL2 = currentL2.next;
    } else if (currentL1 && !currentL2) {
      let number = currentL1.val + carry;
      carry = number >= 10 ? 1 : 0;
      const rest = number >= 10 ? number - 10 : number;

      current.next = new ListNode(rest);

      current = current.next;
      currentL1 = currentL1.next;
    } else {
      let number = currentL2.val + carry;
      carry = number >= 10 ? 1 : 0;
      const rest = number >= 10 ? number - 10 : number;

      current.next = new ListNode(rest);

      current = current.next;
      currentL2 = currentL2.next;
    }
  }

  if (carry > 0) {
    current.next = new ListNode(carry);
  }

  return dummy.next;
};

/*
l1 = [2,4,3], l2 = [5,6,4]

l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
*/
