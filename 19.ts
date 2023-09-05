// 19. Remove Nth Node From End of List
// https://leetcode.com/problems/remove-nth-node-from-end-of-list/

// Stack
// time complexity: O(n) || space complexity: O(n) (n: number of nodes)
function removeNthFromEnd1(head: ListNode | null, n: number): ListNode | null {
  if (!head) return head;

  const stack: ListNode[] = [];

  let pointer: ListNode | null = head;
  while (pointer) {
    stack.push(pointer);

    pointer = pointer.next;
  }

  const targetIndex = stack.length - n;

  if (targetIndex - 1 >= 0 && targetIndex + 1 <= stack.length - 1) {
    stack[targetIndex - 1].next = stack[targetIndex + 1];
  } else if (targetIndex - 1 < 0 && targetIndex + 1 <= stack.length - 1) {
    head = head.next;
  } else if (targetIndex - 1 >= 0 && targetIndex + 1 > stack.length - 1) {
    stack[targetIndex - 1].next = null;
  } else {
    head = null;
  }

  return head;
}

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}
