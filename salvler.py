import json

def lercatg():
    catg = open("catalogo.json", 'r')
    catalogo = catg.read()
    return json.loads(catalogo)

def salvarcatag(catalogo: list):
    catg = open("catalogo.json", 'w+')
    catalogo = json.dumps(catalogo, indent=4)
    catg.write(catalogo)
    catg.close()