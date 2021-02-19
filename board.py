# C = Castillo, N = Caballo, K = king, Q = Queen, P = Peon, B = Alfil
# B = black, W = white
# otra prueba xd
class chessboard:
    
    def __init__(self):
        self.WIDTH,self.HEIGHT = 8,8
        self.counter = 0
        self.pieces = [chr(x) for x in range(97,105)]
    
    def create_board(self):
        board = list()
        for f in range(self.WIDTH):
            cols = list()
            for c in range(self.HEIGHT):
                cols.append(f'{self.pieces[c]}{f+1}')
            board.append(cols)
        return board
    
    def show_board(self,board):
        for f in range(self.WIDTH):
            for c in range(self.HEIGHT):
                print(board[f][c].rjust(3),end='')
            print()

chessman = {'a1'='BC','a2'='DN','a3'='DB','a4'='DQ','a5'='DK','a6'='DB','a7'='DN','a8'='DC',
            'a1'='BP','a2'='DP','a3'='DP','a4'='DP','a5'='DP','a6'='DP','a7'='DP','a8'='DP'
            'a1'='WC','a2'='WN','a3'='WB','a4'='WQ','a5'='WK','a6'='WB','a7'='WN','a8'='WC',
            'a1'='WP','a2'='WP','a3'='WP','a4'='WP','a5'='WP','a6'='WP','a7'='WP','a8'='WP'}        
# new_chessboard = chessboard()
# newboard = new_chessboard.create_board()
# new_chessboard.show_board(newboard)