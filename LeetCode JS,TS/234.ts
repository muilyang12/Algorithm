// 234. Palindrome Linked List
// https://leetcode.com/problems/palindrome-linked-list/

// Stack
// time complexity: O(n + n/2) = O(n) || space complexity: O(n)
function isPalindrome(head: ListNode | null): boolean {
  const stack: number[] = [];
  let pointer = head;

  while (pointer) {
    stack.push(pointer.val);

    pointer = pointer.next;
  }

  let left = 0;
  let right = stack.length - 1;

  while (left < right) {
    if (stack[left] !== stack[right]) return false;

    left += 1;
    right -= 1;
  }

  return true;
}

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}
