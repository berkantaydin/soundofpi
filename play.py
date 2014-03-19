import pygame
import time
import sys

pygame.init()

sounds = []
for i in range(1,10):
    sound = pygame.mixer.Sound('sounds_default/Piano1%s.ogg'%i)
    #sound.play()
    sounds.append(sound)

i = 22 #(division 3 and mod 1)
while i != 0:
	if i < 7:
		i *= 10

	play = i / 7
	i = i % 7
	sounds[i-1].play()
	sys.stdout.write("%s" % play)
	sys.stdout.flush()
	time.sleep(.7)


