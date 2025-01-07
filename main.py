import neighbors
import preparation

import copy
import random

class Station():
    def __init__(self, position : tuple, shape : str, district : int, attraction : bool, above_themse : bool) -> None:
        self.position = position
        self.shape = shape
        self.district = district
        self.attraction = attraction
        self.above_themse = above_themse
        
        self.neighbor = []
        self.previous = None
        self.next = None
        
    def setPrevious(self, station) -> None:
        if station in self.neighbor:
            self.previous = station
    
    def setNext(self, station) -> None:
        if station in self.neighbor or station == None:
            self.next = station
    
    def addNeighbor(self, station ) -> None:
        if not station in self.neighbor:
            self.neighbor.append(station)
        
    def addNeighborList(self, stations : list) -> None:
        for station in stations:
            self.addNeighbor(station)

class Line():
    def __init__(self, start , color : str, choose_mode : str = "random") -> None:
        self.color = color
        self.choose_mode = choose_mode
        
        self.ends : list = [start]
        self.stations = [start]
    
    def addStation(self, new_station, current_station) -> None:
        self.stations.append(new_station)
        
        if len(self.ends) > 1:
            self.ends.remove(current_station)
        else:
            current_station.setPrevious(new_station)
        
        self.ends.append(new_station)
        
        current_station.setNext(new_station)
        new_station.setPrevious(current_station)
        
    def checkIntersection(self, line, current_station, new_station) -> bool:
        intersecting : bool = True
        
        (y1, x1) = current_station.position
        (y2, x2) = new_station.position
        
        for station in line.stations:
            if station.next != None and station.previous != None:
                (y3, x3) = station.previous.position
                (y4, x4) = station.next.position
                
                # Koeffizienten der Gleichung
                
                A = [[x2 - x1, -(x4 - x3)], 
                    [y2 - y1, -(y4 - y3)]]
                B = [x3 - x1, y3 - y1]

                # Determinante berechnen
                det = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
                if det == 0:
                    intersecting = False  # Linien sind parallel
                else:
                    # Cramersche Regel zur Lösung
                    t = ((B[0] * A[1][1]) - (B[1] * A[0][1])) / det
                    u = ((A[0][0] * B[1]) - (A[1][0] * B[0])) / det

                    # Schnittpunkt liegt innerhalb der Segmente
                    if 0 <= t <= 1 and 0 <= u <= 1:
                        # Schnittpunkt berechnen
                        intersection_x = x1 + t * (x2 - x1)
                        intersection_y = y1 + t * (y2 - y1)

                        # Prüfung auf Station
                        if (round(intersection_x), round(intersection_y)) in [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]:
                            intersecting = False  # Schnitt ist an Station

                        intersecting = True  # Linien schneiden sich
                
        return intersecting
        
    def checkStationValidality(self, new_station, current_station, lines : list) -> bool:
        valid = True
        
        if not new_station in self.stations:
            for line in lines:
                if self.checkIntersection(line, current_station, new_station):
                    valid = False
        else:
            valid = False    
            
        return valid
        
    def chooseNewStation(self, shape : str, lines : list) -> None:
        possible_stations = []
        current_station = None
        
        if shape != "joker":
        
            for station in self.ends:
                for neighbor in station.neighbor:
                    if neighbor.shape == shape or neighbor.shape == "any":
                        possible_stations.append((neighbor, station))
        else:
            for station in self.ends:
                for neighbor in station.neighbor:
                    possible_stations.append((neighbor, station))
                    
        if self.choose_mode == "random":
            
            if len(possible_stations) > 0:
            
                new_station = random.choice(possible_stations)
                
                new_station[1].setNext(new_station[0]) #Temporäres Eintragen der zu testenden Station als nächste Station
                
                while self.checkStationValidality(new_station[0], new_station[1], lines) == False and len(possible_stations) > 1:
                    possible_stations.remove(new_station)
                    new_station = random.choice(possible_stations)
                    
                new_station[1].setNext(None)
                
                self.addStation(new_station[0], new_station[1])
            
                print("New Station", new_station[0].position)
                print("Ends", end="")
                for end in self.ends:
                    print(end.position, end="")
            
            else:
                print("No possible station could be found. Skipping turn.")
            

class Card():
    def __init__(self, type : str, shape : str) -> None:
        self.type = type
        self.shape = shape
    
        

def game(cards : list, lines : list, stations : list) -> None:
    
    for line in lines:
        print("New line", line.color)
        card_copy = copy.copy(cards)
        
        underground_counter = 0
        
        while underground_counter < 5:
            
            card = random.choice(card_copy)            
            print()
            print("Card", card.shape)
            card_copy.remove(card)
            
            if card.type == "under":
                underground_counter += 1
                
            if card.shape == "switch":
                print("Skipping switch -> Not properly implemented")
            else:
                line.chooseNewStation(card.shape, lines)
                

    
    for line in lines:
        print(line.color)
        for station in line.stations:
            print(station.position)
        print()
    

if __name__ == "__main__":

    cards : list = preparation.prepare_cards()
    stations : list = preparation.prepare_stations()
    lines : list = preparation.prepare_lines()

    neighbors.load_neighbors(stations)

    game(cards, lines, stations)