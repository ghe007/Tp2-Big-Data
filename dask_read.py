import dask.dataframe as dd
import dask
import time
import resource
import os

dataset_path = '/home/abderrahim/Downloads/TPsDownloads/bigData/flight_prices/itineraries.csv'
cols = ["totalFare", "totalTravelDistance", "travelDuration"]


t = time.perf_counter()
dask_df = dd.read_csv(dataset_path, blocksize="256MB" ,dtype={"totalTravelDistance": "float64"}, usecols=cols[:2]) 

total_fare_mean = dask_df["totalFare"].mean()
total_fare_sum = dask_df["totalFare"].sum()
result1 , result2 = dask.compute(total_fare_mean, total_fare_sum)
t = time.perf_counter() - t

peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
peak_mb = peak / 1024

print("time : ", t) 
print("dask (mean): ",result1)
print("dask (sum): ",result2)
print(f"dask max Ram used: {peak_mb:.2f} MB")
