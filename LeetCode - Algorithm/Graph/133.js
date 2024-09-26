// 133. Clone Graph
// https://leetcode.com/problems/clone-graph/

function _Node(val, neighbors) {
  this.val = val === undefined ? 0 : val;
  this.neighbors = neighbors === undefined ? [] : neighbors;
}

/**
 * @param {_Node} node
 * @return {_Node}
 */
// time complexity: O(n + e)
// space complexity: O(2n) = O(n)
var cloneGraph = function (node) {
  if (!node) return node;

  const hashMap = {};

  const cloneNode = (node) => {
    if (node.val in hashMap) return hashMap[node.val];

    const newNode = new _Node(node.val);

    hashMap[node.val] = newNode;

    newNode.neighbors = node.neighbors.map((neighbor) => cloneNode(neighbor));

    return newNode;
  };

  return cloneNode(node);
};

`
I initially thought the time complexity would be O(n), but that’s not accurate. The time complexity is
actually O(n + e), where e represents the number of edges. When using a recursive approach, the number
of function calls is crucial. Although I used a hash map to avoid redundant computations and some function
calls return the node instantly, those calls still need to be considered in the overall time complexity.
`;
