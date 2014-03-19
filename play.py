import pygame
import time
import sys

pygame.init()

sounds = []
for i in range(1,10):
    sound = pygame.mixer.Sound('sounds_default/Piano1%s.ogg'%i)
    sound.play()
    sounds.append(sound)

#pygame.mixer.music.play()

i = 22 #(3 and mod 1)
a = 0;
while a < 5:
	a += 1
	if i < 7:
		#print i
		#play i
		i *= 10

	play = i / 7
	i = i % 7
	sys.stdout.write("%s" % play)
	sys.stdout.flush()
	time.sleep(1.0)


