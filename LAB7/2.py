import pygame
import os

pygame.init()

size = (400, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Music Player")

# Load music files
music_dir = "C:/Users/Admin/Desktop/LAB7/music"
music_files = os.listdir(music_dir)

def play_music(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

current_song = 0
play_music(os.path.join(music_dir, music_files[current_song]))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music(os.path.join(music_dir, music_files[current_song]))
            elif event.key == pygame.K_RIGHT:
                current_song = (current_song + 1) % len(music_files)
                stop_music()
                play_music(os.path.join(music_dir, music_files[current_song]))
            elif event.key == pygame.K_LEFT:
                current_song = (current_song - 1) % len(music_files)
                stop_music()
                play_music(os.path.join(music_dir, music_files[current_song]))