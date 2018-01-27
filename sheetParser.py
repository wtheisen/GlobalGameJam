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

    classFileName = fileJSON["type"] + 'Class.py'
    classFile = open(classFileName, 'w')

    def writeLine(line):
        classFile.write(line)
        return

    writeLine('class ' + fileJSON["subtype"] + '():\n')
    writeLine('\tdef __init__(self):\n')
    writeLine('\t\tself.x = 0\n\t\tself.y=0\n')
    writeLine('\t\tself.image="' + fileJSON["imagePath"] + '"\n')

    if fileJSON["type"] == 'character':
        print("character type")
    elif fileJSON["type"] == 'item':
        print("item type")

    classFile.close()

    return 1

readSheets()
