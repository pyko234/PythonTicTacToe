class GameBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display_board(self):
        for index, row in enumerate(self.board):
            print(f" {row[0]} | {row[1]} | {row[2]} ")
            if index != 2:
                print("-------------")

    def place_marker(self, row, col, marker):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = marker
            return True
        return False

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[2][0]

        return ''

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

