// 150. Evaluate Reverse Polish Notation
// https://leetcode.com/problems/evaluate-reverse-polish-notation/

/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
  const stack = [];

  for (let i = 0; i < tokens.length; i++) {
    if (tokens[i] === "+") {
      const first = stack.pop();
      const second = stack.pop();
      stack.push(second + first);
    } else if (tokens[i] === "-") {
      const first = stack.pop();
      const second = stack.pop();
      stack.push(second - first);
    } else if (tokens[i] === "*") {
      const first = stack.pop();
      const second = stack.pop();
      stack.push(second * first);
    } else if (tokens[i] === "/") {
      const first = stack.pop();
      const second = stack.pop();
      stack.push(Math.trunc(second / first));
    } else {
      stack.push(Number(tokens[i]));
    }
  }

  return stack[0];
};

/*
tokens = ["2","1","+","3","*"]
stack = [9]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
stack = [10,6,-132]
*/

// This question was a bit tricky. At first, I tried approaching it from the end, but it felt difficult and unlikely to work. Then I tried starting from the beginning, and I was able to clearly find a pair of numbers used for the calculation, along with a letter.

// I didn't know about the "Math.trunc" function. I should keep this in mind. "Math.floor" rounds down, while "Math.trunc" cuts off towards zero.
