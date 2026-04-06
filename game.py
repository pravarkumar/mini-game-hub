#Adding comments to make the code understandable + making changes i forgot the comments part :(
import pygame # ofc its for the game 
import sys # we took input from it and even exited the program + other things also
import os # folder paths and stuff can be accessed with this 
import subprocess #helps run commands in temrinal 
import numpy as np 
#import tictactoe from games.tictactoe 
 
WIDTH = 800
HEIGHT = 850

#I've just like defined the width and height of my screen the image we used for menu was such that it made sense to have height > width 

# __fil__ : Current file path

# os.path.abspath(__file__) Absolute path



pygame.init()      # wanted to start the system 
pygame.mixer.init()  # I learned that this makes the music system switch on I have access to sound effects now 

screen = pygame.display.set_mode((WIDTH, HEIGHT)) # basic command which makes the screen come of apt size we defined before 
pygame.display.set_caption("Mini Game Hub")   # This makes the top small heading of the screen which pops up as the menu 

clock = pygame.time.Clock() # The problem without this will be that the game will run at different frames per sec differently for differet computrs i wanted to make the game run same for all the 				local systems after i made changes later 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Already explined used to get the absolute path remove the problem of finding it always reduces unconvinience of trying to locate the current directory :) like ere we want the folder just outide of this file whose file path we have written 
image_path = os.path.join(BASE_DIR, "images/menu2.png")# the joinded absolute path 
background = pygame.image.load(image_path)# backgroudn image 
background = pygame.transform.scale(background, (WIDTH, HEIGHT))# adjusted the size of the backgroudn image 
# Now we will add the music  
music_path = os.path.join(BASE_DIR, "sound_effects", "menu_music.mp3")

if os.path.exists(music_path):
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(0.5)  # Adjust volume (0.0 to 1.0)
    pygame.mixer.music.play(-1)  # Loop forever
else:
    print("menu_music.mp3 not found!")

# THis is an inbuilt fucntion the "os.path.exists()" the usage is obv I and trying to make th edebugging of errors in the future easier  


# Time to make the buttons glow 
buttons = {
    "flappy_bird": pygame.Rect(83, 260, 634, 117),
    "othello": pygame.Rect(85, 386, 634,117),
    "connect4": pygame.Rect(84, 512, 634, 117),
    "tictactoe": pygame.Rect(85, 632, 634, 118),
    "exit": pygame.Rect(83, 765, 634, 117),
}
# defined the buttons 
glow_colors = {
    "flappy_bird": (0, 0, 255),
    "othello": (0, 255, 0),
    "connect4": (255, 255, 0),
    "tictactoe": (255, 100, 0),
    "exit": (255, 0, 0),
}
#gave them color 



def draw_glow(screen, rect, color):# we take input as the screen and the rect and the color 
    glow_surface = pygame.Surface(rect.size, pygame.SRCALPHA)  # In order to glow i used transperacy like pygame.SRCALPHA which makes the stuff transparent otherwie i would had got a colore drectangle in fron to the button and it would had been unelegant the surface here is abasically fot he same dimensons as the rect just that its transparent 

    for i in range(6, 0, -2): # i will equal to 6 4 2 
        inner_rect = glow_surface.get_rect().inflate(-i * 8, -i * 8)#makes rectangle of the apt size 

        pygame.draw.rect(# draw a rectangle 
            glow_surface,#on this surface 
            (*color, 35.67),# three argumets for the color and one for transperancy 0 for fully transparent and 255 for solid 
            inner_rect,# on which rectangle 
            border_radius=20# radius of the border 
        )

    screen.blit(glow_surface, rect.topleft) # Inbuilt fucntion used to draw things on another like here the first argument's top left corner will match to the second arg which is a pair of cord which i true as i gave the top left of the rect as input thius it gets drn on the rectangle perfectly 
# Obv we saw yt tutorial for this glowing thing :)

# this will allow us to execute different games
def run_file(filename):
    file_path = os.path.join(BASE_DIR, filename)# Told earlier 

    if not os.path.exists(file_path):
        print(f"{filename} not found!")# formatted string
        return

    subprocess.run(["python3", file_path])

# the main loop which will run throughout the life of the program 
def main():
    while True:# Standard for the pygame games will run throughout the life of the game 
        mouse_pos = pygame.mouse.get_pos()
        hovered = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:# basic event logic in pygame 
                pos = event.pos

                if buttons["exit"].collidepoint(pos):
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()

                elif buttons["tictactoe"].collidepoint(pos):
                    pygame.mixer.music.stop()
                    pygame.display.quit()
                    #run_file("tictactoe.py")
                

                elif buttons["connect4"].collidepoint(pos):
                    pygame.mixer.music.stop()
                    pygame.display.quit()
                    run_file("connect4.py")

                elif buttons["othello"].collidepoint(pos):
                    pygame.mixer.music.stop()
                    pygame.display.quit()
                    run_file("othello.py")

                elif buttons["flappy_bird"].collidepoint(pos):
                    pygame.mixer.music.stop()
                    pygame.display.quit()
                    run_file("flappy_bird.py")

        # Detect hover ad respond acc 
        for name, rect in buttons.items():
            if rect.collidepoint(mouse_pos):# We try to find the event of mouse pointing 
                hovered = name
                break
                
        # Draw background 

        screen.blit(background, (0, 0))

        # Draw glow on hover 
        for name, rect in buttons.items():
            if name == hovered: # mouse came over it 
                draw_glow(screen, rect, glow_colors[name]) # make it glow 

        # Change cursor
        if hovered:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)# nice detail fo like I wanted to make the cursor become hand like when it hovered so i did this 
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)# otherwise it remais arrow just like in all standard websites 

        pygame.display.update()# updated the screen after whtaever chages happened 
        clock.tick(60) # set to 60 frames per second 
class Game:
    def __init__(self,current_player,player1,player2,row,col):
        self.player1=player1
        self.player2=player2
        self.board=np.zeros((row,col))
        self.current_player=player1
    def switch(self) :
        if self.current_player==self.player1:
            self.current_player=self.player2
        else:
            self.current_player=self.player1
    def check_win(self):
        raise NotImplementedError("Subclasses must implement this method") # each game has their own winning condition 

if __name__ == "__main__":# Only use when used directly not as a support file 
    main()
