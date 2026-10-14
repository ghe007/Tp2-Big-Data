import pandas as pd
import resource
import psutil


print(psutil.virtual_memory().percent,"%") # show the avilable ram

# read_csv mill make VScode Stop in my OS after a long time (if we did not used try except block)
dataset_path = '/home/abderrahim/Downloads/TPsDownloads/bigData/flight_prices/itineraries.csv'

try:
    
    df = pd.read_csv(dataset_path, usecols=["totalFare", "totalTravelDistance", "travelDuration"])
    print("dataset is loaded.")
except Exception:
    print("the program is out of memory")    
