#İsmail Yigit Onal 31214
stations = {} #station_Name: (station_name, station_type)
cities = {} #city_Name: ("bus": station_name, "train": station_name)
edges = [] #(start_station, end_station, time)

#Function for adding stations
def add_station(station_name, city_name, mode):
    stations[station_name] = (city_name, mode)
    if city_name not in cities:
        cities[city_name] = {'bus': None, 'train': None}
    cities[city_name][mode] = station_name

#Function for adding edges
def add_edge(from_station, to_station, time):
    edges.append((from_station, to_station, time))

#Used Bellman_Ford algorithm to computes the quickest itinerary from a given train/bus station in a departure city to every other city in a given map.
def bellman_ford(source_station):
    dist = {} # shortest known time from source to each station
    parent = {} # previous station in optimal path
    for station in stations:
        dist[station] = 99999999 #like MAX_INT
        parent[station] = None
    dist[source_station] = 0

    # Relax all edges (v - 1) times
    for iteration in range(len(stations) - 1): #written iteration but, not using the value just for the loop.
        for u, v, w in edges:
            # If a shorter path is found
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

    return dist, parent

# Constructs the path to a given station from the source using parent links
def find_path(parents, station):
    path = []
    while station is not None:
        path.insert(0, station)
        station = parents[station]
    return path

# For each city, selects the best "minimum time" station "bus or train", then builds the corresponding path and time to reach that city.
def summarize_by_city(dist, parent):
    results = {}
    for city in cities:
        best_time = 99999999 #MAX_INT
        best_station = None
        for mode in ['bus', 'train']:
            station = cities[city][mode]
            if station is not None and dist[station] < best_time:
                best_time = dist[station]
                best_station = station
        if best_station is not None:
            results[city] = {
                'time': best_time,
                'path': find_path(parent, best_station)
            }
    return results


