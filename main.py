import os
from game_board import GameBoard
from player import Player

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    board = GameBoard()
    player1 = Player('X')
    player2 = Player('O')

    while True:
        clear_screen()

        board.display_board()

        # Player 1's turn
        print()
        print("Player 1's turn (X)")
        row, col = map(int, input("Enter row and column (0-2): ").split("-"))
        if player1.make_move(board, row, col):
            if board.check_winner() == 'X':
                clear_screen()
                board.display_board()
                print()
                print("Player 1 (X) wins!")
                break
        else:
            print("Invaild move.")
            input("Press enter to continue...")
            continue

        if board.is_board_full():
            clear_screen()
            board.display_board()
            print()
            print("It's a tie!")
            break




        # Player 2's turn
        while True:
            clear_screen()
            board.display_board()
            print()
            print("Player 2's turn (O)")
            row, col = map(int, input("Enter row and column (0-2): ").split("-"))
            if player2.make_move(board, row, col):
                if board.check_winner() == 'O':
                    clear_screen()
                    board.display_board()
                    print()
                    print("Player 2 (0) wins!")
                    break
                break # Break the inner loop if a vaild loop is made
            else:
                print("Invaild move.")
                input("Press enter to continue...")


if __name__ == "__main__":
    main()
