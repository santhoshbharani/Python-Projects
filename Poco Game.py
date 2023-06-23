import pygame as py

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

py.init()

size = (800, 600)
screen = py.display.set_mode(size)
py.display.set_caption("Poco Game")

rect_x = 400
rect_y = 580

rect_change_x = 0
rect_change_y = 0

ball_x = 50
ball_y = 50

ball_change_x = 5
ball_change_y = 5

score = 0

def drawrect(screen, x, y):
    if x <= 0:
        x = 0
    if x >= 699:
        x = 699

    py.draw.rect(screen, RED, [x, y, 100, 20])

# Game main loop
done = False
clock = py.time.Clock()

while not done:
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True
        elif event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                rect_change_x = -6
            elif event.key == py.K_RIGHT:
                rect_change_x = 6
        elif event.type == py.KEYUP:
            if event.key == py.K_LEFT or event.key == py.K_RIGHT:
                rect_change_x = 0

    screen.fill(BLACK)

    rect_x += rect_change_x
    rect_y += rect_change_y

    ball_x += ball_change_x
    ball_y += ball_change_y

    if ball_x < 0 or ball_x > 785:
        ball_change_x = -ball_change_x
    elif ball_y < 0:
        ball_change_y = -ball_change_y
    elif ball_y > rect_y and ball_x > rect_x and ball_x < rect_x + 100:
        ball_change_y = -ball_change_y
        score += 1
    elif ball_y > 600:
        ball_change_y = -ball_change_y
        score = 0

    py.draw.rect(screen, WHITE, [ball_x, ball_y, 15, 15])
    drawrect(screen, rect_x, rect_y)

    font = py.font.SysFont("Calibri", 30, False, False)
    text = font.render("Score = " + str(score), True, WHITE)
    screen.blit(text, [370, 10])

    py.display.flip()
    clock.tick(60)

py.quit()
