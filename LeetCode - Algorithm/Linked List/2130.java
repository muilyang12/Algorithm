// 2130. Maximum Twin Sum of a Linked List
// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

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
    public int pairSum(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        int halfOfLength = 0;

        while (fast != null) {
            slow = slow.next;
            fast = fast.next.next;

            halfOfLength += 1;
        }

        ListNode current = head;
        int[] values = new int[halfOfLength];

        for (int i = 0; i < halfOfLength; i++) {
            values[i] += current.val;
            values[halfOfLength - 1 - i] += slow.val;

            current = current.next;
            slow = slow.next;
        }

        int result = -1;
        for (int value : values) {
            result = Math.max(result, value);
        }

        return result;
    }
}