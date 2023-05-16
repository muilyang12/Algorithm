/**
 * @param {ListNode} head
 * @return {ListNode}
 */

// Stack
// time complexity: O(2n) = O(n) || space complexity: O(n)
var reverseList1 = function (head) {
  const stack = [];

  let headPointer = head;
  while (!!headPointer) {
    stack.push(headPointer.val);

    headPointer = headPointer.next;
  }

  const result = new ListNode(-1);

  let resultPointer = result;
  for (let i = stack.length - 1; i >= 0; i--) {
    resultPointer.next = new ListNode(stack[i]);
    resultPointer = resultPointer.next;
  }

  return result.next;
};

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}
