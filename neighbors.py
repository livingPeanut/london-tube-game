def load_neighbors(stations_list):
    for station in stations_list:
        neighbors = []
        
        pos_neighbor_right = find_neighbor_right(station, stations_list)
        if pos_neighbor_right != None:
            neighbors.append(pos_neighbor_right)
        
        pos_neighbor_left = find_neighbor_left(station, stations_list)
        if pos_neighbor_left != None:
            neighbors.append(pos_neighbor_left)
        
        pos_neighbor_top = find_neighbor_top(station, stations_list)
        if pos_neighbor_top != None:
            neighbors.append(pos_neighbor_top)
        
        pos_neighbor_bottom = find_neighbor_bottom(station, stations_list)
        if pos_neighbor_bottom != None:
            neighbors.append(pos_neighbor_bottom)
        
        pos_neighbor_top_left = find_neighbor_top_left(station, stations_list)
        if pos_neighbor_top_left != None:
            neighbors.append(pos_neighbor_top_left)
        
        pos_neighbor_top_right = find_neighbor_top_right(station, stations_list)
        if pos_neighbor_top_right != None:
            neighbors.append(pos_neighbor_top_right)
                
        pos_neighbor_bottom_left = find_neighbor_bottom_left(station, stations_list)
        if pos_neighbor_bottom_left != None:
            neighbors.append(pos_neighbor_bottom_left)
                
        pos_neighbor_bottom_right = find_neighbor_bottom_right(station, stations_list)
        if pos_neighbor_bottom_right != None:
            neighbors.append(pos_neighbor_bottom_right)
            
        station.addNeighborList(neighbors)


def find_neighbor_right(current_station, stations_list):
    neighbor = None
    i = 1
    
    current_x = current_station.position[1]
    current_y = current_station.position[0]
    
    while i <= 9 and neighbor == None:
        for station in stations_list:
            if station.position == (current_y, current_x + i) and station != current_station:
                neighbor = station

        i += 1
    return neighbor
    
def find_neighbor_left(current_station, stations_list):
    neighbor = None
    i = 1
    
    current_x = current_station.position[1]
    current_y = current_station.position[0]
    
    while i <= 9 and neighbor == None:
        for station in stations_list:
            if station.position == (current_y, current_x - i) and station != current_station:
                neighbor = station

        i += 1
    return neighbor

def find_neighbor_top(current_station, stations_list):
    neighbor = None
    i = 1
    
    current_x = current_station.position[1]
    current_y = current_station.position[0]
    
    while i <= 9 and neighbor == None:
        for station in stations_list:
            if station.position == (current_y - i, current_x) and station != current_station:
                neighbor = station

        i += 1
    return neighbor

def find_neighbor_bottom(current_station, stations_list):
    neighbor = None
    i = 1
    
    current_x = current_station.position[1]
    current_y = current_station.position[0]
    
    while i <= 9 and neighbor == None:
        for station in stations_list:
            if station.position == (current_y + i, current_x) and station != current_station:
                neighbor = station

        i += 1
    return neighbor

def find_neighbor_top_left(current_station, stations_list):
    neighbor = None
    i = 0
    
    current_x = current_station.position[1]
    current_y = current_station.position[0]
    
    while i <= 9 and neighbor == None:
        for station in stations_list:
            if station.position == (current_y - i, current_x - i) and station != current_station:
                neighbor = station
        
        i += 1

    return neighbor

def find_neighbor_top_right(current_station, stations_list):
    neighbor = None
    i = 1
    
    current_x = current_station.position[1]
    current_y = current_station.position[0]
    
    while i <= 9 and neighbor == None:
        for station in stations_list:
            if station.position == (current_y - i, current_x + i) and station != current_station:
                neighbor = station
        
        i += 1

    return neighbor

def find_neighbor_bottom_left(current_station, stations_list):
    neighbor = None
    i = 1
    
    current_x = current_station.position[1]
    current_y = current_station.position[0]
    
    while i <= 9 and neighbor == None:
        for station in stations_list:
            if station.position == (current_y + i, current_x - i) and station != current_station:
                neighbor = station
        
        i += 1

    return neighbor

def find_neighbor_bottom_right(current_station, stations_list):
    neighbor = None
    i = 1
    
    current_x = current_station.position[1]
    current_y = current_station.position[0]
    
    while i <= 9 and neighbor == None:
        for station in stations_list:
            if station.position == (current_y + i, current_x + i) and station != current_station:
                neighbor = station
        
        i += 1

    return neighbor

def neighbor_self_test(stations : list) -> bool:
    valid = True
    
    for station in stations:
        for neighbor in station.neighbor:
            if not station in neighbor.neighbor:
                print("wrong neighbor detection", station.position, neighbor.position)
                valid = False
    
    return valid

def print_all_station_neighbors() -> None:
    import preparation
    stations : list = preparation.prepare_stations()
    load_neighbors(stations)
    for station in stations:
        print(station.position, end=" ")
        for neighbor in station.neighbor:
            print(neighbor.position, end=" ")
        print(len(station.neighbor))

if __name__ == "__main__":
    import preparation
    stations : list = preparation.prepare_stations()
    load_neighbors(stations)
    print(neighbor_self_test(stations))