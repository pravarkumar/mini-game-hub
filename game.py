import numpy as np #we need to create boards 

class Game:#common to all games things like switching winning and stuf
    def __init__(self, p1, p2, rows, cols): #constructor
        self.player1 = p1
        self.player2 = p2
        self.current_player = p1
        self.rows = rows
        self.cols = cols 
        self.board = np.zeroes((rows,cols),dtype = int)                                   #self-> this object itself 
    
    def swith_turn(self):
        #We will chnage turn after eah iteration 
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1                                   #4 parameters (player1,player2,rows,columns)
    
    def check_win(self):
        
