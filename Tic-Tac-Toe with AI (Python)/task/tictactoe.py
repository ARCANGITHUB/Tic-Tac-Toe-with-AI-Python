import random
from random import randint


class TicTacToe:
    opt = []
    level = []
    board = []
    ava_spots = []
    x = 0
    y = 0

    def __init__(self):
        self.grid = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        self.counter = 0

    def players(self, *played):
        for play in played:
            if play == 'easy':
                self.change('ai')
                self.level.append(play)
            elif play == 'medium':
                self.change('ai')
                self.level.append(play)
            elif play == 'hard':
                self.change('ai')
                self.level.append(play)
            elif play == 'user':
                self.change('user')
                self.level.append(play)
        return played

    def commands_users(self):
        user_ai = input("Input command: > ")
        while True:
            if user_ai == 'exit':
                exit()
            try:
                command, player1, player2 = user_ai.split()
                self.players(player1, player2)
                print(self.__str__())
                break
            except ValueError:
                print("Bad parameters!")
                user_ai = input("Input command: > ")

    def change(self, *args):
        self.opt += args
        return self.opt

    def assignments(self):
        if self.opt[0] == 'user':
            return 'X'
        elif self.opt[1] == 'user':
            return 'O'

    def assignments2(self):
        if self.opt[0] == 'ai':
            return 'X'
        elif self.opt[1] == 'ai':
            return 'O'

    def coord_ai_easy(self):
        self.x = random.randint(0, 2)
        self.y = random.randint(0, 2)

    def coord_user(self):
        move = input("Enter the coordinates: ").replace('  ', ' ')
        try:
            self.y, self.x = int(move[0]), int(move[2])
        except ValueError:
            print("You should enter numbers!\n")

    def loop_looking(self):
        for i in self.grid[self.x][self.y]:
            if self.grid[self.x][self.y] == '_':
                return self.grid[self.x][self.y]

    def easy_x(self):
        if self.opt[0] == 'ai' and self.level[0] == 'easy':
            print('Making move level "easy"')
            while True:
                self.coord_ai_easy()
                if self.loop_looking():
                    self.grid[self.x][self.y] = 'X'
                    self.counter += 1
                    print(self.__str__())
                    if self.game_state():
                        exit()
                    break
                elif self.grid[self.x][self.y] == ['X', 'O']:
                    continue

    def easy_o(self):
        if self.opt[1] == 'ai' and self.level[1] == 'easy':
            print('Making move level "easy"')
            while True:
                self.coord_ai_easy()
                if self.loop_looking():
                    self.grid[self.x][self.y] = 'O'
                    self.counter += 1
                    print(self.__str__())
                    if self.game_state():
                        exit()
                    break
                elif self.grid[self.x][self.y] == ['X', 'O']:
                    continue

    def medium_alg_o(self):
        #   Horizontals
        if self.grid[0][0] == 'X' and self.grid[0][1] == 'X' \
                and self.grid[0][2] == '_':
            self.grid[0][2] = 'O'
        elif self.grid[0][0] == 'X' and self.grid[0][2] == 'X' \
                and self.grid[0][1] == '_':
            self.grid[0][1] = 'O'
        elif self.grid[0][1] == 'X' and self.grid[0][2] == 'X' \
                and self.grid[0][0] == '_':
            self.grid[0][0] = 'O'

        elif self.grid[1][0] == 'X' and self.grid[1][1] == 'X' \
                and self.grid[1][2] == '_':
            self.grid[1][2] = 'O'
        elif self.grid[1][0] == 'X' and self.grid[1][2] == 'X' \
                and self.grid[1][1] == '_':
            self.grid[1][1] = 'O'
        elif self.grid[1][1] == 'X' and self.grid[1][2] == 'X' \
                and self.grid[1][0] == '_':
            self.grid[1][0] = 'O'

        elif self.grid[2][0] == 'X' and self.grid[2][1] == 'X' \
                and self.grid[2][2] == '_':
            self.grid[2][2] = 'O'
        elif self.grid[2][0] == 'X' and self.grid[2][2] == 'X' \
                and self.grid[2][1] == '_':
            self.grid[2][1] = 'O'
        elif self.grid[2][1] == 'X' and self.grid[2][2] == 'X' \
                and self.grid[2][0] == '_':
            self.grid[2][0] = 'O'

        #   Verticals

        elif self.grid[0][0] == 'X' and self.grid[1][0] == 'X' \
                and self.grid[2][0] == '_':
            self.grid[2][0] = 'O'
        elif self.grid[0][0] == 'X' and self.grid[2][0] == 'X' \
                and self.grid[1][0] == '_':
            self.grid[1][0] = 'O'
        elif self.grid[1][0] == 'X' and self.grid[2][0] == 'X' \
                and self.grid[0][0] == '_':
            self.grid[0][0] = 'O'

        elif self.grid[0][1] == 'X' and self.grid[1][1] == 'X' \
                and self.grid[2][1] == '_':
            self.grid[2][1] = 'O'
        elif self.grid[0][1] == 'X' and self.grid[2][1] == 'X' \
                and self.grid[1][1] == '_':
            self.grid[1][1] = 'O'
        elif self.grid[1][1] == 'X' and self.grid[2][1] == 'X' \
                and self.grid[0][1] == '_':
            self.grid[0][1] = 'O'

        elif self.grid[0][2] == 'X' and self.grid[1][2] == 'X' \
                and self.grid[2][2] == '_':
            self.grid[2][2] = 'O'
        elif self.grid[0][2] == 'X' and self.grid[2][2] == 'X' \
                and self.grid[1][2] == '_':
            self.grid[1][2] = 'O'
        elif self.grid[1][2] == 'X' and self.grid[2][2] == 'X' \
                and self.grid[0][2] == '_':
            self.grid[0][2] = 'O'

        # Diagonals

        elif self.grid[0][0] == 'X' and self.grid[1][1] == 'X' \
                and self.grid[2][2] == '_':
            self.grid[2][2] = 'O'
        elif self.grid[0][0] == 'X' and self.grid[2][2] == 'X' \
                and self.grid[1][1] == '_':
            self.grid[1][1] = 'O'
        elif self.grid[1][1] == 'X' and self.grid[2][2] == 'X' \
                and self.grid[0][0] == '_':
            self.grid[0][0] = 'O'

        elif self.grid[0][2] == 'X' and self.grid[1][1] == 'X' \
                and self.grid[2][0] == '_':
            self.grid[2][0] = 'O'
        elif self.grid[0][2] == 'X' and self.grid[2][0] == 'X' \
                and self.grid[1][1] == '_':
            self.grid[1][1] = 'O'
        elif self.grid[1][1] == 'X' and self.grid[2][0] == 'X' \
                and self.grid[0][2] == '_':
            self.grid[0][2] = 'O'
        else:
            self.grid[self.x][self.y] = 'O'

    def medium_alg_x(self):
        #   Horizontals
        if self.grid[0][0] == 'O' and self.grid[0][1] == 'O' \
                and self.grid[0][2] == '_':
            self.grid[0][2] = 'X'
        elif self.grid[0][0] == 'O' and self.grid[0][2] == 'O' \
                and self.grid[0][1] == '_':
            self.grid[0][1] = 'X'
        elif self.grid[0][1] == 'O' and self.grid[0][2] == 'O' \
                and self.grid[0][0] == '_':
            self.grid[0][0] = 'X'

        elif self.grid[1][0] == 'O' and self.grid[1][1] == 'O' \
                and self.grid[1][2] == '_':
            self.grid[1][2] = 'X'
        elif self.grid[1][0] == 'O' and self.grid[1][2] == 'O' \
                and self.grid[1][1] == '_':
            self.grid[1][1] = 'X'
        elif self.grid[1][1] == 'O' and self.grid[1][2] == 'O' \
                and self.grid[1][0] == '_':
            self.grid[1][0] = 'X'

        elif self.grid[2][0] == 'O' and self.grid[2][1] == 'O' \
                and self.grid[2][2] == '_':
            self.grid[2][2] = 'X'
        elif self.grid[2][0] == 'O' and self.grid[2][2] == 'O' \
                and self.grid[2][1] == '_':
            self.grid[2][1] = 'X'
        elif self.grid[2][1] == 'O' and self.grid[2][2] == 'O' \
                and self.grid[2][0] == '_':
            self.grid[2][0] = 'X'

        #   Verticals

        elif self.grid[0][0] == 'O' and self.grid[1][0] == 'O' \
                and self.grid[2][0] == '_':
            self.grid[2][0] = 'X'
        elif self.grid[0][0] == 'O' and self.grid[2][0] == 'O' \
                and self.grid[1][0] == '_':
            self.grid[1][0] = 'X'
        elif self.grid[1][0] == 'O' and self.grid[2][0] == 'O' \
                and self.grid[0][0] == '_':
            self.grid[0][0] = 'X'

        elif self.grid[0][1] == 'O' and self.grid[1][1] == 'O' \
                and self.grid[2][1] == '_':
            self.grid[2][1] = 'X'
        elif self.grid[0][1] == 'O' and self.grid[2][1] == 'O' \
                and self.grid[1][1] == '_':
            self.grid[1][1] = 'X'
        elif self.grid[1][1] == 'O' and self.grid[2][1] == 'O' \
                and self.grid[0][1] == '_':
            self.grid[0][1] = 'X'

        elif self.grid[0][2] == 'O' and self.grid[1][2] == 'O' \
                and self.grid[2][2] == '_':
            self.grid[2][2] = 'X'
        elif self.grid[0][2] == 'O' and self.grid[2][2] == 'O' \
                and self.grid[1][2] == '_':
            self.grid[1][2] = 'X'
        elif self.grid[1][2] == 'O' and self.grid[2][2] == 'O' \
                and self.grid[0][2] == '_':
            self.grid[0][2] = 'X'

        # Diagonals

        elif self.grid[0][0] == 'O' and self.grid[1][1] == 'O' \
                and self.grid[2][2] == '_':
            self.grid[2][2] = 'X'
        elif self.grid[0][0] == 'O' and self.grid[2][2] == 'O' \
                and self.grid[1][1] == '_':
            self.grid[1][1] = 'X'
        elif self.grid[1][1] == 'O' and self.grid[2][2] == 'O' \
                and self.grid[0][0] == '_':
            self.grid[0][0] = 'X'

        elif self.grid[0][2] == 'O' and self.grid[1][1] == 'O' \
                and self.grid[2][0] == '_':
            self.grid[2][0] = 'X'
        elif self.grid[0][2] == 'O' and self.grid[2][0] == 'O' \
                and self.grid[1][1] == '_':
            self.grid[1][1] = 'X'
        elif self.grid[1][1] == 'O' and self.grid[2][0] == 'O' \
                and self.grid[0][2] == '_':
            self.grid[0][2] = 'X'
        else:
            self.grid[self.x][self.y] = 'X'

    def board_index(self):
        self.board = [self.grid[0][0], self.grid[0][1], self.grid[0][2],
                      self.grid[1][0], self.grid[1][1], self.grid[1][2],
                      self.grid[2][0], self.grid[2][1], self.grid[2][2],
                      ]
        return self.board

    def find_index(self):
        self.ava_spots.clear()
        for i, value in enumerate(self.board_index()):
            if value == '_':
                self.ava_spots.append(i)

        return self.ava_spots

    def eval_x(self, b):
        for row in range(3):
            if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
                if b[row][0] == 'X':
                    return 10
                elif b[row][0] == 'O':
                    return -10

        for col in range(3):

            if b[0][col] == b[1][col] and b[1][col] == b[2][col]:

                if b[0][col] == 'X':
                    return 10
                elif b[0][col] == 'O':
                    return -10

        if b[0][0] == b[1][1] and b[1][1] == b[2][2]:

            if b[0][0] == 'X':
                return 10
            elif b[0][0] == 'O':
                return -10

        if b[0][2] == b[1][1] and b[1][1] == b[2][0]:

            if b[0][2] == 'X':
                return 10
            elif b[0][2] == 'O':
                return -10

        return 0

    def minimax_alg_x(self, board, depth, is_max):
        score = self.eval_x(board)

        if score == 10:
            return score

        if score == -10:
            return score

        if len(self.find_index()) == 0:
            return 0

        # If this maximizer's move
        if is_max:
            best = -1000

            # Traverse all cells
            for i in range(3):
                for j in range(3):

                    # Check if cell is empty
                    if board[i][j] == '_':

                        # Make the move
                        board[i][j] = 'X'

                        # Call minimax recursively and choose
                        # the maximum value
                        best = max(best, self.minimax_alg_x(board, depth + 1,
                                                            not is_max))

                        # Undo the move
                        board[i][j] = '_'
            return best

        # If this minimizer's move
        else:
            best = 1000

            # Traverse all cells
            for i in range(3):
                for j in range(3):

                    # Check if cell is empty
                    if board[i][j] == '_':

                        # Make the move
                        board[i][j] = 'O'

                        # Call minimax recursively and choose
                        # the minimum value
                        best = min(best, self.minimax_alg_x(board, depth + 1,
                                                            not is_max))

                        # Undo the move
                        board[i][j] = '_'
            return best

    def best_move_x(self, board):
        best_val = -1000
        best_move = (-1, -1)

        # Traverse all cells, evaluate minimax function for
        # all empty cells. And return the cell with optimal
        # value.
        for i in range(3):
            for j in range(3):

                # Check if cell is empty
                if board[i][j] == '_':

                    # Make the move
                    board[i][j] = 'X'

                    # compute evaluation function for this
                    # move.
                    move_val = self.minimax_alg_x(board, 0, False)

                    # Undo the move
                    board[i][j] = '_'

                    # If the value of the current move is
                    # more than the best value, then update
                    # best/
                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val
        return best_move

    def eval_o(self, b):
        for row in range(3):
            if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
                if b[row][0] == 'O':
                    return 10
                elif b[row][0] == 'X':
                    return -10

        for col in range(3):

            if b[0][col] == b[1][col] and b[1][col] == b[2][col]:

                if b[0][col] == 'O':
                    return 10
                elif b[0][col] == 'X':
                    return -10

        if b[0][0] == b[1][1] and b[1][1] == b[2][2]:

            if b[0][0] == 'O':
                return 10
            elif b[0][0] == 'X':
                return -10

        if b[0][2] == b[1][1] and b[1][1] == b[2][0]:

            if b[0][2] == 'O':
                return 10
            elif b[0][2] == 'X':
                return -10

        return 0

    def minimax_alg_o(self, board, depth, is_max):
        score = self.eval_o(board)

        if score == 10:
            return score

        if score == -10:
            return score

        if len(self.find_index()) == 0:
            return 0

        # If this maximizer's move
        if is_max:
            best = -1000

            # Traverse all cells
            for i in range(3):
                for j in range(3):

                    # Check if cell is empty
                    if board[i][j] == '_':

                        # Make the move
                        board[i][j] = 'O'

                        # Call minimax recursively and choose
                        # the maximum value
                        best = max(best, self.minimax_alg_o(board, depth + 1,
                                                            not is_max))

                        # Undo the move
                        board[i][j] = '_'
            return best

        # If this minimizer's move
        else:
            best = 1000

            # Traverse all cells
            for i in range(3):
                for j in range(3):

                    # Check if cell is empty
                    if board[i][j] == '_':

                        # Make the move
                        board[i][j] = 'X'

                        # Call minimax recursively and choose
                        # the minimum value
                        best = min(best, self.minimax_alg_o(board, depth + 1,
                                                            not is_max))

                        # Undo the move
                        board[i][j] = '_'
            return best

    def best_move_o(self, board):
        best_val = -1000
        best_move = (-1, -1)

        # Traverse all cells, evaluate minimax function for
        # all empty cells. And return the cell with optimal
        # value.
        for i in range(3):
            for j in range(3):

                if board[i][j] == '_':

                    # Make the move
                    board[i][j] = 'O'

                    # compute evaluation function for this
                    # move.
                    move_val = self.minimax_alg_o(board, 0, False)

                    # Undo the move
                    board[i][j] = '_'

                    # If the value of the current move is
                    # more than the best value, then update
                    # best/
                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val
        return best_move

    def medium_x(self):
        if self.opt[0] == 'ai' and self.level[0] == 'medium':
            print('Making move level "medium"')
            while True:
                self.coord_ai_easy()
                if self.loop_looking():
                    self.medium_alg_x()
                    self.counter += 1
                    print(self.__str__())
                    if self.game_state():
                        exit()
                    break
                elif self.grid[self.x][self.y] == ['X', 'O']:
                    continue

    def medium_o(self):
        if self.opt[1] == 'ai' and self.level[1] == 'medium':
            print('Making move level "medium"')
            while True:
                self.coord_ai_easy()
                if self.loop_looking():
                    self.medium_alg_o()
                    self.counter += 1
                    print(self.__str__())
                    if self.game_state():
                        exit()
                    break
                elif self.grid[self.x][self.y] == ['X', 'O']:
                    continue

    def hard_x(self):
        if self.opt[0] == 'ai' and self.level[0] == 'hard':
            print('Making move level "hard"')
            while True:
                self.coord_ai_easy()
                if self.loop_looking():
                    x = self.best_move_x(self.grid)[0]
                    y = self.best_move_x(self.grid)[1]
                    self.grid[x][y] = 'X'
                    self.counter += 1
                    print(self.__str__())
                    if self.game_state():
                        exit()
                    break
                elif self.grid[self.x][self.y] == ['X', 'O']:
                    continue

    def hard_o(self):
        if self.opt[1] == 'ai' and self.level[1] == 'hard':
            print('Making move level "hard"')
            while True:
                self.coord_ai_easy()
                if self.loop_looking():
                    x = self.best_move_o(self.grid)[0]
                    y = self.best_move_o(self.grid)[1]
                    self.grid[x][y] = 'O'
                    self.counter += 1
                    print(self.__str__())
                    if self.game_state():
                        exit()
                    break
                elif self.grid[self.x][self.y] == ['X', 'O']:
                    continue

    def user_o(self):
        if self.opt[1] == 'user':
            while True:
                self.coord_user()
                if not 1 <= self.y <= 3 or not 1 <= self.x <= 3:
                    print("Coordinates should be from 1 to 3!\n")
                    continue
                elif self.grid[self.y - 1][self.x - 1] != "_":
                    print("This cell is occupied! Choose another one!\n")
                    continue
                else:
                    self.grid[self.y - 1][self.x - 1] = 'O'
                    self.counter += 1
                    print(self.__str__())
                    if self.game_state():
                        exit()
                    break

    def user_x(self):
        if self.opt[0] == 'user':
            while True:
                self.coord_user()
                if not 1 <= self.y <= 3 or not 1 <= self.x <= 3:
                    print("Coordinates should be from 1 to 3!\n")
                    continue
                elif self.grid[self.y - 1][self.x - 1] != "_":
                    print("This cell is occupied! Choose another one!\n")
                    continue
                else:
                    self.grid[self.y - 1][self.x - 1] = 'X'
                    self.counter += 1
                    print(self.__str__())
                    if self.game_state():
                        exit()
                    break

    def move_ux(self, turn):
        if turn == 'user':
            self.user_x()

    def move_uo(self, turn):
        if turn == 'user':
            self.user_o()

    def move_aix(self, turn):
        if turn == 'ai':
            self.easy_x()
            self.medium_x()
            self.hard_x()

    def move_aio(self, turn):
        if turn == 'ai':
            self.easy_o()
            self.medium_o()
            self.hard_o()

    def winning(self):
        win = ["".join(self.grid[0]), "".join(self.grid[1]), "".join(self.grid[2]),
               "".join([self.grid[0][0], self.grid[1][0], self.grid[2][0]]),
               "".join([self.grid[0][1], self.grid[1][1], self.grid[2][1]]),
               "".join([self.grid[0][2], self.grid[1][2], self.grid[2][2]]),
               "".join([self.grid[0][0], self.grid[1][1], self.grid[2][2]]),
               "".join([self.grid[0][2], self.grid[1][1], self.grid[2][0]])]
        return win

    def win_x(self):
        for i in self.winning():
            if i.count("X") == 3:
                self.counter += 10
                print("X wins")
                exit()

    def win_o(self):
        for i in self.winning():
            if i.count("O") == 3:
                self.counter += 10
                print("O wins")
                exit()

    def draw(self):
        for i in self.winning():
            if i != '_':
                if self.counter == 9:
                    if i.count("O") != 3:
                        if i.count("X") != 3:
                            print("Draw!")
                            exit()
                        else:
                            return self.win_x()
                    else:
                        return self.win_o()

    def game_state(self):
        self.win_x()
        self.win_o()
        self.draw()
        return False

    def __str__(self):
        out = "---------\n"
        for i in range(len(self.grid)):
            out += f"| {' '.join(self.grid[i])} |\n"
        out += "---------"
        return out


def change_turn(turn):
    if turn == s.opt[0]:
        return s.opt[1]
    if turn == s.opt[1]:
        return s.opt[0]


s = TicTacToe()
s.commands_users()
s.game_state()

turn = s.opt[0]
while True:

    s.move_ux(turn)
    s.move_aix(turn)
    s.move_uo(turn)
    s.move_aio(turn)
    s.find_index()
    if s.game_state():
        exit()
    turn = change_turn(turn)
