// 20. Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const openSet = new Set(["(", "{", "["]);
  const closeSet = new Set([")", "}", "]"]);
  const openToClose = {
    "(": ")",
    "{": "}",
    "[": "]",
  };

  const stack = [];

  for (let i = 0; i < s.length; i++) {
    const char = s.charAt(i);

    if (openSet.has(char)) stack.push(char);
    else if (closeSet.has(char)) {
      const lastOne = stack.pop();
      if (openToClose[lastOne] !== char) {
        return false;
      }
    }
  }

  if (stack.length > 0) {
    return false;
  }

  return true;
};

/*
s = "()[]{}"
     ^
*/
