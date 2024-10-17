// 97. Interleaving String
// https://leetcode.com/problems/interleaving-string/

function isInterleave(s1: string, s2: string, s3: string): boolean {
  const s1Length = s1.length;
  const s2Length = s2.length;

  if (s1Length + s2Length !== s3.length) return false;

  const resultArray: boolean[][] = [];
  for (let i = 0; i < s1Length + 1; i++) {
    const temp: boolean[] = [];

    for (let j = 0; j < s2Length + 1; j++) {
      temp.push(false);
    }

    resultArray.push(temp);
  }
  resultArray[0][0] = true;

  for (let i = 0; i < s1Length; i++) {
    if (s1[i] !== s3[i]) break;

    resultArray[i + 1][0] = true;
  }

  for (let j = 0; j < s2Length; j++) {
    if (s2[j] !== s3[j]) break;

    resultArray[0][j + 1] = true;
  }

  for (let i = 0; i < s1Length; i++) {
    for (let j = 0; j < s2Length; j++) {
      if (resultArray[i][j + 1]) {
        resultArray[i + 1][j + 1] = s1[i] === s3[i + j + 1];
      } else if (resultArray[i + 1][j]) {
        resultArray[i + 1][j + 1] = s2[j] === s3[i + j + 1];
      }
    }
  }

  return resultArray[s1Length][s2Length];
}

`
s1 = "aabcc"
      ^
s2 = "dbbca"
       ^
s3 = "aadbbcbcac"
        ^

[
  [ true, false, false, false, false, false ],
  [ true, false, false, false, false, false ],
  [ true, false, false, false, false, false ],
  [ false, false, false, false, false, false ],
  [ false, false, false, false, false, false ],
  [ false, false, false, false, false, false ]
]
`;
