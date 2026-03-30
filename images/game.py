import pygame
import sys
import os
import subprocess

WIDTH = 800
HEIGHT = 850

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Game Hub")

clock = pygame.time.Clock()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, "menu2.png")

background = pygame.image.load(image_path)
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


buttons = {
    "shooter": pygame.Rect(83, 280, 628, 97),
    "othello": pygame.Rect(85, 392, 629, 99),
    "connect4": pygame.Rect(88, 502, 626, 101),
    "tictactoe": pygame.Rect(85, 615, 630, 99),
    "exit": pygame.Rect(83, 730, 632, 87),
}


glow_colors = {
    "shooter": (0, 0, 255),
    "othello": (0, 255, 0),
    "connect4": (255, 255, 0),
    "tictactoe": (255, 100, 0),
    "exit": (255, 0, 0),
}

def draw_glow(screen, rect, color):

    glow_surface = pygame.Surface(rect.size, pygame.SRCALPHA)

    for i in range(6, 0, -2):
        inner_rect = glow_surface.get_rect().inflate(-i * 4, -i * 4)

        pygame.draw.rect(
            glow_surface,
            (*color, 35),
            inner_rect,
            border_radius=20
        )

    screen.blit(glow_surface, rect.topleft)


def run_file(filename):
    file_path = os.path.join(BASE_DIR, filename)

    if not os.path.exists(file_path):
        print(f"{filename} not found!")
        return

    subprocess.run(["python3", file_path])


def main():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        hovered = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if buttons["exit"].collidepoint(pos):
                    pygame.quit()
                    sys.exit()

                elif buttons["tictactoe"].collidepoint(pos):
                    pygame.display.quit()
                    run_file("ticktacktoe.py")

                elif buttons["connect4"].collidepoint(pos):
                    pygame.display.quit()
                    run_file("connect4.py")

                elif buttons["othello"].collidepoint(pos):
                    pygame.display.quit()
                    run_file("othello.py")

                elif buttons["shooter"].collidepoint(pos):
                    pygame.display.quit()
                    run_file("shooter.py")


        for name, rect in buttons.items():
            if rect.collidepoint(mouse_pos):
                hovered = name
                break


        screen.blit(background, (0, 0))


        for name, rect in buttons.items():
            if name == hovered:
                draw_glow(screen, rect, glow_colors[name])


        if hovered:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
