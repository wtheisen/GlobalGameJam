import os, math, pygame
from pygame.locals import *
from pygame.compat import geterror

def load_image(name):
    try:
         image = pygame.image.load(name)
    except:
         print "failed to load image: " + name

    image = image.convert()
    return image, image.get_rect()

class GameSpace:
    def main(self):
        pygame.init()
        self.size = self.width, self.height = 640, 420
        self.black = 0, 0, 0
        self.screen = pygame.display.set_mode(self.size)

        self.player = Player()
        self.clock = pygame.time.Clock()

        while True:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    self.player.move(event.key)

            self.player.tick()

            self.screen.fill(self.black)
            self.screen.blit(self.player.image, self.player.rect)
            pygame.display.flip()

    def load_image(name):
        try:
            image = pygame.image.load(name)
        except:
            print "failed to load image: " + name
        image = image.convert()

        return image, image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('death.png')
        self.unrotated_image, temp = load_image('death.png')
        self.playerX = 0
        self.playerY = 0
        self.rotAngle = 0
        self.faceMouse()

    def tick(self):
        #update the player
        return None

    def createLaser(self, startX, startY):
        print "pew pew"

    def move(self, k):
        if k == pygame.K_LEFT:
            self.playerX = self.playerX - 1
        elif k == pygame.K_RIGHT:
            self.playerX = self.playerX + 1
        elif k == pygame.K_UP:
            self.playerY = self.playerY - 1
        elif k == pygame.K_DOWN:
            self.playerY = self.playerY + 1
        elif k == pygame.K_SPACE:
            self.createLaser(self.playerX, self.playerY)

        self.rect = (self.playerX, self.playerY)
        self.faceMouse()

    def faceMouse(self):
        mouseX, mouseY = pygame.mouse.get_pos()

        rotAngle = math.atan2(self.playerY - mouseY, mouseX - self.playerX)
        rotAngle = -math.degrees(rotAngle)
        self.image = pygame.transform.rotate(self.unrotated_image, rotAngle)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('death.png')
        self.unrotated_image, temp = load_image('death.png')

    def tick(self):
        #update the player
        return None

if __name__ == "__main__":
    gs = GameSpace()
    gs.main()

