// 328. Odd Even Linked List
// https://leetcode.com/problems/odd-even-linked-list/

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
    public ListNode oddEvenList(ListNode head) {
        if (head == null)
            return head;

        ListNode current = head;

        ListNode evenNodesHead = new ListNode();
        ListNode evenNodesCurrent = evenNodesHead;

        ListNode endOfOdd = current;

        while (current != null) {
            if (current.next != null) {
                evenNodesCurrent.next = current.next;

                current.next = current.next.next;

                evenNodesCurrent = evenNodesCurrent.next;

                evenNodesCurrent.next = null;
            }

            endOfOdd = current;
            current = current.next;
        }

        endOfOdd.next = evenNodesHead.next;

        return head;
    }
}