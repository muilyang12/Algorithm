// 71. Simplify Path
// https://leetcode.com/problems/simplify-path/

/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function (path) {
  const resultStack = [];

  const pathDivided = path.split("/");

  for (let i = 0; i < pathDivided.length; i++) {
    const current = pathDivided[i];
    if (current === "") continue;
    else if (current === ".") continue;
    else if (current === "..") resultStack.pop();
    else resultStack.push(current);
  }

  return "/" + resultStack.join("/");
};

/*
path = "/home/user/Documents/../Pictures"
*/
