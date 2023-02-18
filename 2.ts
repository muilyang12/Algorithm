// 2. Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/

// time complexity: O(max(m, n)) || space complexity: O(max(m, n))
function addTwoNumbers(
  l1: ListNode | null,
  l2: ListNode | null
): ListNode | null {
  if (!l1 || !l2) return null;

  let l1Pointer: ListNode | null = l1;
  let l2Pointer: ListNode | null = l2;

  let result: ListNode = new ListNode();
  let resultPointer: ListNode = result;

  let carry = 0;
  while (true) {
    let l1Value = l1Pointer?.val ? l1Pointer?.val : 0;
    let l2Value = l2Pointer?.val ? l2Pointer?.val : 0;

    const remainder = (l1Value + l2Value + carry) % 10;
    const quotient = (l1Value + l2Value + carry - remainder) / 10;

    resultPointer.val = remainder;
    carry = quotient;

    if (l1Pointer?.next || l2Pointer?.next || carry > 0) {
      resultPointer.next = new ListNode();
      resultPointer = resultPointer.next;

      l1Pointer = l1Pointer?.next ? l1Pointer.next : null;
      l2Pointer = l2Pointer?.next ? l2Pointer.next : null;
    } else {
      break;
    }
  }

  return result;
}

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}
