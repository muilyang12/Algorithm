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

`
I believe I performed very well this time. 

Initially, I thought I would update the result whenever the value became equal to or smaller than the index. 
For example, given the array [5, 4, 3, 2, 1], I would stop at the 3rd number because the value 3 is equal to
the index 3 (i + 1). However, this approach does not work for cases like [10, 10, 10], where the index needs
to be considered to update the result correctly.
`;
