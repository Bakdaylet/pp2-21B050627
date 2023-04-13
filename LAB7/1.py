import sys
import pygame
from datetime import datetime
import os

def degree(k):
    k -= 6
    return k

pygame.init()
W = 800
H = 800

screen = pygame.display.set_mode((W, H))
clock2 = pygame.image.load('Mikky2.png')
gato = pygame.transform.scale(clock2, (700, 500))
st = pygame.image.load('second_hand.png').convert_alpha()
st.set_colorkey((255, 255, 255))
st2 = pygame.image.load('minutes_hand.png').convert_alpha()
st2.set_colorkey((255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((250, 255, 255))
    screen.blit(gato, (50, 170))

    now = datetime.now()
    minute = now.minute
    second = now.second

    n = degree(second * -6)
    rot = pygame.transform.rotate(st, n)
    rot_rect = rot.get_rect(center=(400, 420))
    screen.blit(rot, rot_rect)

    k = degree(minute * -6)
    rot2 = pygame.transform.rotate(st2, k)
    rot_rect2 = rot2.get_rect(center=(400, 420))
    screen.blit(rot2, rot_rect2)

    pygame.display.update()
    pygame.time.delay(1000)
