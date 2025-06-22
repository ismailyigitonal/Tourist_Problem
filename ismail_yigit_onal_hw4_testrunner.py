#Ismail Yigit Onal 31214
import json # Used for reading JSON files (our test cases)
import os # Used for handling file paths
import ismail_yigit_onal_hw4_cs301 # Importing our main algorithm functions and data

# Function to run a single test given its JSON file path
def run_test(filepath):

    ismail_yigit_onal_hw4_cs301.stations.clear()
    ismail_yigit_onal_hw4_cs301.cities.clear()
    ismail_yigit_onal_hw4_cs301.edges.clear()

    # Open and read the JSON file
    with open(filepath, 'r') as file:
        data = json.load(file)

    # Add all stations (bus/train stations) from the file to the data structures
    for station in data["stations"]:
        ismail_yigit_onal_hw4_cs301.add_station(station["name"], station["city"], station["mode"])

    # Add all edges (connections between stations) from the file
    for edge in data["edges"]:
        ismail_yigit_onal_hw4_cs301.add_edge(edge["from"], edge["to"], edge["time"])

    start = data["start"] #starting station
    dist, parent = ismail_yigit_onal_hw4_cs301.bellman_ford(start) #I run the bellman_ford algorithm
    results = ismail_yigit_onal_hw4_cs301.summarize_by_city(dist, parent) #Summarize results city by city

    #Printing the test file name and results here
    print(f" Test: {os.path.basename(filepath)}")
    for city in results:
        print("City:", city)
        print("Time:", results[city]['time'], "minute")
        print("Route:", " -> ".join(results[city]['path']))
        print()


#All the tests to try from the Json_Tests File for me.
#run_test("Json_tests/test1_single_city.json")
#run_test("Json_tests/test2_two_cities_bus.json")
#run_test("Json_tests/test3_three_cities_chain_bus.json")
#run_test("Json_tests/test4_train_only.json")
#run_test("Json_tests/test5_transfer_within_city.json")
#run_test("Json_tests/test6_bus_better_than_train.json")
#run_test("Json_tests/test7_train_better_than_bus.json")
#run_test("Json_tests/test8_unreachable_city.json")
#run_test("Json_tests/test9_multiple_paths_to_city.json")


