// 91. Decode Ways
// https://leetcode.com/problems/decode-ways/

/**
 * @param {string} s
 * @return {number}
 */

// Divide-and-conquer
// time complexity: O(2^n) || space complexity: O(n) -> Length of call stack
var numDecodings1 = function (s) {
  if (s[0] === "0") return 0;

  let result = 0;

  const target01 = s.slice(0, 1);
  if (Number(target01) <= 26) {
    const nextS = s.slice(1);
    if (nextS.length === 0) result += 1;
    else result += numDecodings1(nextS);
  }

  if (s.length >= 2) {
    const target02 = s.slice(0, 2);
    if (Number(target02) <= 26) {
      const nextS = s.slice(2);
      if (nextS.length === 0) result += 1;
      else result += numDecodings1(nextS);
    }
  }

  return result;
};

// Depth First Search (DFS)
// time complexity: O(2^n) || space complexity: O(n) -> Length of call stack
var numDecodings2 = function (s) {
  const dfs = (start) => {
    // 부분 문자열의 첫 시작이 '0' 일 때.
    if (s[start] === "0") {
      return 0;
    }

    // start가 문자열의 끝을 가리킬 때.
    if (start == s.length) {
      return 1;
    }

    // 두 개 이상의 문자가 남았고 둘 다 26보다 작거나 같을 때.
    if (start + 1 <= s.length - 1 && Number(s.slice(start, start + 2)) <= 26) {
      return dfs(start + 1) + dfs(start + 2);
    }

    return dfs(start + 1);
  };

  return dfs(0);
};
