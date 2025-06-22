#Ismail Yigit Onal 31214
import json
import os
import time # To measure runtime performance
import pandas as pd # To save results into a CSV file
import ismail_yigit_onal_hw4_cs301

# Function to run a single test file and measure its runtime
def run_test_with_timer(filepath):
    ismail_yigit_onal_hw4_cs301.stations.clear()
    ismail_yigit_onal_hw4_cs301.cities.clear()
    ismail_yigit_onal_hw4_cs301.edges.clear()

    with open(filepath, 'r') as file:
        data = json.load(file)

    for station in data["stations"]:
        ismail_yigit_onal_hw4_cs301.add_station(
            station["name"], station["city"], station["mode"]
        )
    for edge in data["edges"]:
        ismail_yigit_onal_hw4_cs301.add_edge(
            edge["from"], edge["to"], edge["time"]
        )


    start_station = data["start"]

    # Start the timer / run the algorithm / then stop the timer
    start_time = time.perf_counter()
    ismail_yigit_onal_hw4_cs301.bellman_ford(start_station)
    end_time = time.perf_counter()

    # Finding the runtime
    runtime = end_time - start_time

    #Calculating the input size (I use it while plotting the graphs.)
    input_size = len(ismail_yigit_onal_hw4_cs301.cities)

    #Here I return results as dictionary
    return {
        "filename": os.path.basename(filepath),
        "input_size": input_size,
        "runtime": runtime
    }
# Function to run all JSON tests inside a folder and save their timings
def run_all_tests_with_timing(folder="Performance_Tests", output_csv="performance_results.csv"):
    results = []

    # Go through each JSON file in the folder
    for filename in sorted(os.listdir(folder)):
        if filename.endswith(".json"):
            filepath = os.path.join(folder, filename)
            result = run_test_with_timer(filepath)
            results.append(result)
            print(f" {filename} - {result['runtime']:.6f} sec")

    # Save all results into a CSV file
    df = pd.DataFrame(results)
    df.to_csv(output_csv, index=False)
    print(f"\n CSV output saved to: {output_csv}")

# If this script is run directly start the performance testing
if __name__ == "__main__":
    run_all_tests_with_timing("Performance_Tests", "performance_results.csv")
