// 117. Populating Next Right Pointers in Each Node II
// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

function _Node(val, left, right, next) {
  this.val = val === undefined ? null : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
  this.next = next === undefined ? null : next;
}

/**
 * @param {_Node} root
 * @return {_Node}
 */
var connect = function (root) {
  const queue = [];
  if (root) queue.push(root);

  let previous = null;
  while (queue.length > 0) {
    const currentLength = queue.length;
    for (let i = 0; i < currentLength; i++) {
      let current = queue.shift();

      if (current.left) queue.push(current.left);
      if (current.right) queue.push(current.right);

      if (previous) previous.next = current;
      previous = current;
    }

    previous.next = null;
    previous = null;
  }

  return root;
};
