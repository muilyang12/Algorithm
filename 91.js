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

    // 한 개의 문자만 남았을 때.
    return dfs(start + 1);
  };

  return dfs(0);
};

// Depth First Search (DFS) + Memoization
// time complexity: O(n) || space complexity: O(n) -> Length of call stack
var numDecodings3 = function (s) {
  // 해당 위치에서부터 시작했을 때 몇 가지로 디코드 될 수 있는지를 저장하는 배열.
  const memo = [];
  memo[s.length] = 1;

  const dfs = (start) => {
    if (!!memo[start]) {
      return memo[start];
    }

    // return을 사용하지 않으니까 셋 중의 하나의 경우만 해당되도록 else if, else로 묶어야 함.
    if (s[start] === "0") {
      // 부분 문자열의 첫 시작이 '0' 일 때는 그 위치에서 시작할 경우 경우의 수가 0.
      memo[start] = 0;
    } else if (
      start + 1 <= s.length - 1 &&
      Number(s.slice(start, start + 2)) <= 26
    ) {
      // 두 개 이상의 문자가 남았고 둘 다 26보다 작거나 같을 때.
      memo[start] = dfs(start + 1) + dfs(start + 2);
    } else {
      // 한 개의 문자만 남았을 때.
      memo[start] = dfs(start + 1);
    }

    return memo[start];
  };

  return dfs(0);
};

// Dynamic Programming
// time complexity: O(n) || space complexity: O(n)
var numDecodings4 = function (s) {
  const length = s.length;

  const memo = [];
  memo[length] = 1;

  for (let i = length - 1; i >= 0; i--) {
    if (s[i] === "0") {
      memo[i] = 0;
    } else if (i + 1 <= length - 1 && Number(s.slice(i, i + 2)) < 27) {
      memo[i] = memo[i + 1] + memo[i + 2];
    } else {
      memo[i] = memo[i + 1];
    }
  }

  return memo[0];
};
