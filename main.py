import pygame
import roj

# Constatnts, variables and objects
width = 30
height = 20
difficulty = 10

r = roj.roj(width, height, difficulty)

#pygame.init()
pygame.display.init()
pygame.font.init()

font = pygame.font.Font(pygame.font.get_default_font(), 25)
display = pygame.display.set_mode((width*27,height*27))
pygame.display.set_caption("Minesweeper")

def drawBoard(boardstate):
    for y in range(height):
        for x in range(width):
            if r.getRevealed(x, y):
                col = (128, 128, 128)
            else:
                col = (255, 255, 255)
            pygame.draw.rect(display, col, pygame.Rect(x*27, y*27, 25, 25))
            if boardstate[y][x] != "0" and boardstate[y][x] != " " and boardstate[y][x] != "*":
                display.blit(font.render(boardstate[y][x], True, (0, 0, 0)), (x*27+1, y*27+1))
            elif boardstate[y][x] == "*":
                display.blit(font.render("X", True, (0, 0, 0)), (x*27+1, y*27+1))


    pygame.display.flip()


loop = True
while loop:
    drawBoard(r.getBoardstate())
    pygame.event.pump()
    if pygame.mouse.get_pressed()[0]:
        (x, y) = pygame.mouse.get_pos()
        if x >= 0 and x < width*27 and y >= 0 and y < height*27:
            r.pick(int(x/27), int(y/27))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        loop = False

pygame.font.quit()
pygame.display.quit()
