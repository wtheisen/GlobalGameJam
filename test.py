import pygame,math,sys
from pygame.locals import *





print("hello")
screen = pygame.display.set_mode((1024, 768))


alien = pygame.image.load('alien.png')
#
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 60
deltat = clock.tick(FRAMES_PER_SECOND)


speed = direction = 0

position = (100,100)

TURN_SPEED = 5

i=0


class PlayerSprite(pygame.sprite.Sprite):
	MAX_FORWARD_SPEED = 10
	MAX_REVERSE_SPEED = 10
	ACCERATION = 2
	TURN_SPEED = 5
	
	def __init__(self, image, position):
		pygame.sprite.Sprite.__init__(self)
		self.src_image = pygame.image.load(image)
		self.position = position
		self.speed = self.direction = 0


	
	def update(self, deltat):
		x, y = self.position	
		self.position = (x, y)
		self.image = pygame.transform.rotate(self.src_image, self.direction)	
		self.rect=self.image.get_rect()
		self.rect.center = self.position


import sheetParser
sheetParser.readSheets()

 
rect = screen.get_rect()

player = PlayerSprite('alien.png', rect.center)
player_group = pygame.sprite.RenderPlain(player)


while 1:
	#aksjfl;aksjd
	clock.tick(FRAMES_PER_SECOND)
	for event in pygame.event.get():		
		if event.type == KEYDOWN:
			if event.key == K_w:
				player.position = (0,0)
				## move character
						

		if event.type == 12:
			sys.exit(0)

		print (event)
	screen.fill((0,0,0))
	keypressed = pygame.key.get_pressed()
	if keypressed[pygame.K_ESCAPE]:
		print (keypressed)

	i+=1
	x=0
	y=0
	##rotated = pygame.transform.rotate(alien, 45* math.pi / 180)
	##screen.blit(rotated ,(i, 100)) 
	player_group.update(deltat)
	player_group.draw(screen)

	pygame.display.flip()

	pygame.event.pump()	
	
	


#screen = pygame.display.set_mode((1024,768),FULLSCREEN)
