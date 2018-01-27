# Utility functions for reading in and parsing the stat sheets
# Author - William Theisen

import os, json

statsFolder = './stats/'

def readSheets():
    for filename in os.listdir(statsFolder):
        if filename.endswith('.stat'):
            filePath = os.path.join(statsFolder, filename)
            with open(filePath) as f:
                fileJSON = json.load(f)

            createClass(filePath, fileJSON)
        else:
            continue

def createClass(filePath, fileJSON):
    print('File path: ', filePath)
    print("File Contents:")

    classFileName = fileJSON["subtype"] + fileJSON["name"] + 'Class.py'
    classFile = open('./classes/' + classFileName, 'w')

    def writeLine(line):
        classFile.write(line)
        return

    writeLine('import pygame, math\n')
    writeLine('class  objectClass(pygame.sprite.Sprite):\n')
    writeLine('    @staticmethod\n')
    writeLine('    def getSubType():\n')
    writeLine('        return ' +fileJSON["subtype"]+'\n')
    writeLine('    def __init__(self):\n')
    writeLine('        pygame.sprite.Sprite.__init__(self)\n')
    writeLine('        self.x = 100\n        self.y=100\n')
    writeLine('        self.imagePath="' + fileJSON["imagePath"] + '"\n')

    writeLine('        self.src_image=pygame.image.load(self.imagePath)\n')
    writeLine('        self.name="' + fileJSON['name'] + '"\n')
    writeLine('        self.position= (self.x, self.y)\n')
    writeLine('        print("import Successful")\n')

    writeLine('        self.image=self.src_image\n')
    writeLine('        self.rect=self.src_image.get_rect()\n')
    writeLine('        self.objectID=' + fileJSON['objectID'] + '\n')
    writeLine('        self.instanceID=' + fileJSON['instanceID'] + '\n')
    writeLine('        self.screen=None\n')



    if fileJSON["type"] == 'character':
        print("character type")
        writeLine('        self.health=' + fileJSON['health'] + '\n')
        writeLine('        self.speed=' + fileJSON['speed'] + '\n')
        writeLine('        self.activeItem=None\n')
        writeLine('        self.items=[' + ', '.join(fileJSON['items']) + ']\n')
        writeLine('\n')
        writeLine('    def equipItem(self, item):\n')
        writeLine('        self.items.append(item)\n')
        writeLine('\n')
        writeLine('    def move(self, xDir, yDir):\n')
        writeLine('        self.x += self.speed * xDir\n')
        writeLine('        self.y += self.speed * yDir\n')
        writeLine('        self.position = (self.x, self.y)\n')
        writeLine('        self.rect.center = self.position\n')
        writeLine('        if self.activeItem != None:\n')
        writeLine('            self.activeItem.position = self.position\n')


        writeLine('\n')
        writeLine('    def useActiveItem(self):\n')
        writeLine('        if self.activeItem == None:\n')
        writeLine('            return\n')
        writeLine('        self.activeItem.use()\n')
        writeLine('\n')

        writeLine('    def faceMouse(self):\n')
        writeLine('        mouseX, mouseY = pygame.mouse.get_pos()\n')
        writeLine('        rotAngle = math.atan2(self.y - mouseY, mouseX - self.x)\n')
        writeLine('        rotAngle = math.degrees(rotAngle)\n')
        writeLine('        self.image = pygame.transform.rotate(self.src_image, rotAngle)\n')



    elif fileJSON["type"] == 'item':
        print("item type")
        writeLine('        self.weaponType="' + fileJSON['weaponType'] + '"\n')
        writeLine('        self.consumable=' + fileJSON['consumable'] + '\n')
        writeLine('        self.ammo=' + fileJSON['ammo'] + '\n')
        writeLine('        self.damage=' + fileJSON['damage'] + '\n')
        writeLine('        self.effects=' + fileJSON['effects'] + '\n')
        writeLine('\n')
        writeLine('    def use(self):\n')
        writeLine('        print("used item")\n')
        writeLine('        self.addEffect()\n')
        writeLine('\n')
        writeLine('    def addEffect(self):\n')
        writeLine('        print("drawing a light line")\n')
        writeLine('        mouseX, mouseY = pygame.mouse.get_pos()\n')
        writeLine('        self.x, self.y = self.position\n')
        writeLine('        deltaX = mouseX -self.x\n')
        writeLine('        deltaY = mouseY -self.y\n')
        writeLine('        screenY = self.screen.get_height()\n')
        writeLine('        while (mouseY < screenY) and (mouseY > 0):\n')
        writeLine('            mouseY +=deltaY\n')
        writeLine('            mouseX +=deltaX\n')
        writeLine('        pygame.draw.line(self.screen, (200,200,200), self.position, (mouseX,mouseY), 9)\n')

    elif fileJSON["type"] == 'environment':
        print("environment type")
        writeLine('        self.destructable=' + fileJSON['destructable'] + '\n')
        writeLine('        self.items=[' + ', '.join(fileJSON['items']) + ']\n')
        writeLine('        self.cover=' + fileJSON['cover'] + '\n')
        writeLine('        self.health=' + fileJSON['health'] + '\n')
        writeLine('\n')
        writeLine('    def equipItem(self, item):\n')
        writeLine('        self.items.append(item)\n')
        writeLine('\n')
        writeLine('    def move(self, xDir, yDir):\n')
        writeLine('        self.x += self.speed * xDir\n')
        writeLine('        self.y += self.speed * yDir\n')
        writeLine('\n')
        writeLine('    def useActiveItem(self):\n')
        writeLine('        self.activeItem.use()\n')
        writeLine('\n')

    writeLine('    def drawGEN(self):\n')
    writeLine('        window.blit(self.image, (self.x, self.y))\n')
    writeLine('\n')

    writeLine('def getSubType():')
    writeLine('    return "'+fileJSON["subtype"] +'"\n')
    writeLine('\n')


    classFile.close()

    return 1

readSheets()
