
const n = 8;

const isSafe = (x, y, board) => {
    if (x >= 0 && y >= 0 && x < n && y < n && board[x][y] === -1) return true;
    return false;
}

const populateBoard = () => {
    const board = [];

    for (let i = 0; i < n; i++){
        board.push([]);
        for(let j = 0; j< n; j ++){
            board[i].push(-1)
        }
    }

    return board;
}
const ktUtil = (x, y, idx, board, xMoves, yMoves) => {

    if (idx === n * n) {
        return true;
    }

    for(let i = 0; i < n; i ++){
        const newX = x + xMoves[i];
        const newY = y + yMoves[i];
        

        if(isSafe(newX, newY, board)){
            board[newX][newY] = idx;

            if(ktUtil(newX, newY, idx+1, board, xMoves, yMoves) === true){
                return true;
            }

            board[newX][newY] = -1;
        }

        
    }
    return false;

}

const kt = () => {
    const board = populateBoard();

    
    const xMoves = [2, 1, -1, -2, -2, -1, 1, 2];
    const yMoves = [1, 2, 2, 1, -1, -2, -2, -1];

    const idx = 1;

    board[0][0] = 0;

    if(ktUtil(0, 0, idx, board, xMoves, yMoves) === false){
        console.log("No Solution Found");
    }
    else{
        console.log(board);
    }

}

kt();