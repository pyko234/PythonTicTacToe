class Player:
    def __init__(self, marker):
        self.marker = marker

    def make_move(self, board, row, col):
        return board.place_marker(row, col, self.marker)

    def get_marker(self):
        return self.marker


