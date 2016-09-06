from lib2to3.refactor import _EveryNode
import pygame
import random

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 255)

# defines
WIDTH = 800
HEIGHT = 600
delta = 10
FPS = 12

pygame.init()
# globals
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Slither')

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

def snake(delta, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], delta, delta])

def msg_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [HEIGHT / 2, WIDTH / 2])

def get_new_apple():
    rand_x_apple = round(random.randrange(0, WIDTH - delta) / 10.0) * 10.0
    rand_y_apple = round(random.randrange(0, HEIGHT - delta) / 10.0) * 10.0
    return (rand_x_apple,rand_y_apple)

def gameLoop():
    snakeList = []
    snakeLength=1
    gameExit = False
    gameOver = False
    lead_x = HEIGHT / 2
    lead_y = WIDTH / 2
    lead_x_ch = 0
    lead_y_ch = 0
    apple=get_new_apple()

    while not gameExit:
        while gameOver:
            gameDisplay.fill(white)
            msg_to_screen('Game over, press c to play again, q to quit', blue)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # event handeler is thisc
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_ch = -delta
                    lead_y_ch = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_ch = delta
                    lead_y_ch = 0
                elif event.key == pygame.K_UP:
                    lead_y_ch = -delta
                    lead_x_ch = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_ch = delta
                    lead_x_ch = 0

            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #         lead_x_ch = 0
            #         lead_y_ch = 0

        # logics


        if lead_x < 0 or lead_x >= WIDTH or lead_y < 0 or lead_y >= HEIGHT:
            gameOver = True

        lead_x += lead_x_ch
        lead_y += lead_y_ch

        gameDisplay.fill(white)

        if lead_x_ch or lead_y_ch:  #only if the snake is moving, now the snake is not moving
            snakeHead=[]
            snakeHead.append(lead_x)
            snakeHead.append(lead_y)
            snakeList.append(snakeHead)
            if len(snakeList)>snakeLength:
                del snakeList[0]


        if not gameExit:
            pygame.draw.rect(gameDisplay, red, [apple[0], apple[1], delta, delta])
            snake(delta, snakeList)

        if (lead_x == apple[0] and lead_y == apple[1]):
            apple=get_new_apple()
            snakeLength+=1

        pygame.display.update()
        clock.tick(FPS)

def main():


    gameLoop()
    pygame.quit()
    quit()



main()