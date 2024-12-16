# 9.2
import pygame
import sys


def start(WIDTH, HEIGHT, screen, clock, color):
    font = pygame.font.Font(None, 74)
    title = font.render("Atari Pong", True, color[1])
    option1 = font.render("Player vs Player", True, color[2])
    option2 = font.render("Player vs Computer", True, color[2])
    button1 = pygame.Rect(WIDTH // 2 - 225, HEIGHT // 2 - 50, 455, 50)
    button2 = pygame.Rect(WIDTH // 2 - 275, HEIGHT // 2 + 50, 550, 50)

    mode = None
    while mode is None:
        screen.fill(color[0])
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
        pygame.draw.rect(screen, color[0], button1)
        pygame.draw.rect(screen, color[0], button2)

        screen.blit(option1, (WIDTH // 2 - option1.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(option2, (WIDTH // 2 - option2.get_width() // 2, HEIGHT // 2 + 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    mode = 1
                elif button2.collidepoint(event.pos):
                    mode = 2

        pygame.display.flip()
        clock.tick(60)
    return mode


def draw(WIDTH, HEIGHT, screen, color, player1, player2, ball, score1, score2):
    screen.fill(color[0])
    pygame.draw.rect(screen, color[1], player1)
    pygame.draw.rect(screen, color[1], player2)
    pygame.draw.ellipse(screen, color[2], ball)
    pygame.draw.aaline(screen, color[4], (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    font = pygame.font.Font(None, 36)
    text = font.render(f"{score1} - {score2}", True, color[3])
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 20))
