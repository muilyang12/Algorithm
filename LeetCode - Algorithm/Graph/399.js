// 399. Evaluate Division
// https://leetcode.com/problems/evaluate-division/

/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} queries
 * @return {number[]}
 */
var calcEquation = function (equations, values, queries) {
  const graph = {};

  equations.forEach(([from, to], index) => {
    if (graph[from]) graph[from].push([to, values[index]]);
    else graph[from] = [[to, values[index]]];

    if (graph[to]) graph[to].push([from, 1 / values[index]]);
    else graph[to] = [[from, 1 / values[index]]];
  });

  return queries.map((query) => {
    return getValue(query[0], query[1], graph, new Set()) ?? -1;
  });
};

const getValue = (from, to, graph, visited) => {
  if (visited.has(from)) return;

  visited.add(from);

  const possibleToAndValues = graph[from];

  if (!possibleToAndValues) return;

  const target = possibleToAndValues.find(([possibleTo, _]) => possibleTo === to);
  if (target) {
    const [_, possibleValue] = target;

    return possibleValue;
  }

  for (let i = 0; i < possibleToAndValues.length; i++) {
    const [possibleTo, possibleValue] = possibleToAndValues[i];

    const value = getValue(possibleTo, to, graph, visited);
    if (value) return possibleValue * value;
  }

  visited.delete(from);
};

/*
graph = { a: [ [ 'b', 1.5 ] ], b: [ [ 'c', 2.5 ] ], bc: [ [ 'cd', 5 ] ] }

a, c
b, c
*/

// This problem is really challenging. recursion always feels tricky. :( The key is always to grasp the concept. Here, this function will return the value from "from" to "to" with iterating through the entire array. And, my approach essentially assumes only one path exists since I return immediately once the answer is found.
