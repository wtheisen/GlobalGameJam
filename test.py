import pygame,math,sys , os
import imp
from pygame.locals import *





print("hello")
screen = pygame.display.set_mode((1024, 768))


#alien = pygame.image.load('alien.png')
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


modules = {}

classFolder = "./classes/"
for filename in os.listdir(classFolder):
        if filename.endswith('.py'):
                pathname = os.path.join(classFolder, filename)
                print (pathname)
                print (filename)
                #importlib.import_module(pathname.split(".")[0], package=filename.split(".")[0])
                modules[filename.split(".")[0]]= imp.load_source(filename.split(".")[0], pathname)

print ("current imports\n")
print(sys.modules.keys())

rect = screen.get_rect()

blonic  = modules["playerblonicClass"].playerblonicClass()




blonic_group = pygame.sprite.RenderPlain(blonic)


while 1:
        #aksjfl;aksjd
        clock.tick(FRAMES_PER_SECOND)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
                blonic.move(0,-1)
        if keys[pygame.K_s]:
                blonic.move(0,1)
        if keys[pygame.K_d]:
                blonic.move(1,0)
        if keys[pygame.K_a]:
                blonic.move(-1,0)
        

        for event in pygame.event.get():
                if event.type == KEYDOWN:
                        if event.key == K_w:
                                blonic.move(0,-1)
                                print ("blonic")


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
        #blonic_group.update(deltat)
        blonic_group.draw(screen)
        
        print(blonic.position)
            
        pygame.display.flip()

        pygame.event.pump()




#screen = pygame.display.set_mode((1024,768),FULLSCREEN)
