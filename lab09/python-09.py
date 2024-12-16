# 9.2
from module_09 import *

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PING PONG")
clock = pygame.time.Clock()
colors = [
    (34, 37, 42),
    (187, 124, 205),
    (92, 173, 233),
    (137, 202, 120),
    (223, 193, 132)
]

ball_size = 15
paddle_width, paddle_height = 10, 100
player1 = pygame.Rect(20, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
player2 = pygame.Rect(WIDTH - 30, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, ball_size, ball_size)

player_speed, ai_speed = 7, 7
ball_speed_x, ball_speed_y = 5, 5
score1, score2 = 0, 0
max_points = 11

running = True
mode = start(WIDTH, HEIGHT, screen, clock, colors)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= player_speed
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += player_speed

    if mode == 1:
        if keys[pygame.K_UP] and player2.top > 0:
            player2.y -= player_speed
        if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
            player2.y += player_speed
    elif mode == 2:
        if ball.centery > player2.centery and player2.bottom < HEIGHT:
            player2.y += ai_speed
        if ball.centery < player2.centery and player2.top > 0:
            player2.y -= ai_speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1
        ball_speed_x *= 1.1
        ball_speed_y *= 1.1

    if ball.left <= 0:
        score2 += 1
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
        ball_speed_x = 5
        ball_speed_y = 5
        ball_speed_x *= -1
    if ball.right >= WIDTH:
        score1 += 1
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
        ball_speed_x = 5
        ball_speed_y = 5
        ball_speed_x *= -1

    if score1 == max_points:
        print("Player 1 wins!")
        running = False
    if score2 == max_points:
        print("Player 2 wins!")
        running = False

    draw(WIDTH, HEIGHT, screen, colors, player1, player2, ball, score1, score2)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
