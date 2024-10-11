/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function (citations) {
  const sortedCitations = citations.sort((a, b) => b - a);

  result = 0;

  for (let i = 0; i < sortedCitations.length; i++) {
    if (sortedCitations[i] > i + 1) result = Math.max(result, i + 1);
    else {
      result = Math.max(result, sortedCitations[i]);

      break;
    }
  }

  return result;
};

`
[6,5,3,1,0]
 ^

[3,1,1]
 ^

[10, 10, 10]
 ^
`;
