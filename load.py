'''
this file will handle loading the map, images, and sounds
'''

# loads a map from the mapID
# returns map, width, and height
def loadMap(mapID):
    map = []
    fileName = 'levels/' + mapID + '.txt'
    mapText = open(fileName, 'r')
    for rowText in mapText:
        mapRow = rowText.strip().split()
        map.append(mapRow)
    rows = len(map)
    cols = len(map[0])
    return map