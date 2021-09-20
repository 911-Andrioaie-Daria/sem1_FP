class UI:
    def __init__(self, game):
        self._game_service = game

    @property
    def game_service(self):
        return self._game_service

    def print_board(self):
        board_of_game = self.game_service.get_game_board
        print(board_of_game)

    def is_game_won(self):
        return self.game_service.is_game_won()

    def is_game_draw(self):
        return self.game_service.is_game_draw()

    @staticmethod
    def read_user_move():
        user_choice_of_column = int(input('Enter the column on which you want to place your move: '))
        return user_choice_of_column - 1

    def start(self):
        is_human_turn = True
        while not self.is_game_won() and not self.is_game_draw():
            self.print_board()
            print('\n')
            print('\n')
            if is_human_turn:
                try:
                    users_choice = self.read_user_move()
                    self.game_service.make_human_move(users_choice)
                    print('Your move:')
                except Exception as exception_message:
                    print(exception_message)
                    is_human_turn = not is_human_turn # give the human player anther chance to make a valid move
            else:
                self.game_service.make_computer_move()
                print('Computer move:')

            is_human_turn = not is_human_turn

        self.print_board()

        if self.is_game_won() == 'X':
            print('You won!')
        elif self.is_game_won() == '0':
            print('You can try again. The computer won this time.')
        elif self.is_game_draw():
            print('Looks like there are no other moves available')