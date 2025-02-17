// 61. Rotate List
// https://leetcode.com/problems/rotate-list/

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || k == 0)
            return head;

        int length = 0;
        ListNode current = head;

        while (current != null) {
            current = current.next;
            length += 1;
        }

        int actualRotationCount = k % length;

        ListNode fast = head;
        ListNode slow = head;

        for (int i = 0; i < actualRotationCount; i++)
            fast = fast.next;

        while (fast.next != null) {
            fast = fast.next;

            slow = slow.next;
        }

        fast.next = head;
        ListNode result = slow.next;
        slow.next = null;

        return result;
    }
}