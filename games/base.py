# Base Game Class
class Game:
    def __init__(self, current_player, player1, player2, row, col):
        self.player1 = player1
        self.player2 = player2
        self.board = np.zeros((row, col))
        self.current_player = player1

    def switch(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def check_win(self):
        raise NotImplementedError("Subclasses must implement this method")