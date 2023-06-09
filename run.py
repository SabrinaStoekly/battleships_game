import random


class Battleship:
    """
    Keeps track of the current state of the gam
    Sets up the board  and places the  ship on a random possition
    """
    def __init__(self):
        self.board = []
        self.ship_row = 0
        self.ship_col = 0
        self.num_turns = 0
        self.guesses = []

        for x in range(5):
            self.board.append(["-"] * 5)

        self.place_ship()

    def place_ship(self):
        self.ship_row = random.randint(0, 4)
        self.ship_col = random.randint(0, 4)

    def print_board(self):
        print("  1 2 3 4 5")
        for i, row in enumerate(self.board):
            print(i+1, " ".join(row))

    def make_guess(self, guess_r, guess_c):
        """
        Takes a row and column as arguments and
        checks if there is a ship at that location
        on the board
        """
        self.num_turns += 1

        if guess_r == self.ship_row and guess_c == self.ship_col:
            print("Congratulations! You sank my battleship!")
            return True
        else:
            if guess_r < 1 or guess_r > 5 or guess_c < 1 or guess_c > 5:
                print("Oops, that's not even in the ocean.")
            elif self.board[guess_r-1][guess_c-1] == "X":
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                self.board[guess_r-1][guess_c-1] = "X"
                self.guesses.append((guess_r, guess_c))

            self.print_board()
            return False


def play_game():
    """
    Prints the full and upddated board to the console
    """
    game = Battleship()
    print("Let's play Battleship!")
    game.print_board()

    while True:
        try:
            guess_r = int(input("Guess Row (1-5): "))
            guess_c = int(input("Guess Col (1-5): "))
        except ValueError:
            print("Oops, please enter a valid row and column number.")
            continue

        if game.make_guess(guess_r, guess_c):
            print("You took", game.num_turns, "turns to win.")
            print("Here are your guesses:")
            for guess in game.guesses:
                print(guess)
            break


print('--' * 25)
print('Welcome to the BattleShip Game !!')
print('The board size is 5x5, and it has 1 ship')
print('You have as many guesses as you can!')
print('--' * 25)
play_game()







