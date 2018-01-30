#utility functions for test.py
from collections import defaultdict

def createClasses():
    import sheetParser
    sheetParser.readSheets()

    return True

def importClasses():
    import os, imp

    temp = {}
    modules = defaultdict(list)

    classFolder = "./classes/"
    for filename in os.listdir(classFolder):
        if filename.endswith('.py'):
            pathname = os.path.join(classFolder, filename)
            print (pathname)
            print (filename)
            modName = filename.split('.')[0]
            #importlib.import_module(pathname.split(".")[0], package=filename.split(".")[0])
            temp[modName] = imp.load_source(modName, pathname)
            modules[temp[modName].getSubType()].append(temp[modName])

    return modules

def checkPointCol(x, y, sceneObjects):
    #return False
    print ("checking stuff")
    print (sceneObjects)
    for key, val in sceneObjects.items():
        for obj in val:
            print (obj)
            if obj.rect.collidepoint(x, y):
                if key == 'enemy':
                    obj.health -= 1
                    print ("hit enemy")
                    return True
                #else:
                #    return True

    return False

def checkCol(startX, startY, endX, endY, sceneObjects):
    #figure out the line equation here
    print ("checking col")
    deltaY = float(endY - startY)
    deltaX = float(endX - startX)
    interval = 5
    x=float(startX)
    y=float(startY)
    #m = (endY - startY) / (float)(endX - startX)
    #b = startY - m * startX

    for i in range(0, interval):
        x+=(deltaX/interval)
        y+=(deltaY/interval)    
        #y = m * x + b
        print(x)
        if checkPointCol(x, y, sceneObjects):
            return

