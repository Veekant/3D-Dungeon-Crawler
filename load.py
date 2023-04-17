'''
this file will handle loading the map, images, and sounds

TO DO:
load textures (TP2/3)
load sounds (TP3)
'''

# loads a map from the mapID
def loadMap(mapID):
    map = []
    # open map file
    fileName = 'levels/' + mapID + '.txt'
    mapFile = open(fileName, 'r')
    # loop through each row
    for rowText in mapFile:
        textRow = rowText.strip().split()
        # loop through each col
        mapRow = []
        for i in range(len(textRow)):
            # cast string to int and add to list
            mapRow.append(int(textRow[i]))
        map.append(mapRow)
    mapFile.close()
    return map