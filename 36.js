/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    const boardSize = board.length;
    let usedNumbers;

    for (let i = 0; i < boardSize; i++) {
        usedNumbers = new Set();
        for (let j = 0; j < boardSize; j++) {
            const value = board[i][j];

            if (value === '.') continue;

            if (usedNumbers.has(value)) return false;
            else usedNumbers.add(value);
        }

        usedNumbers = new Set();
        for (let j = 0; j < boardSize; j++) {
            const value = board[j][i];

            if (value === '.') continue;

            if (usedNumbers.has(value)) return false;
            else usedNumbers.add(value);
        }
    }

    for (let i = 0; i < (boardSize / 3) ** 2; i++) {
        /*
            0 1 2
            3 4 5
            6 7 8
        */
        usedNumbers = new Set();

        const quotient = Math.floor(i / 3);
        const remainder = i % 3;

        for (let i = 0; i < boardSize / 3; i++) {
            for (let j = 0; j < boardSize / 3; j++) {
                const value = board[quotient * 3 + i][remainder * 3 + j];

                if (value === '.') continue;

                if (usedNumbers.has(value)) return false;
                else usedNumbers.add(value);
            }
        }

    }

    return true;
};