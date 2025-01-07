from main import *
stations : list = []
cards : list = []
lines : list = []


def prepare_stations() -> list:
    global stations
    
    stations.append(Station((0,0), "pentagon", 1, False, True))

    stations.append(Station((0,1), "triangle", 2, False, True))
    stations.append(Station((0,2), "square", 2, False, True))
    stations.append(Station((1,1), "pentagon", 2, False, True))
    stations.append(Station((2,0), "circle", 2, False, True))

    stations.append(Station((0,4), "triangle", 3, False, True))
    stations.append(Station((0,5), "circle", 3, False, True))
    stations.append(Station((1,3), "square", 3, False, True))
    stations.append(Station((1,6), "pentagon", 3, True, True))
    stations.append(Station((2,3), "triangle", 3, False, True))
    stations.append(Station((2,6), "square", 3, False, True))

    stations.append(Station((0,7), "triangle", 4, False, True))
    stations.append(Station((1,8), "square", 4, False, True))
    stations.append(Station((1,9), "pentagon", 4, False, True))
    stations.append(Station((2,9), "triangle", 4, False, True))

    stations.append(Station((0,9), "circle", 5, False, True))


    stations.append(Station((3,0), "square", 6, True, True))
    stations.append(Station((3,2), "pentagon", 6, False, True))
    stations.append(Station((4,1), "triangle", 6, False, False))
    stations.append(Station((4,2), "square", 6, False, False))
    stations.append(Station((5,0), "pentagon", 6, False, False))
    stations.append(Station((5,2), "square", 6, False, False))

    stations.append(Station((3,4), "triangle", 7, False, True))
    stations.append(Station((3,5), "any", 7, True, True))
    stations.append(Station((3,6), "circle", 7, False, True))
    stations.append(Station((4,4), "pentagon", 7, False, True))
    stations.append(Station((4,5), "square", 7, False, True))
    stations.append(Station((5,4), "circle", 7, False, True))
    stations.append(Station((6,3), "pentagon", 7, False, False))
    stations.append(Station((6,4), "triangle", 7, False, False))
    stations.append(Station((6,6), "square", 7, False, False))

    stations.append(Station((3,7), "circle", 8, False, True))
    stations.append(Station((3,9), "square", 8, False, True))
    stations.append(Station((4,8), "pentagon", 8, False, True))
    stations.append(Station((5,7), "circle", 8, False, False))
    stations.append(Station((6,7), "triangle", 8, False, False))
    stations.append(Station((6,9), "triangle", 8, True, False))

    stations.append(Station((7,0), "circle", 9, False, False))
    stations.append(Station((7,2), "square", 9, False, False))
    stations.append(Station((8,1), "circle", 9, False, False))
    stations.append(Station((9,1), "square", 9, False, False))

    stations.append(Station((7,3), "circle", 10, False, False))
    stations.append(Station((7,5), "pentagon", 10, False, False))
    stations.append(Station((8,6), "pentagon", 10, False, False))
    stations.append(Station((9,3), "pentagon", 10, False, False))
    stations.append(Station((9,4), "circle", 10, True, False))
    stations.append(Station((9,5), "triangle", 10, False, False))

    stations.append(Station((7,8), "circle", 11, False, False))
    stations.append(Station((7,9), "pentagon", 11, False, False))
    stations.append(Station((8,8), "triangle", 11, False, False))
    stations.append(Station((9,7), "circle", 11, False, False))

    stations.append(Station((9,0), "triangle", 12, False, False))

    stations.append(Station((9,9), "square", 13, False, False))
    return stations

def prepare_cards() -> list:
    global cards
    
    cards.append(Card("over", "triangle"))
    cards.append(Card("over", "circle"))
    cards.append(Card("over", "switch"))
    cards.append(Card("over", "square"))
    cards.append(Card("under", "circle"))
    cards.append(Card("over", "joker"))
    cards.append(Card("under", "triangle"))
    cards.append(Card("under", "joker"))
    cards.append(Card("under", "square"))
    cards.append(Card("under", "pentagon"))
    cards.append(Card("over", "pentagon"))
    return cards
    
def prepare_lines() -> list:
    global stations, lines
    
    for station in stations:
        if station.position == (2,3):
            lines.append(Line(station, "green"))
        elif station.position == (3,7):
            lines.append(Line(station, "pink"))
        elif station.position == (5,2):
            lines.append(Line(station, "purple"))
        elif station.position == (7,5):
            lines.append(Line(station, "blue"))
    
    return lines