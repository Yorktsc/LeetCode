class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        """
        self.matrix = [[0] * n for _ in range(n)]
        """
        self.r = [0] * n
        self.c = [0] * n
        self.d = 0
        self.vd = 0
        self.n = n
        
    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        """
        n = len(self.matrix)
        one,two,three,four = True, True, True, True
        self.matrix[row][col] = player
        for i in range(n):
            if self.matrix[row][i] != player:
                one = False
        for j in range(n):
            if self.matrix[j][col] != player:
                two = False
        for k in range(n):
            if self.matrix[k][k] != player:
                three = False
        for l in range(n):
            if self.matrix[l][n-1-l] != player:
                four = False
        if one or two or three or four:
            return player
        return 0
        """
        
        offset = 1 if player == 1 else -1
        
        self.r[row] += offset
        self.c[col] += offset
        if row == col:
            self.d += offset
        if row + col == self.n - 1:
            self.vd += offset
        if self.n in [self.r[row], self.c[col],  self.d, self.vd]:
            return 1
        elif -self.n in [self.r[row], self.c[col],  self.d, self.vd]:
            return 2
        else:
            return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
