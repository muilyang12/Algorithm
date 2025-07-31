// 138. Copy List with Random Pointer
// https://leetcode.com/problems/copy-list-with-random-pointer/

function _Node(val, next, random) {
  this.val = val;
  this.next = next;
  this.random = random;
}

/**
 * @param {_Node} head
 * @return {_Node}
 */
var copyRandomList = function (head) {
  const hash = new Map();

  const copyNode = (node) => {
    if (!node) return null;
    if (hash.has(node)) return hash.get(node);

    const newNode = new _Node(node.val);
    hash.set(node, newNode);
    newNode.next = copyNode(node.next);
    newNode.random = copyNode(node.random);

    return newNode;
  };

  return copyNode(head);
};
