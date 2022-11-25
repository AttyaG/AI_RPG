import mainCharacter as mc
import globalMap as gMap
import gui


def go(player, gb, place):
    places = gb.getPlaces()
    if place in places:
        if player.getCL() in gb.places[place]:
            player.setCurrentLocation(place)
            print(f'going to {place}')
            print('change window etc')
        else:
            print(f'unable to go to {place}')
    else:
        print(f'There no {place}')
        

if __name__ == '__main__':
    print('start')
    gb = gMap.GlobalMap()
    player = mc.MainCharacter()
    go(player, gb, 'home')
    app = gui.QApplication([])
    qss="style.qss"
    with open(qss,"r") as fh:
        app.setStyleSheet(fh.read())

    window = gui.MainMenu()
    window.show()

    app.exec()
