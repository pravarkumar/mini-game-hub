import pygame
import numpy as np
import sys
from games.base import Game
class TicTacToe(Game):
    def __init__(self,player1,player2):
        self.bgcolor =(28, 170, 156)
        self.ROWS=10
        self.COLS=10
        self.linecolor =(0, 0, 0)
        self.xcolor =(66, 66, 66)
        self.ocolor =(255, 255, 255)
        self.cellsize =82  # each cell is now 240x240
        self.width =self.cellsize*self.ROWS    # board width
        self.height =self.cellsize*self.COLS     # board height
        self.board = np.zeros((self.ROWS,self.COLS))
        self.current_player =player1
        self.player1 =player1
        self.player2 =player2

    def drawgrid(self, screen):
        screen.fill(self.bgcolor)
        for i in range(1,self.COLS):
            pygame.draw.line(screen,self.linecolor,(self.cellsize*i,0),(self.cellsize*i,self.height),2)
        for i in range(1,self.ROWS):
            pygame.draw.line(screen,self.linecolor,(0,i*self.cellsize),(self.width,i*self.cellsize),2)

    def drawmarks(self, screen):
        for row in range(10):
            for col in range(10):
                x = col*self.cellsize
                y = row*self.cellsize
                if self.board[row][col]==1:
                    pygame.draw.line(screen, self.xcolor, (x+20,y+20),(x+self.cellsize-20,y+self.cellsize-20),5)
                    pygame.draw.line(screen, self.xcolor, (x+self.cellsize-20,y+20),(x+20,y+self.cellsize-20),5)
                elif self.board[row][col]==2:
                    pygame.draw.circle(screen, self.ocolor, (x+self.cellsize//2, y+self.cellsize//2), self.cellsize//3,5)

    def makemove(self,row,col):
        if self.board[row][col]==0:
            if self.current_player==self.player1:
                self.board[row][col]=1
            else:
                self.board[row][col]=2
            return True
        return False

    def checkwin(self,player):
        if player==self.player1:
            b=(self.board==1)  #convert to True/False grid
        else:
            b=(self.board==2)

        #Horizontal
        h=b[:,:-4] & b[:,1:-3] & b[:,2:-2] & b[:,3:-1] & b[:,4:]

        #Vertical 
        v=b[:-4,:] & b[1:-3,:] & b[2:-2,:] & b[3:-1,:] & b[4:,:]

        #Diagonal 
        d1=b[:-4,:-4] & b[1:-3,1:-3] & b[2:-2,2:-2] & b[3:-1,3:-1] & b[4:,4:]

        #Diagonal 
        d2=b[:-4,4:] & b[1:-3,3:-1] & b[2:-2,2:-2] & b[3:-1,1:-3] & b[4:,:-4]

        return np.any(h) or np.any(v) or np.any(d1) or np.any(d2)

    def isdraw(self):
        return np.all(self.board!=0)

    def end_screen(self, screen, winner):
        # Simple end screen with Play Again and Menu
        endimage_path="images/win_screen.jpeg"
        backg=pygame.image.load(endimage_path)
        backg=pygame.transform.scale(backg,(825,825))
        
        screen.fill((26, 26, 46))
        font=pygame.font.SysFont("freesans",40)
        


        if winner != "draw":
            text = font.render(f"{winner}  HAS WON  THE GAME!", True, (255,255,0))
        else:
            text = font.render("ITS A DRAW!", True, (255,255,0))
        screen.blit(backg, (0,0))
        
        # Buttons
        playrect=pygame.Rect(48,420,729,167)
        quitrect=pygame.Rect(49,603,729,193)

        textbox=pygame.Rect(50,226,719,172)
        textbox1=pygame.Rect(50,226,669,144)
        pygame.draw.rect(screen,(20,13,47),textbox1)
        
        
        
        text_rect=text.get_rect(center=textbox.center)
        
        screen.blit(text, text_rect)
        
        
        
        pygame.display.update()
        waiting=True
        while waiting:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=event.pos
                    if playrect.collidepoint(pos):
                        
                        return "playagain"
                    elif quitrect.collidepoint(pos):
                        return "quit"