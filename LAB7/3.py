import pygame

pygame.init()

width = 600
height = 600

screen = pygame.display.set_mode((width, height))
ball_surface = pygame.Surface((50, 50), pygame.SRCALPHA)
pygame.draw.circle(ball_surface, (255, 0, 0), (25, 25), 25)

ball_x = (width - ball_surface.get_width()) // 2
ball_y = (height - ball_surface.get_height()) // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - 20, 0)
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + 20, height - ball_surface.get_height())
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - 20, 0)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + 20, width - ball_surface.get_width())

    screen.fill((255, 255, 255))
    screen.blit(ball_surface, (ball_x, ball_y))
    pygame.display.update()
