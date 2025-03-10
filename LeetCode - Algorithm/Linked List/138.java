// 138. Copy List with Random Pointer
// https://leetcode.com/problems/copy-list-with-random-pointer/

import java.util.Map;
import java.util.HashMap;

class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}

class Solution {
    Map<Node, Node> hashMap;

    public Node copyRandomList(Node head) {
        if (head == null)
            return head;

        this.hashMap = new HashMap<>();

        return this.copy(head);
    }

    private Node copy(Node node) {
        if (hashMap.containsKey(node))
            return hashMap.get(node);

        Node newNode = new Node(node.val);
        hashMap.put(node, newNode);

        if (node.next != null)
            newNode.next = this.copy(node.next);
        if (node.random != null)
            newNode.random = this.copy(node.random);

        return newNode;
    }
}