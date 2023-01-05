public class KingsTourJava{
    private int N;

    public KingsTourJava(){
        this.N = 8;
    }

    private boolean isSafe(int x, int y, int[][] board){
        if(x >= 0 && y >= 0 && x < this.N && y < this.N && board[x][y] == -1){
            return true;
        }
        return false;
    }

    private boolean ktUtils(int x, int y, int idx, int[][] board, int[] xMoves, int[] yMoves){

        if(idx == this.N * this.N){
            return true;
        }

        for(int i = 0; i < this.N; i++){
            int newX = x + xMoves[i];
            int newY = y + yMoves[i];

            if(this.isSafe(newX, newY, board)){
                board[newX][newY] = idx;

                if(this.ktUtils(newX, newY, idx + 1, board, xMoves, yMoves) == true){
                    return true;
                }

                board[newX][newY] = -1;
            }
        }

        return false;
    }

    private int[][] populateBoard(){
        int[][] board = new int[this.N][this.N];

        for(int i = 0; i < this.N; i++){
            for(int j = 0; j < this.N; j++){
                board[i][j] = -1;
            }
        }

        return board;
    }

    private void printBoard(int[][] board){
        
        String boardString = "";

        for(int i = 0; i < this.N; i++){
            boardString += "\n";
            for(int j = 0; j < this.N; j++){
                boardString += board[i][j] + " ";
            }
        }

        System.out.println(boardString);
    }

    public void runKT(){
        int[][] board = this.populateBoard();

        int[] xMoves = new int[] {2, 1, -1, -2, -2, -1, 1, 2};
        int[] yMoves = new int[] {1, 2, 2, 1, -1, -2, -2, -1};

        board[0][0] = 0;

        if(this.ktUtils(0, 0, 1, board, xMoves, yMoves) == false){
            System.out.println("No Solution Found");
        }
        else{
            this.printBoard(board);
        }

    }




}