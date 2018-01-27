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

    writeLine('class ' + fileJSON["subtype"] + '(pygame.sprite.Sprite):\n')
    writeLine('\tdef __init__(self):\n')
    writeLine('\t\tpygame.sprite.Sprite.__init__(self)\n') 
    writeLine('\t\tself.x = 0\n\t\tself.y=0\n')
    writeLine('\t\tself.image="' + fileJSON["imagePath"] + '"\n')
    
    writeLine('\t\tself.src_image=pygame.image.load(self.image)\n')
    writeLine('\t\tself.name="' + fileJSON['name'] + '"\n')
    writeLine('\t\tself.position= (self.x, self.y)')
    writeLine('\t\tprint("import Successful")\n') 
 



    if fileJSON["type"] == 'character':
        print("character type")
        writeLine('\t\tself.health="' + fileJSON['health'] + '"\n')
        writeLine('\t\tself.speed="' + fileJSON['speed'] + '"\n')
        writeLine('\t\tself.activeItem=None\n')
        writeLine('\t\tself.items=[' + ', '.join(fileJSON['items']) + ']\n')
        writeLine('\n')
        writeLine('\tdef equipItem(self, item):\n')
        writeLine('\t\tself.items.append(item)\n')
        writeLine('\n')
        writeLine('\tdef move(self, xDir, yDir):\n')
        writeLine('\t\tself.x += self.speed * xDir\n')
        writeLine('\t\tself.y += self.speed * yDir\n')
        writeLine('\t\tself.position = (self.x, self.y)\n')
        
        writeLine('\n')
        writeLine('\tdef useActiveItem(self):\n')
        writeLine('\t\tself.activeItem.use()\n')
        writeLine('\n')
    elif fileJSON["type"] == 'item':
        print("item type")
        writeLine('\t\tself.weaponType="' + fileJSON['weaponType'] + '"\n')
        writeLine('\t\tself.consumable="' + fileJSON['consumable'] + '"\n')
        writeLine('\t\tself.ammo="' + fileJSON['ammo'] + '"\n')
        writeLine('\t\tself.damage="' + fileJSON['damage'] + '"\n')
        writeLine('\t\tself.effects=' + fileJSON['effects'] + '\n')
        writeLine('\n')
        writeLine('\tdef use(self):\n')
        writeLine('\t\tprint("used item")\n')
        writeLine('\n')
        writeLine('\tdef addEffect(self):\n')
        writeLine('\t\tprint("used item")\n')
    elif fileJSON["type"] == 'environment':
        print("environment type")
        writeLine('\t\tself.destructable="' + fileJSON['destructable'] + '"\n')
        writeLine('\t\tself.items=[' + ', '.join(fileJSON['items']) + ']\n')
        writeLine('\t\tself.cover=' + fileJSON['cover'] + '\n')
        writeLine('\n')
        writeLine('\tdef equipItem(self, item):\n')
        writeLine('\t\tself.items.append(item)\n')
        writeLine('\n')
        writeLine('\tdef move(self, xDir, yDir):\n')
        writeLine('\t\tself.x += self.speed * xDir\n')
        writeLine('\t\tself.y += self.speed * yDir\n')
        writeLine('\n')
        writeLine('\tdef useActiveItem(self):\n')
        writeLine('\t\tself.activeItem.use()\n')
        writeLine('\n')

    writeLine('\tdef drawGEN(self):\n')
    writeLine('\t\twindow.blit(self.image, (self.x, self.y))\n')
    writeLine('\n')

    classFile.close()

    return 1

readSheets()
