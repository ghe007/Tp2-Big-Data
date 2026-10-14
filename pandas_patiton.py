import pandas as pd
import resource
import time

dataset_path = '/home/abderrahim/Downloads/TPsDownloads/bigData/flight_prices/itineraries.csv'

total_fare_count = 0
total_fare_sum = 0
t = time.perf_counter()

for chunk in pd.read_csv(dataset_path, chunksize=100_000, usecols=["totalFare", "totalTravelDistance", "travelDuration"]):
        fares = chunk["totalFare"]
        total_fare_sum += fares.sum()
        total_fare_count += fares.count()
t = time.perf_counter() - t

global_mean = total_fare_sum / total_fare_count

peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
peak_mb = peak / 1024

print("time: ", t) 
print("mean: ",global_mean) 
print("total: ", total_fare_sum)
print(f"max Ram used: {peak_mb:.2f} MB")