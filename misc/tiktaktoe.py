class TikTakToe():
    
    def __init__(self, board: dict = {}) -> None:

        self.board = board
        
        self.p2_turn = False
        if len(self.board) > 0:
            if len(self.board) % 2 == 0:
                self.p2_turn = True

    def __repr__(self) -> str:
        return str(self.board)

    def __str__(self):
        str = ""
        for i in range(0,3):
            str += "|"
            for j in range(0,3):
                str += self.board.get((i,j), "_") + "|"
            str += "\n"
        return str

    def check_state(self):
        pass

    def mark_place(self, place: tuple):
        pass

dict = {(1,0): "X", (1,1): "O", (0,2): "X"}
board = TikTakToe(dict)
print(repr(board))
print(board)
