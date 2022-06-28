import pygame

sound_file = '/home/pi/raspberrypi_cookbook_ed4/python/school_bell.wav'

pygame.mixer.init()
pygame.mixer.music.load(sound_file)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
    continue
